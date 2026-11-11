#!/usr/bin/env pybricks-micropython

# ==================================================================
#  WRO FUTURE ENGINEERS - OBSTACLE CHALLENGE
#  Race program (competition version)
# ==================================================================
#
#  GOAL
#  ----
#  1. Leave the parking lot.
#  2. Drive 3 laps (12 corners) autonomously:
#       - RED pillar   -> the car passes on the RIGHT side of the pillar
#       - GREEN pillar -> the car passes on the LEFT side of the pillar
#  3. Come back to the parking lot and park parallel inside it.
#
#  HARDWARE (LEGO EV3, Pybricks MicroPython)
#  -----------------------------------------
#    Port A, B : medium motors, drive (same axle)
#    Port C    : medium motor, steering
#    Port S1   : gyro sensor (heading)
#    Port S2   : ultrasonic sensor, LEFT  (distance to the left wall)
#    Port S3   : ultrasonic sensor, RIGHT (distance to the right wall)
#    Port S4   : Pixy2 camera (I2C 0x54), signature 1 = red, 2 = green
#
#  CONVENTIONS
#  -----------
#    Steering angle : positive = wheels turned to the LEFT
#    Gyro heading   : a LEFT turn gives a NEGATIVE angle
#    Sides          : +1 = left, -1 = right
#    Driving direction ("direction"):
#       +1 = counter-clockwise (left turns, inner wall on the left)
#       -1 = clockwise        (right turns, inner wall on the right)
#    Lateral position x (mm): position of the car in the corridor,
#       0 = middle of the corridor, positive = left of the middle
#
#  RACE SEQUENCE (rules 6.12 to 6.14)
#  ----------------------------------
#    1. Power on: the program starts automatically, shows "READY" and
#       waits WITHOUT any measurement or computation.
#    2. CENTER button pressed at the start signal.
#    3. Gyro calibration (car standing still, about 4 s).
#    4. Driving direction found from the parking position: the parking
#       lot is along the OUTER wall, so the wall that is very close to
#       the car is the outer wall.
#    5. Unparking, 3 laps, parking.
#
#  HOW THE CAR DRIVES
#  ------------------
#    - The two ultrasonic sensors give the lateral position x of the
#      car in the corridor. The car steers to reach a target x by taking
#      a heading angle proportional to the error; the gyro holds that
#      heading.
#    - The camera gives, for the nearest pillar, its distance (from its
#      vertical position Y in the image) and its lateral position.
#      The car moves just enough to keep PILLAR_CLEARANCE between its
#      center and the pillar, on the correct side, and remembers the
#      pillar position until the pillar is behind the car.
#    - A corner is detected when the INNER wall ends (inner ultrasonic
#      reads more than OPEN_DISTANCE). The corner is driven with the
#      gyro, aiming at an ABSOLUTE heading (-90, -180, ...).
#    - "Track position" = distance travelled ALONG the corridor axis
#      (encoder distance x cosine of the heading error). It is used to
#      find the parking lot again after 3 laps.
#
#  LOG
#  ---
#    All measurements are kept in memory during the race and written at
#    the end to log_obstacle.csv on the EV3.
#
# ==================================================================

import sys
import os
import math

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Direction, Button, Stop
from pybricks.tools import wait, StopWatch

from pixycamev3.pixy2 import Pixy2

VERSION = "OBST-1"


# ==================================================================
#  TUNING PARAMETERS
#  Distances in millimetres (mm), angles in degrees, motor speeds in
#  degrees per second, times in milliseconds (ms).
# ==================================================================

MAX_RUN_TIME = 180000       # maximum race time (3 min), safety stop

# ---------- Drive ----------
DRIVE_SPEED = 250           # normal driving speed (deg/s)
WHEEL_DIAMETER = 56         # drive wheel diameter (mm)
GEAR_RATIO = 1.0            # wheel turns per motor turn
# Distance correction: real distance / measured distance.
# Measure it once (drive a known distance) and set it here.
DIST_SCALE = 1.0

# ---------- Steering ----------
MAX_STEERING = 30           # maximum steering angle while driving (deg)
STEER_LOCK = 30             # full steering angle for (un)parking (deg)
STEERING_SPEED = 600        # steering motor speed

# ---------- Lateral control ----------
K_LANE = 0.30               # heading angle (deg) per mm of lateral error
LANE_ANGLE_MAX = 45         # maximum heading angle to change lane (deg)
KG = 0.8                    # steering (deg) per degree of heading error
CENTER_TOLERANCE = 15       # lateral error ignored (dead zone, mm)
WALL_MAX = 1100             # beyond this distance a wall is "missing" (mm)
# In the Obstacle Challenge the corridors are 1 m wide. The sum of the two
# ultrasonic readings must then be about CORRIDOR_WIDTH - SENSOR_SPAN.
# A reading that does not fit (wall end seen by the wide sonar beam,
# pillar next to the car...) is rejected and the other wall is used alone.
CORRIDOR_WIDTH = 1000       # corridor width (mm)
SENSOR_SPAN = 160           # distance between the two sonar faces (mm)
SUM_TOLERANCE = 150         # accepted error on the sum of the readings
WALL_ANGLE_MAX = 40         # beyond this angle to the corridor axis the
                            # sonar readings are ignored (deg)
WALL_MIN = 80               # never plan closer than this to a wall (mm)
WALL_DANGER = 70            # closer than this: steer away at once (mm)

# ---------- Corners ----------
OPEN_DISTANCE = 1200        # inner wall "open" beyond this distance (mm)
OPEN_CONFIRM = 2            # consecutive readings to confirm the opening
TURN_ANGLE = 90             # corner angle (deg)
STEERING_TURN = 25          # steering angle during a corner (deg)
TURN_EARLY_STOP = 5         # wheels straightened 5 deg before the target
TURN_TIMEOUT = 5000         # maximum corner duration (ms), safety
TURN_WRONG_WAY = 15         # gyro turning the wrong way by 15 deg: stop
LOCK_DISTANCE = 700         # no new corner during this distance (mm):
                            # a corridor is 1 m long
INNER_SEEN_COUNT = 5        # the inner wall must have been seen this many
                            # times (car roughly straight) before an
                            # opening can count: a corner is a change
                            # "wall -> no wall"
INNER_SEEN_ANGLE = 20       # max angle to the corridor axis for that (deg)
TURN_LOOK_ANGLE = 45        # last part of a corner: the camera already
                            # sees the first pillar of the next corridor
STEERING_TURN_TIGHT = 30    # that pillar must be passed on the INNER side
STEERING_TURN_WIDE = 12     # that pillar must be passed on the OUTER side
TURN_ALIGN_MAX = 15         # a corner starts only when the car is within
                            # this angle of the corridor axis (deg)
TURN_ALIGN_DIST = 150       # ...or after this distance of straightening
TOTAL_CORNERS = 12          # 3 laps x 4 corners

# ---------- Pillars (camera) ----------
SIG_RED = 1                 # Pixy2 signature of the red pillars
SIG_GREEN = 2               # Pixy2 signature of the green pillars
MIN_HEIGHT = 6              # smaller blocks are ignored (noise, px)
MIN_RATIO = 0.8             # height / width minimum (else floor line)
CONFIRM_FRAMES = 3          # consecutive frames to confirm a pillar
Y_TRIGGER = 85              # start avoiding when pillar Y >= this
# Camera -> pillar distance from the vertical position Y in the image:
#   distance_mm = Y_K / (Y - Y_0)   (nominal model anchors: Y=130 at 300 mm, Y=83 at 1000 mm; raw calibration observations are not stored in this repository)
Y_0 = 63
Y_K = 20100
CAM_FOV = 60                # horizontal field of view of the Pixy2 (deg)
CAM_OFFSET = 100            # camera position ahead of the car center (mm)
# Minimum lateral distance between the CAR CENTER and a pillar:
#   half car width + half pillar width (25) + safety margin
PILLAR_CLEARANCE = 150      # mm
PASS_MARGIN = 200           # back to the middle when the car center is
                            # this far beyond the pillar (rear clear)
SWITCH_MARGIN = 20          # a pillar of the other colour is only taken
                            # once the car center is this far beyond the
                            # current pillar
PIXY_MAX_ERRORS = 20        # consecutive I2C errors before giving up


# ---------- Unparking ----------
# The car leaves the lot with a multi-point maneuver:
#   1. straight back UNPARK_BACK (more room in front)
#   2. UNPARK_CYCLES times: forward, wheels towards the track,
#      UNPARK_STEP mm, then backwards, wheels towards the wall,
#      UNPARK_STEP mm (each cycle turns the nose a little more out)
#   3. forward, wheels towards the track, until the heading turned
#      UNPARK_ANGLE, then wheels the other way until parallel again
# Every move is recorded: parking = the same moves played backwards.
UNPARK_SPEED = 120          # speed while leaving the lot
UNPARK_BACK = 30            # mm
UNPARK_CYCLES = 1           # number of forward/backward cycles
UNPARK_STEP = 40            # mm per move in a cycle
UNPARK_ANGLE = 60           # deg

# ---------- Parking ----------
PARK_SPEED = 120            # speed while parking
PARK_PREP_DIST = 700        # start approaching this far before the lot
PARK_LANE_MIN = 230         # never pass the lot with the outer sonar
                            # closer than this to the outer wall (mm):
                            # the boundary walls stick out 200 mm
PARK_BLOCK_DROP = 120       # outer reading drop next to a boundary wall
LOT_LENGTH = 390            # lot length (mm), to check the measurement
US_OFFSET = 0               # sonar position ahead of the car center (mm)
PARK_OFFSET = 0             # fine correction of the stop position (mm)
PARK_EXTRA_ANGLE = 4        # extra angle on the first reverse arc (deg):
                            # increase it if the car parks too far from
                            # the wall

# ---------- Gyro ----------
GYRO_CAL_TIME = 3000        # drift measurement time, car still (ms)
GYRO_DRIFT_MAX = 1.0        # acceptable drift (deg/s)
GYRO_AUTO_RECAL = 2         # automatic recalibration attempts

# ---------- Control loops ----------
LOOP_MS = 20                # main loop period (ms)
TURN_LOOP_MS = 10           # loop period during corners and maneuvers

LOG_FILE = "log_obstacle.csv"

PARAMS = [
    ("DRIVE_SPEED", DRIVE_SPEED), ("DIST_SCALE", DIST_SCALE),
    ("MAX_STEERING", MAX_STEERING), ("STEER_LOCK", STEER_LOCK),
    ("K_LANE", K_LANE), ("LANE_ANGLE_MAX", LANE_ANGLE_MAX), ("KG", KG),
    ("WALL_MAX", WALL_MAX), ("WALL_MIN", WALL_MIN),
    ("OPEN_DISTANCE", OPEN_DISTANCE), ("STEERING_TURN", STEERING_TURN),
    ("LOCK_DISTANCE", LOCK_DISTANCE), ("INNER_SEEN_COUNT", INNER_SEEN_COUNT),
    ("Y_TRIGGER", Y_TRIGGER),
    ("Y_0", Y_0), ("Y_K", Y_K), ("PILLAR_CLEARANCE", PILLAR_CLEARANCE),
    ("PASS_MARGIN", PASS_MARGIN), ("UNPARK_BACK", UNPARK_BACK),
    ("UNPARK_CYCLES", UNPARK_CYCLES), ("UNPARK_STEP", UNPARK_STEP),
    ("UNPARK_ANGLE", UNPARK_ANGLE), ("PARK_LANE_MIN", PARK_LANE_MIN),
    ("PARK_OFFSET", PARK_OFFSET), ("PARK_EXTRA_ANGLE", PARK_EXTRA_ANGLE),
    ("LOT_LENGTH", LOT_LENGTH),
    ("CORRIDOR_WIDTH", CORRIDOR_WIDTH), ("SENSOR_SPAN", SENSOR_SPAN),
]


# ==================================================================
#  HARDWARE
#  If a motor or sensor is not connected, the EV3 shows which one on
#  its screen and beeps 3 times, instead of stopping silently.
# ==================================================================

ev3 = EV3Brick()


def open_device(name, factory):
    """Create a motor or sensor. Return its name if it is missing."""
    try:
        return factory()
    except OSError:
        return name


DEVICES = [
    ("A motor", lambda: Motor(Port.A)),
    ("B motor", lambda: Motor(Port.B)),
    ("C steering", lambda: Motor(Port.C)),
    # CLOCKWISE: with this mounting, a left turn gives a negative angle
    ("S1 gyro", lambda: GyroSensor(Port.S1, Direction.CLOCKWISE)),
    ("S2 left US", lambda: UltrasonicSensor(Port.S2)),
    ("S3 right US", lambda: UltrasonicSensor(Port.S3)),
    ("S4 camera", lambda: Pixy2(port=4, i2c_address=0x54)),
]

_opened = [open_device(n, f) for n, f in DEVICES]
_missing = [d for d in _opened if isinstance(d, str)]
if _missing:
    ev3.screen.clear()
    ev3.screen.print("NOT CONNECTED:")
    for m in _missing:
        ev3.screen.print("  " + m)
    ev3.screen.print("Check the cable")
    ev3.screen.print("then restart")
    print("NOT CONNECTED:", ", ".join(_missing))
    for i in range(3):
        ev3.speaker.beep(200, 400)
        wait(200)
    wait(15000)
    raise SystemExit(1)

motor_a, motor_b, steering, gyro, ultra_left, ultra_right, pixy = _opened

SIGMAP = (1 << (SIG_RED - 1)) | (1 << (SIG_GREEN - 1))

# Distance travelled by the car for one degree of drive motor rotation
MM_PER_DEG = 3.14159 * WHEEL_DIAMETER * GEAR_RATIO / 360 * DIST_SCALE


# ==================================================================
#  CAR STATE (global variables)
# ==================================================================

clock = StopWatch()         # time since the program started
LOG = []                    # log kept in memory
phase = "INIT"              # current phase (for the log)
direction = 0               # driving direction (+1 / -1)
inner = 0                   # side of the inner wall (+1 left, -1 right)
outer = 0                   # side of the outer wall
target_heading = 0          # heading of the current corridor (deg)
last_steer = None           # last steering command sent

drift_rate = 0.0            # gyro drift measured at start (deg/s)
drift_t0 = 0                # time of the gyro reset (ms)

track_pos = 0.0             # position along the current corridor (mm)
_last_odo = 0.0             # encoder distance at the last update
io_errors = 0               # consecutive camera read errors


# ==================================================================
#  LOG
#  "D" lines: measurements of the main loop
#  "E" lines: events (pillar seen, corner, parking steps...)
# ==================================================================

HEADER = ("t_ms;phase;corner;track_pos;L_raw;R_raw;L_perp;R_perp;x_car;"
          "x_target;x_pillar;pos_err;heading_rel;head_goal;steer_cmd;"
          "steer_real;pix_sig;pix_x;pix_y;pix_h;pil_state")


def set_phase(p):
    global phase
    phase = p


def format_entry(r):
    if r[0] == "E":
        return "EVT;" + str(r[1]) + ";" + r[2] + ";" + r[3]
    return ";".join(str(x) for x in r[1:])


def event(msg):
    LOG.append(("E", clock.time(), phase, msg))


def write_log():
    lines = ["# VERSION " + VERSION]
    for name, val in PARAMS:
        lines.append("# " + name + " = " + str(val))
    lines.append("# EVT;t_ms;phase;message")
    lines.append(HEADER)
    for r in LOG:
        lines.append(format_entry(r))
    try:
        with open(LOG_FILE, "w") as f:
            for line in lines:
                f.write(line + "\n")
    except Exception as e:
        print("LOG FILE ERROR:", e)


# ==================================================================
#  BASIC FUNCTIONS
# ==================================================================

def clamp(value, low, high):
    return max(low, min(high, value))


def drive(speed):
    """Run both drive motors (negative speed = backwards)."""
    motor_a.run(speed)
    motor_b.run(speed)


def stop_drive():
    motor_a.brake()
    motor_b.brake()


def odo():
    """Signed encoder distance since the start (mm, forward positive)."""
    return (motor_a.angle() + motor_b.angle()) / 2 * MM_PER_DEG


def set_steering(angle, speed=STEERING_SPEED):
    """Turn the wheels to 'angle' (deg, + = left), without blocking."""
    global last_steer
    angle = round(angle)
    if angle != last_steer:
        steering.run_target(speed, angle, then=Stop.HOLD, wait=False)
        last_steer = angle


def check_stop():
    """Safety stop: race time exceeded or button pressed."""
    if clock.time() > MAX_RUN_TIME:
        raise Exception("MAX RUN TIME")
    if ev3.buttons.pressed():
        raise Exception("STOP BY BUTTON")


def heading():
    """Gyro heading (deg), corrected for the drift measured at start."""
    elapsed = (clock.time() - drift_t0) / 1000
    return gyro.angle() - drift_rate * elapsed


def heading_rel():
    """Heading relative to the current corridor axis (deg).
    Positive = the car points to the right of the corridor axis."""
    return heading() - target_heading


def update_track_pos():
    """Add the distance travelled ALONG the corridor axis since the
    last call. Must be called often (every loop)."""
    global track_pos, _last_odo
    o = odo()
    track_pos += (o - _last_odo) * math.cos(heading_rel() * 3.14159 / 180)
    _last_odo = o


def side_distance(side, lraw, rraw):
    """Raw ultrasonic distance on one side (+1 left, -1 right)."""
    return lraw if side == 1 else rraw


def read_walls():
    """Read both ultrasonic sensors.

    Returns raw distances, distances perpendicular to the walls (the
    car may be at an angle), the lateral position x of the car (None if
    a wall is missing) and the relative heading.
    """
    lraw = ultra_left.distance()
    rraw = ultra_right.distance()
    h = heading_rel()
    c = math.cos(h * 3.14159 / 180)
    lp = round(lraw * c)
    rp = round(rraw * c)
    half = (CORRIDOR_WIDTH - SENSOR_SPAN) / 2   # each side when centered
    l_ok = lraw < WALL_MAX
    r_ok = rraw < WALL_MAX
    x_car = None
    total = lp + rp
    if l_ok and r_ok and abs(total - 2 * half) <= SUM_TOLERANCE:
        x_car = round((rp - lp) / 2)            # both walls agree
    elif l_ok and r_ok and total > 2 * half:
        # one reading too long (wall end seen by the beam): use the
        # shorter one
        x_car = round(half - lp) if lp < rp else round(rp - half)
    elif l_ok and r_ok:
        # one reading too short (pillar or block next to the car): use
        # the longer one
        x_car = round(half - lp) if lp > rp else round(rp - half)
    elif l_ok:
        x_car = round(half - lp)
    elif r_ok:
        x_car = round(rp - half)
    # Too much angle: the sonar readings are not reliable any more,
    # and a position outside the corridor is impossible
    if abs(h) > WALL_ANGLE_MAX or (x_car is not None and abs(x_car) > half):
        x_car = None
    return lraw, rraw, lp, rp, x_car, h


# ==================================================================
#  CAMERA
# ==================================================================

def read_blocks():
    """Read the Pixy2. An isolated I2C error is ignored (no block)."""
    global io_errors
    try:
        count, blocks = pixy.get_blocks(SIGMAP, 4)
        io_errors = 0
        return count, blocks
    except OSError as e:
        io_errors += 1
        event("PIXY I2C ERROR " + str(io_errors) + " : " + str(e))
        if io_errors >= PIXY_MAX_ERRORS:
            raise
        return 0, []


def is_pillar(b):
    """True if a camera block looks like a pillar (not a floor line)."""
    if b.sig not in (SIG_RED, SIG_GREEN):
        return False
    if b.height < MIN_HEIGHT:
        return False
    if b.height < MIN_RATIO * b.width:
        return False
    return True


def nearest_pillar(h, x_car):
    """Nearest pillar of the CURRENT corridor.

    Returns (block, fwd, lat) or (None, None, None). The nearest pillar
    is the lowest one in the image (largest Y). Pillars whose computed
    position is outside the corridor (for example a pillar of the next
    corridor seen through the corner) are ignored.
    """
    count, blocks = read_blocks()
    best = (None, None, None)
    limit = CORRIDOR_WIDTH / 2 - 40
    for i in range(count):
        b = blocks[i]
        if not is_pillar(b):
            continue
        fwd, lat = pillar_geometry(b, h)
        if fwd is None or fwd < 50:
            continue
        if x_car is not None and abs(x_car + lat) > limit:
            continue
        if best[0] is None or b.y_center > best[0].y_center:
            best = (b, fwd, lat)
    return best


def pillar_geometry(p, h):
    """Pillar position relative to the CAR CENTER, along the corridor.

    fwd = distance ahead of the car center (mm)
    lat = lateral offset from the car center (mm, + = left)
    The camera is CAM_OFFSET mm ahead of the car center, and the car
    may be at an angle h to the corridor axis: both are taken into
    account.
    """
    if p.y_center <= Y_0 + 3:
        return None, None
    dist = Y_K / (p.y_center - Y_0)                           # from camera
    bearing_img = (158 - p.x_center) * (CAM_FOV / 2) / 158    # + = left
    a = (bearing_img - h) * 3.14159 / 180                     # + = left
    hr = h * 3.14159 / 180
    fwd = CAM_OFFSET * math.cos(hr) + dist * math.cos(a)
    lat = -CAM_OFFSET * math.sin(hr) + dist * math.sin(a)
    return round(fwd), round(lat)


# ==================================================================
#  LATERAL CONTROL
# ==================================================================

def lane_target(lane, x_pillar, lp, rp):
    """Target lateral position (mm, + = left of the middle).

    lane = 0  : middle of the corridor
    lane = -1 : RED pillar, the car passes on its RIGHT
    lane = +1 : GREEN pillar, the car passes on its LEFT
    The car moves only as far as needed to keep PILLAR_CLEARANCE,
    and never closer than WALL_MIN to a wall.
    """
    if lane == 0 or x_pillar is None:
        return 0
    half = (CORRIDOR_WIDTH - SENSOR_SPAN) / 2
    x_right_max = -(half - WALL_MIN)
    x_left_max = half - WALL_MIN
    if lane == -1:
        return round(max(x_right_max, min(0, x_pillar - PILLAR_CLEARANCE)))
    return round(min(x_left_max, max(0, x_pillar + PILLAR_CLEARANCE)))


def drive_to(x_car, x_target, h, lp, rp, l_ok, r_ok, speed):
    """Steer towards the target lateral position.

    The lateral error gives a heading angle (limited to LANE_ANGLE_MAX);
    the gyro steering then holds that heading.
    """
    pos_err = 0
    if x_car is not None:
        pos_err = x_car - x_target          # > 0: car too far left
    if abs(pos_err) <= CENTER_TOLERANCE:
        pos_err = 0

    head_goal = clamp(K_LANE * pos_err, -LANE_ANGLE_MAX, LANE_ANGLE_MAX)
    cmd = clamp(KG * (h - head_goal), -MAX_STEERING, MAX_STEERING)

    # Safety: too close to a wall -> steer away from it at once
    if l_ok and lp < WALL_DANGER:
        cmd = -MAX_STEERING
    elif r_ok and rp < WALL_DANGER:
        cmd = MAX_STEERING

    set_steering(cmd)
    drive(speed)
    return pos_err, round(head_goal), cmd


# ==================================================================
#  GYRO MANEUVERS (corners, unparking, parking)
# ==================================================================

def maneuver(steer, speed, goal, name, timeout=TURN_TIMEOUT):
    """Drive with a fixed steering angle until the heading reaches
    'goal' (deg). Works forwards (speed > 0) and backwards (speed < 0)."""
    set_steering(steer, STEERING_SPEED)
    wait(150)                               # let the wheels turn first
    drive(speed)
    start_err = heading() - goal
    sign = 1 if start_err > 0 else -1
    timer = StopWatch()
    while (heading() - goal) * sign > 2:
        check_stop()
        update_track_pos()
        if timer.time() > timeout:
            event(name + " TIMEOUT heading=" + str(round(heading())))
            break
        wait(TURN_LOOP_MS)
    stop_drive()
    event(name + " done heading=" + str(round(heading()))
          + " goal=" + str(round(goal)))


def drive_arc(steer, dist, speed, name):
    """Drive 'dist' mm (dist < 0: backwards) with a fixed steering
    angle. Returns the distance really travelled (signed)."""
    set_steering(steer, STEERING_SPEED)
    wait(150)                               # let the wheels turn first
    start = odo()
    drive(speed if dist > 0 else -speed)
    timer = StopWatch()
    while abs(odo() - start) < abs(dist):
        check_stop()
        update_track_pos()
        if timer.time() > TURN_TIMEOUT:
            break
        wait(TURN_LOOP_MS)
    stop_drive()
    moved = odo() - start
    event(name + " done moved=" + str(round(moved))
          + " heading=" + str(round(heading())))
    return moved


def drive_straight(dist, speed, name):
    """Drive 'dist' mm with straight wheels (dist < 0: backwards)."""
    return drive_arc(0, dist, speed, name)


def do_turn():
    """Drive a corner with the gyro (target_heading already updated)."""
    set_phase("TURN")
    h_start = heading()
    event("TURN START heading=" + str(round(h_start))
          + " target=" + str(target_heading))
    set_steering(STEERING_TURN * direction, STEERING_SPEED)
    drive(DRIVE_SPEED)
    timer = StopWatch()
    while True:
        check_stop()
        update_track_pos()
        h = heading()
        if (h - target_heading) * direction <= TURN_EARLY_STOP:
            break
        if timer.time() > TURN_TIMEOUT:
            event("TURN TIMEOUT heading=" + str(round(h)))
            break
        if (h - h_start) * direction > TURN_WRONG_WAY:
            event("GYRO SIGN WRONG")
            raise Exception("GYRO SIGN WRONG")
        # End of the corner: the camera sees the first pillar of the next
        # corridor -> tighter turn if it must be passed on the inner side,
        # wider turn if it must be passed on the outer side
        if (h - target_heading) * direction <= TURN_LOOK_ANGLE:
            p, fwd, lat = nearest_pillar(h - target_heading, None)
            if p is not None and fwd < 900:
                pass_side = -1 if p.sig == SIG_RED else 1
                steer = STEERING_TURN_TIGHT if pass_side == inner \
                    else STEERING_TURN_WIDE
                set_steering(steer * direction, STEERING_SPEED)
        wait(TURN_LOOP_MS)
    set_steering(0, STEERING_SPEED)
    event("TURN END heading=" + str(round(heading()))
          + " time=" + str(timer.time()) + "ms")


# ==================================================================
#  GYRO CALIBRATION (after the start button, car standing still)
# ==================================================================

def wait_button(buttons):
    while True:
        pressed = ev3.buttons.pressed()
        for b in buttons:
            if b in pressed:
                while ev3.buttons.pressed():
                    wait(10)
                return b
        wait(10)


def measure_drift():
    wait(1500)
    gyro.reset_angle(0)
    t = StopWatch()
    wait(GYRO_CAL_TIME)
    return gyro.angle() / (t.time() / 1000)


def gyro_sysfs_path():
    """ev3dev system folder of the sensor on port S1."""
    base = "/sys/class/lego-sensor/"
    for name in os.listdir(base):
        try:
            with open(base + name + "/address") as f:
                if f.read().strip().endswith("in1"):
                    return base + name
        except Exception:
            pass
    return None


def hw_recalibrate():
    """Force the gyro to recalibrate itself (ev3dev GYRO-CAL mode)."""
    global gyro
    try:
        path = gyro_sysfs_path()
        if path is None:
            return
        with open(path + "/mode", "w") as f:
            f.write("GYRO-CAL")
        wait(1500)
        with open(path + "/mode", "w") as f:
            f.write("GYRO-ANG")
        wait(1000)
        gyro = GyroSensor(Port.S1, Direction.CLOCKWISE)
        event("AUTO RECAL done")
    except Exception as e:
        event("AUTO RECAL ERROR " + str(e))


def calibrate_gyro():
    """Measure the drift; recalibrate if it is too high; if it stays
    high, start anyway (the drift is removed by heading())."""
    global drift_rate, drift_t0
    for attempt in range(GYRO_AUTO_RECAL + 1):
        ev3.screen.clear()
        ev3.screen.print("GYRO CALIBRATION")
        ev3.screen.print("DO NOT TOUCH")
        try:
            drift_rate = measure_drift()
        except Exception as e:
            event("GYRO READ ERROR " + str(e))
            drift_rate = 0.0
        event("GYRO CAL drift_rate=" + str(round(drift_rate, 2)) + " deg/s")
        if abs(drift_rate) <= GYRO_DRIFT_MAX:
            break
        if attempt < GYRO_AUTO_RECAL:
            hw_recalibrate()
    gyro.reset_angle(0)
    drift_t0 = clock.time()


# ==================================================================
#  UNPARKING AND PARKING
#  The car stands in the lot, parallel to the outer wall. It leaves the
#  lot with a multi-point maneuver and RECORDS every move. After the 3
#  laps it stops exactly where the unparking ended, then plays the same
#  moves BACKWARDS (same steering, opposite direction, reverse order):
#  the car follows the same path back into the lot.
# ==================================================================

unpark_moves = []           # recorded moves: ("D", steer, mm) or
                            # ("H", steer, heading relative to the corridor)
unpark_end_pos = 0.0        # track position at the end of the unparking
unpark_end_gap = 0          # outer sonar distance at the end (mm)


def unpark():
    global unpark_end_pos, unpark_end_gap
    set_phase("UNPARK")
    track_steer = STEER_LOCK * inner        # wheels towards the track
    wall_steer = STEER_LOCK * outer         # wheels towards the wall

    moved = drive_straight(-UNPARK_BACK, UNPARK_SPEED, "UNPARK BACK")
    unpark_moves.append(("D", 0, moved))
    for i in range(UNPARK_CYCLES):
        moved = drive_arc(track_steer, UNPARK_STEP, UNPARK_SPEED, "UNPARK FWD")
        unpark_moves.append(("D", track_steer, moved))
        moved = drive_arc(wall_steer, -UNPARK_STEP, UNPARK_SPEED, "UNPARK REV")
        unpark_moves.append(("D", wall_steer, moved))

    # Heading reached after the cycles (needed to replay the next move),
    # stored RELATIVE to the corridor (the absolute heading changes by
    # 360 deg per lap)
    unpark_moves.append(("H", track_steer, heading_rel()))
    maneuver(track_steer, UNPARK_SPEED,
             target_heading - UNPARK_ANGLE * inner, "UNPARK OUT")
    unpark_moves.append(("H", wall_steer, heading_rel()))
    maneuver(wall_steer, UNPARK_SPEED, target_heading, "UNPARK STRAIGHTEN")
    set_steering(0, STEERING_SPEED)

    lraw = ultra_left.distance()
    rraw = ultra_right.distance()
    unpark_end_pos = track_pos
    unpark_end_gap = side_distance(outer, lraw, rraw)
    event("UNPARK END track_pos=" + str(round(unpark_end_pos))
          + " outer_gap=" + str(unpark_end_gap))


def park():
    """Replay the unparking moves backwards."""
    set_phase("PARK")
    stop_drive()
    wait(200)
    event("PARK START track_pos=" + str(round(track_pos))
          + " heading_rel=" + str(round(heading_rel())))
    first_turn = True
    for kind, steer, value in reversed(unpark_moves):
        if kind == "H" and first_turn:
            # deeper first arc: brings the car closer to the wall
            value = value - PARK_EXTRA_ANGLE * inner
            first_turn = False
        if kind == "D":
            # same steering, same distance, opposite direction
            drive_arc(steer, -value, PARK_SPEED, "PARK MOVE")
        else:
            # same steering, backwards, until the recorded heading
            maneuver(steer, -PARK_SPEED, target_heading + value, "PARK TURN")
    set_steering(0, STEERING_SPEED)
    motor_a.hold()
    motor_b.hold()
    lraw = ultra_left.distance()
    rraw = ultra_right.distance()
    event("PARKED outer_wall=" + str(side_distance(outer, lraw, rraw))
          + " heading_rel=" + str(round(heading_rel())))


# ==================================================================
#  MAIN PROGRAM
# ==================================================================

try:
    # The wheels must be physically straight at power on:
    # this position becomes the steering "zero".
    steering.reset_angle(0)
    motor_a.reset_angle(0)
    motor_b.reset_angle(0)
    event("VERSION " + VERSION)

    # ---------- Waiting state (rule 6.12): no measurement ----------
    ev3.screen.clear()
    ev3.screen.print("WRO OBSTACLE")
    ev3.screen.print(VERSION)
    ev3.screen.print("")
    ev3.screen.print("READY")
    ev3.screen.print("CENTER = START")
    ev3.speaker.beep()
    wait_button([Button.CENTER])
    event("START BUTTON")

    # ---------- Start: gyro calibration, car still in the lot ----------
    calibrate_gyro()

    # ---------- Driving direction from the parking position ----------
    # The lot is along the OUTER wall: the closer wall is the outer one.
    l0 = ultra_left.distance()
    r0 = ultra_right.distance()
    outer = 1 if l0 < r0 else -1
    inner = -outer
    direction = inner                  # inner wall on the left = CCW
    event("DIRECTION " + ("CCW (left turns)" if direction == 1
                          else "CW (right turns)")
          + " L=" + str(l0) + " R=" + str(r0))

    ev3.screen.clear()
    ev3.screen.print("RUN")

    _last_odo = odo()
    track_pos = 0.0                    # lot center = position 0
    unpark()

    # ---------- Race state ----------
    set_phase("RACE")
    corner_count = 0
    lock_until = track_pos             # no corner detection before this
    open_count = 0
    align_start = None                 # straightening before a corner
    inner_seen = 0                     # inner wall readings in this corridor

    # Pillar avoidance
    pil_state = "CENTER"               # CENTER / AVOID / PASS
    lane = 0
    candidate_sig = None
    seen_count = 0
    lost_count = 0
    avoid_sig = None
    avoid_lost = 0
    pil_pos = 0.0                      # pillar position along the corridor
    x_pillar = None                    # pillar lateral position

    # Measurements used to find the lot again (see header)
    d0 = None                          # lot center -> 1st opening
    side_lengths = []                  # corner 4 / 8 end -> next opening
    turn_end_pos = 0.0
    lot_pos = None                     # lot center position, last lap
    blocks = []                        # parking walls seen (last lap)
    in_block = False
    block_start = 0.0

    while True:
        check_stop()
        update_track_pos()
        lraw, rraw, lp, rp, x_car, h = read_walls()
        inner_raw = side_distance(inner, lraw, rraw)
        outer_raw = side_distance(outer, lraw, rraw)
        outer_perp = lp if outer == 1 else rp

        # ---------- 1) Camera: nearest pillar, confirmed ----------
        p, fwd, lat = nearest_pillar(h, x_car)
        if p is None:
            lost_count += 1
            if lost_count >= 3:
                candidate_sig = None
                seen_count = 0
        else:
            lost_count = 0
            if p.sig == candidate_sig:
                seen_count += 1
            else:
                candidate_sig = p.sig
                seen_count = 1
        confirmed = p is not None and seen_count >= CONFIRM_FRAMES
        trigger = confirmed and fwd is not None and p.y_center >= Y_TRIGGER

        # ---------- 2) Pillar avoidance ----------
        # pil_pos = track position where the CAR CENTER reaches the pillar
        if trigger and (pil_state == "CENTER" or (
                p.sig != avoid_sig and track_pos >= pil_pos + SWITCH_MARGIN)):
            lane = -1 if p.sig == SIG_RED else 1
            avoid_sig = p.sig
            avoid_lost = 0
            pil_pos = track_pos + fwd
            x_pillar = (x_car if x_car is not None else 0) + lat
            pil_state = "AVOID"
            event("PILLAR " + ("RED" if lane == -1 else "GREEN")
                  + " ahead=" + str(fwd) + " x_pillar=" + str(round(x_pillar))
                  + " x_car=" + str(x_car)
                  + " -> PASS " + ("RIGHT" if lane == -1 else "LEFT"))
        elif pil_state != "CENTER" and confirmed and p.sig == avoid_sig \
                and fwd is not None:
            pil_pos = track_pos + fwd
            if x_car is not None:
                x_pillar = 0.5 * x_pillar + 0.5 * (x_car + lat)
            avoid_lost = 0
            pil_state = "AVOID"
        elif pil_state == "AVOID":
            avoid_lost += 1
            if avoid_lost >= 3:
                pil_state = "PASS"      # out of view, position remembered
        if pil_state != "CENTER" and track_pos >= pil_pos + PASS_MARGIN:
            pil_state = "CENTER"
            lane = 0
            x_pillar = None
            avoid_sig = None
            event("PILLAR PASSED track_pos=" + str(round(track_pos)))

        # ---------- 3) Corner detection (inner wall ends) ----------
        # The inner wall must be seen first in this corridor: when the car
        # is at an angle just after a corner, the inner sonar can look
        # back into the corner and read "far" without any real opening.
        if inner_raw < WALL_MAX and abs(h) < INNER_SEEN_ANGLE:
            inner_seen += 1
        if corner_count < TOTAL_CORNERS and track_pos >= lock_until \
                and inner_seen >= INNER_SEEN_COUNT \
                and inner_raw > OPEN_DISTANCE:
            open_count += 1
        elif align_start is None:
            open_count = 0

        # Opening confirmed while the car is still at an angle (in the
        # middle of a pillar avoidance): straighten first, then turn
        if open_count >= OPEN_CONFIRM and abs(h) > TURN_ALIGN_MAX:
            if align_start is None:
                align_start = track_pos
                event("OPENING while angled (" + str(round(h))
                      + " deg): straighten first")
            if track_pos - align_start < TURN_ALIGN_DIST:
                open_count = OPEN_CONFIRM      # keep the opening pending
                set_steering(clamp(KG * h, -MAX_STEERING, MAX_STEERING))
                drive(DRIVE_SPEED)
                wait(LOOP_MS)
                continue

        if open_count >= OPEN_CONFIRM:
            open_count = 0
            align_start = None
            opening = corner_count + 1
            event("OPENING " + str(opening) + " track_pos="
                  + str(round(track_pos)))
            if opening == 1:
                d0 = track_pos
            elif opening in (5, 9):
                side_lengths.append(track_pos - turn_end_pos)

            # New corridor: absolute heading, track position restarts
            target_heading -= TURN_ANGLE * direction
            do_turn()
            set_phase("RACE")
            corner_count += 1
            track_pos = 0.0
            _last_odo = odo()
            turn_end_pos = 0.0
            lock_until = LOCK_DISTANCE
            inner_seen = 0
            # Pillars of the previous corridor are behind the car
            pil_state, lane, x_pillar, avoid_sig = "CENTER", 0, None, None
            event("CORNER " + str(corner_count) + "/" + str(TOTAL_CORNERS))

            if corner_count == TOTAL_CORNERS:
                # Back in the starting corridor: where is the lot?
                if d0 is not None and side_lengths:
                    L = sum(side_lengths) / len(side_lengths)
                    lot_pos = L - d0
                else:
                    lot_pos = 1000
                event("LOT EXPECTED at track_pos=" + str(round(lot_pos)))
            continue

        # ---------- 4) Last lap: approach the parking lot ----------
        parking = lot_pos is not None and track_pos >= lot_pos - PARK_PREP_DIST
        if parking:
            # Stop where the unparking ended (relative to the lot center)
            stop_pos = lot_pos + unpark_end_pos + PARK_OFFSET
            # Parking boundary walls seen by the outer sensor: they refine
            # the position of the lot (center = middle of the two walls)
            near = outer_raw < max(unpark_end_gap, PARK_LANE_MIN) - PARK_BLOCK_DROP
            if near and not in_block:
                in_block, block_start = True, track_pos
            elif not near and in_block:
                in_block = False
                blocks.append((block_start + track_pos) / 2)
                event("PARKING WALL at " + str(round(blocks[-1])))
                if len(blocks) == 1:
                    # First wall = rear end of the lot (walls are 20 mm
                    # thick): lot center half a lot length further
                    lot_pos = blocks[0] + LOT_LENGTH / 2 + 10 + US_OFFSET
                    event("LOT MEASURED (1 wall) at " + str(round(lot_pos)))
                    stop_pos = lot_pos + unpark_end_pos + PARK_OFFSET
                if len(blocks) >= 2 and \
                        abs(blocks[-1] - blocks[-2] - LOT_LENGTH) < 150:
                    lot_pos = (blocks[-1] + blocks[-2]) / 2 + US_OFFSET
                    event("LOT MEASURED at " + str(round(lot_pos)))
                    stop_pos = lot_pos + unpark_end_pos + PARK_OFFSET

            if track_pos >= stop_pos:
                break                     # in position: park

        # ---------- 5) Steering ----------
        if parking:
            # Lane along the outer wall, at the distance where the
            # unparking ended (but never too close to the boundary walls)
            lane_gap = max(unpark_end_gap, PARK_LANE_MIN)
            half = (CORRIDOR_WIDTH - SENSOR_SPAN) / 2
            x_target = round(outer * (half - lane_gap))
            if in_block or outer_perp < lane_gap - PARK_BLOCK_DROP:
                x_used = None             # wall reading hidden by a block
            else:
                x_used = x_car
            # Slow down close to the stop position
            speed = PARK_SPEED if track_pos > stop_pos - 200 else DRIVE_SPEED
        else:
            x_target = lane_target(lane, x_pillar, lp, rp)
            x_used = x_car
            speed = DRIVE_SPEED
        perr, hgoal, cmd = drive_to(x_used, x_target, h, lp, rp,
                                    lraw < WALL_MAX, rraw < WALL_MAX, speed)

        # ---------- 6) Log ----------
        if p is not None:
            pix = (p.sig, p.x_center, p.y_center, p.height)
        else:
            pix = ("-", "-", "-", "-")
        LOG.append(("D", clock.time(), phase, corner_count, round(track_pos),
                    lraw, rraw, lp, rp, "-" if x_car is None else x_car,
                    x_target, "-" if x_pillar is None else round(x_pillar),
                    round(perr), round(h), hgoal, round(cmd, 1),
                    steering.angle(), pix[0], pix[1], pix[2], pix[3],
                    pil_state))

        wait(LOOP_MS)

    # ---------- Parallel parking ----------
    stop_drive()
    wait(200)
    update_track_pos()
    error = stop_pos - track_pos           # small overshoot correction
    if abs(error) > 10:
        drive_straight(clamp(error, -100, 100), PARK_SPEED, "PARK ALIGN")
    park()
    set_phase("END")
    ev3.screen.clear()
    ev3.screen.print("FINISHED")
    ev3.speaker.beep()

except Exception as e:
    event("ERROR " + str(e))
    sys.print_exception(e)

finally:
    stop_drive()
    steering.hold()
    event("STOP total_time=" + str(clock.time()) + "ms")
    write_log()