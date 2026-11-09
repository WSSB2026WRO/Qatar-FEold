#!/usr/bin/env pybricks-micropython

# ==================================================================
#  WRO FUTURE ENGINEERS - OPEN CHALLENGE
#  Race program (competition version)
# ==================================================================
#
#  GOAL
#  ----
#  Drive 3 laps (12 corners) autonomously, in the randomly drawn
#  direction (clockwise or counter-clockwise), without touching the
#  walls, then stop in the starting section.
#
#  HARDWARE (LEGO EV3, Pybricks MicroPython)
#  -----------------------------------------
#    Port A, B : medium motors, drive (same axle)
#    Port C    : medium motor, steering
#    Port S1   : gyro sensor (heading)
#    Port S2   : ultrasonic sensor, LEFT  (distance to the left wall)
#    Port S3   : ultrasonic sensor, RIGHT (distance to the right wall)
#
#  CONVENTIONS
#  -----------
#    Steering angle : positive = wheels turned to the LEFT
#    Gyro heading   : a LEFT turn gives a NEGATIVE angle
#    Driving direction ("direction"):
#       +1 = left turns (counter-clockwise)
#       -1 = right turns (clockwise)
#        0 = not known yet (before the first corner)
#
#  RACE SEQUENCE (rules 6.12 to 6.14)
#  ----------------------------------
#    1. Power on: the program starts automatically, shows "READY" and
#       waits WITHOUT any measurement or computation.
#    2. CENTER button pressed at the start signal.
#    3. Gyro calibration (car standing still, about 4 s).
#    4. Race: straight -> corner detected -> corner -> ...
#    5. After the 12th corner: automatic stop at the starting position.
#
#  HOW THE CAR DRIVES
#  ------------------
#    - On straights, the car stays in the middle of the corridor using
#      both ultrasonic sensors, and stays parallel to the walls using
#      the gyro.
#    - A corner is detected when one side "opens" (wall farther than
#      1 m): this is the end of the inner wall.
#    - The corner is driven with the gyro, aiming at an ABSOLUTE heading
#      (-90, -180, -270... degrees) so that errors do not add up.
#    - The distance travelled is measured with the motor encoders.
#
#  LOG
#  ---
#    All measurements are kept in memory during the race and written at
#    the end to log_open.csv on the EV3 (to analyse the race later).
#    Nothing is printed during the race, to keep the control loop fast.
#
# ==================================================================

import sys
import os

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Direction, Button, Stop
from pybricks.tools import wait, StopWatch

VERSION = "OPEN-COMP-2"


# ==================================================================
#  TUNING PARAMETERS
#  Distances in millimetres (mm), angles in degrees, motor speeds in
#  degrees per second, times in milliseconds (ms).
# ==================================================================

MAX_RUN_TIME = 180000       # maximum race time (3 min), safety stop

# ---------- Drive ----------
DRIVE_SPEED = 300           # drive motor speed (deg/s)
WHEEL_DIAMETER = 56         # drive wheel diameter (mm)
GEAR_RATIO = 1.0            # wheel turns per motor turn

# ---------- Steering ----------
MAX_STEERING = 10           # maximum steering angle on straights (deg)
STEERING_SPEED = 450        # steering motor speed on straights
STEERING_TURN = 20          # steering angle during a corner (deg)
CORNER_STEERING_SPEED = 600 # steering motor speed during a corner

# ---------- Centering in the corridor ----------
CENTER_TOLERANCE = 10       # left/right difference ignored (dead zone, mm)
KP = 0.09                   # steering (deg) per mm of left/right difference
KG = 0.6                    # steering (deg) per degree of heading error
WALL_MAX = 950              # beyond this distance a wall is "missing" (mm)
# If the car is more than 12 deg off the corridor axis, the ultrasonic
# sensors measure at an angle (wrong values): the walls are ignored and
# the car straightens with the gyro only.
WALL_HEADING_MAX = 12
# Safety: a wall closer than 15 cm -> steer away from it first
WALL_DANGER = 150

# ---------- Gyro ----------
GYRO_CAL_TIME = 3000        # drift measurement time, car still (ms)
GYRO_DRIFT_MAX = 1.0        # acceptable drift (deg/s)
GYRO_AUTO_RECAL = 2         # automatic recalibration attempts

# ---------- Corners ----------
OPEN_DISTANCE = 1000        # a side is "open" when the wall is beyond 1 m
OPEN_CONFIRM = 2            # consecutive readings to confirm the opening
TURN_ANGLE = 90             # corner angle (deg)
TURN_EARLY_STOP = 5         # wheels straightened 5 deg before the target
TURN_TIMEOUT = 4000         # maximum corner duration (ms), safety
TURN_WRONG_WAY = 15         # gyro turning the wrong way by 15 deg: stop
PRE_TURN_DISTANCE = 0       # distance driven before steering (mm)
LOCK_DISTANCE = 450         # after a corner, no detection for 450 mm
TOTAL_CORNERS = 12          # 3 laps x 4 corners

# ---------- Final stop at the starting position ----------
# During the race the car measures:
#   d0 = distance between its starting position and the 1st opening
#   L  = useful length of the starting side (end of corner 4 -> next
#        opening, and the same after corner 8; the average is used)
# After the 12th corner it drives L - d0: it is back at its start point.
FINAL_DISTANCE = 600        # fallback distance if the measurement failed
FINAL_OFFSET = 0            # fine correction (+ = farther, - = shorter)
FINAL_SLOW_DIST = 150       # the last 150 mm are driven slowly
FINAL_SLOW_SPEED = 150      # speed of the final approach (deg/s)

# ---------- Control loops ----------
LOOP_MS = 20                # loop period on straights (ms)
TURN_LOOP_MS = 10           # loop period during a corner (ms)

LOG_FILE = "log_open.csv"   # log file written at the end of the race

# Parameters copied at the top of the log (to know which settings
# were used for a race)
PARAMS = [
    ("DRIVE_SPEED", DRIVE_SPEED), ("WHEEL_DIAMETER", WHEEL_DIAMETER),
    ("GEAR_RATIO", GEAR_RATIO), ("MAX_STEERING", MAX_STEERING),
    ("STEERING_SPEED", STEERING_SPEED), ("STEERING_TURN", STEERING_TURN),
    ("CORNER_STEERING_SPEED", CORNER_STEERING_SPEED),
    ("CENTER_TOLERANCE", CENTER_TOLERANCE), ("KP", KP), ("KG", KG),
    ("WALL_MAX", WALL_MAX), ("WALL_HEADING_MAX", WALL_HEADING_MAX),
    ("WALL_DANGER", WALL_DANGER),
    ("GYRO_CAL_TIME", GYRO_CAL_TIME), ("GYRO_DRIFT_MAX", GYRO_DRIFT_MAX),
    ("OPEN_DISTANCE", OPEN_DISTANCE), ("OPEN_CONFIRM", OPEN_CONFIRM),
    ("TURN_ANGLE", TURN_ANGLE), ("TURN_EARLY_STOP", TURN_EARLY_STOP),
    ("TURN_TIMEOUT", TURN_TIMEOUT), ("PRE_TURN_DISTANCE", PRE_TURN_DISTANCE),
    ("LOCK_DISTANCE", LOCK_DISTANCE), ("TOTAL_CORNERS", TOTAL_CORNERS),
    ("FINAL_DISTANCE", FINAL_DISTANCE), ("FINAL_OFFSET", FINAL_OFFSET),
    ("FINAL_SLOW_DIST", FINAL_SLOW_DIST), ("FINAL_SLOW_SPEED", FINAL_SLOW_SPEED),
    ("LOOP_MS", LOOP_MS),
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

motor_a, motor_b, steering, gyro, ultra_left, ultra_right = _opened

# Distance travelled by the car for one degree of drive motor rotation
MM_PER_DEG = 3.14159 * WHEEL_DIAMETER * GEAR_RATIO / 360


# ==================================================================
#  CAR STATE (global variables)
# ==================================================================

clock = StopWatch()         # time since the program started
LOG = []                    # log kept in memory
phase = "INIT"              # current phase (INIT, STRAIGHT, TURN, LOCK...)
direction = 0               # driving direction (+1, -1, or 0 if unknown)
corner_count = 0            # number of corners driven
target_heading = 0          # heading aimed at by the gyro (deg)
last_steer = None           # last command sent to the steering

drift_rate = 0.0            # gyro drift measured at start (deg/s)
drift_t0 = 0                # time of the gyro reset (ms)

hist_l = [0, 0, 0]          # last 3 readings of the left ultrasonic
hist_r = [0, 0, 0]          # last 3 readings of the right ultrasonic


# ==================================================================
#  LOG
#  Two kinds of lines:
#    - "D": measurements of the control loop (one line every 10-20 ms)
#    - "E": events (opening detected, start/end of a corner...)
# ==================================================================

HEADER = ("t_ms;phase;corner;dir;dist_mm;L_mm;R_mm;diff_mm;heading;"
          "target;head_err;steer_cmd;steer_real;spdA;spdB;side;open_cnt;"
          "L_raw;R_raw;gyro_raw")


def set_phase(p):
    """Change the current phase (written in every log line)."""
    global phase
    phase = p


def format_entry(r):
    """Turn a log entry into a CSV text line."""
    if r[0] == "E":
        return "EVT;" + str(r[1]) + ";" + r[2] + ";" + r[3]
    return ";".join(str(x) for x in r[1:])


def event(msg):
    """Record an event in the log."""
    LOG.append(("E", clock.time(), phase, msg))


def record(left, right, diff, h, herr, cmd, side, oc, lraw, rraw):
    """Record one line of measurements in the log."""
    LOG.append(("D", clock.time(), phase, corner_count, direction,
                round(distance_mm()), left, right, diff, h,
                target_heading, herr, round(cmd, 1), steering.angle(),
                motor_a.speed(), motor_b.speed(), side, oc,
                lraw, rraw, gyro.angle()))


def write_log():
    """Write the whole log to LOG_FILE (called at the end)."""
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
    """Limit a value between low and high."""
    return max(low, min(high, value))


def drive_forward(speed=None):
    """Drive forward (default speed: DRIVE_SPEED)."""
    if speed is None:
        speed = DRIVE_SPEED
    motor_a.run(speed)
    motor_b.run(speed)


def stop_drive():
    """Stop the drive motors."""
    motor_a.brake()
    motor_b.brake()


def distance_mm():
    """Distance travelled since the start (average of both motors)."""
    return (abs(motor_a.angle()) + abs(motor_b.angle())) / 2 * MM_PER_DEG


def set_steering(angle, speed=STEERING_SPEED):
    """Turn the wheels to 'angle' (deg, + = left).

    The command is only sent when the target changes, and it does not
    block the program: the motor reaches the position while the loop
    keeps reading the sensors.
    """
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
    """Heading of the car (deg), corrected for the gyro drift.

    An EV3 gyro "drifts": even when still, its angle slowly changes.
    The drift is measured at the start and removed here.
    """
    elapsed = (clock.time() - drift_t0) / 1000
    return round(gyro.angle() - drift_rate * elapsed)


def median3(values):
    """Middle value of 3 (median filter)."""
    return sorted(values)[1]


def read_us():
    """Read both ultrasonic sensors.

    Returns the filtered values (median of the last 3 readings, which
    removes isolated wrong readings) and the raw values.
    """
    lraw = ultra_left.distance()
    rraw = ultra_right.distance()
    hist_l.pop(0)
    hist_l.append(lraw)
    hist_r.pop(0)
    hist_r.append(rraw)
    return median3(hist_l), median3(hist_r), lraw, rraw


def init_us():
    """Fill the ultrasonic history with a current reading.

    Called at the start and after each corner, so that the filter does
    not keep old values measured in the previous corridor.
    """
    l = ultra_left.distance()
    r = ultra_right.distance()
    for i in range(3):
        hist_l[i] = l
        hist_r[i] = r


# ==================================================================
#  CENTERING ON STRAIGHTS
#  Steering = KP x (left - right difference) + KG x (heading error)
#    - the "difference" term brings the car back to the middle
#    - the "heading" term keeps the car parallel to the walls
# ==================================================================

def centering():
    left, right, lraw, rraw = read_us()
    h = heading()
    herr = h - target_heading       # > 0: the car points too far right

    # The walls are used only if both are visible AND the car is
    # roughly straight (otherwise the readings are wrong).
    if left < WALL_MAX and right < WALL_MAX and abs(herr) <= WALL_HEADING_MAX:
        diff = left - right         # > 0: the car is too far right
        if abs(diff) <= CENTER_TOLERANCE:
            diff = 0
    else:
        diff = 0

    cmd = clamp(KP * diff + KG * herr, -MAX_STEERING, MAX_STEERING)

    # Wall safety: has priority over everything else
    if left < WALL_DANGER and left <= right:
        cmd = -MAX_STEERING         # too close to the left wall -> steer right
        diff = "DANGER_L"
    elif right < WALL_DANGER:
        cmd = MAX_STEERING          # too close to the right wall -> steer left
        diff = "DANGER_R"

    set_steering(cmd)

    return left, right, diff, h, herr, cmd, lraw, rraw


def drive_distance(dist, ph, speed=None):
    """Drive 'dist' mm while staying centered, without looking for a
    corner. Used after each corner (lock) and for the final stop."""
    set_phase(ph)
    start = distance_mm()
    event("START " + ph + " " + str(dist) + "mm at dist=" + str(round(start))
          + " heading=" + str(heading()))
    while distance_mm() - start < dist:
        check_stop()
        l, r, d, h, he, c, lr, rr = centering()
        drive_forward(speed)
        record(l, r, d, h, he, c, 0, 0, lr, rr)
        wait(LOOP_MS)
    event("END " + ph + " dist=" + str(round(distance_mm()))
          + " heading=" + str(heading()))


# ==================================================================
#  CORNER
#  Fixed steering (STEERING_TURN) until the gyro is TURN_EARLY_STOP
#  degrees from the target heading, then the wheels are straightened.
# ==================================================================

def do_turn():
    set_phase("TURN")
    h_start = heading()
    event("TURN START heading=" + str(h_start)
          + " target=" + str(target_heading)
          + " dist=" + str(round(distance_mm()))
          + " L=" + str(ultra_left.distance())
          + " R=" + str(ultra_right.distance()))

    cmd = STEERING_TURN * direction     # left (+) or right (-)
    set_steering(cmd, CORNER_STEERING_SPEED)
    drive_forward()

    timer = StopWatch()
    while True:
        check_stop()
        h = heading()

        # Heading almost reached: end of the corner.
        # (h - target) x direction is the angle still to turn,
        # whatever the turning direction.
        if (h - target_heading) * direction <= TURN_EARLY_STOP:
            break

        # Safety: corner too long
        if timer.time() > TURN_TIMEOUT:
            event("TURN TIMEOUT heading=" + str(h))
            break

        # Safety: the gyro turns the wrong way (sensor badly mounted or
        # configured) -> stop at once
        if (h - h_start) * direction > TURN_WRONG_WAY:
            event("GYRO SIGN WRONG h_start=" + str(h_start) + " h=" + str(h))
            raise Exception("GYRO SIGN WRONG")

        l, r, lr, rr = read_us()
        record(l, r, 0, h, h - target_heading, cmd, 0, 0, lr, rr)
        wait(TURN_LOOP_MS)

    set_steering(0, CORNER_STEERING_SPEED)
    event("TURN END heading=" + str(heading())
          + " time=" + str(timer.time()) + "ms"
          + " dist=" + str(round(distance_mm()))
          + " steer_real=" + str(steering.angle()))


# ==================================================================
#  GYRO CALIBRATION
#  Done AFTER the start button is pressed, with the car standing still.
#    1. The drift is measured during GYRO_CAL_TIME.
#    2. If it is too high, the sensor is forced to recalibrate itself
#       (same as unplugging / plugging it back) and measured again.
#    3. If it stays too high, the car starts anyway: the measured
#       drift is removed all the time by heading().
# ==================================================================

def wait_button(buttons):
    """Wait until one of the buttons is pressed, then released."""
    while True:
        pressed = ev3.buttons.pressed()
        for b in buttons:
            if b in pressed:
                while ev3.buttons.pressed():
                    wait(10)
                return b
        wait(10)


def measure_drift():
    """Measure the gyro drift (deg/s), car standing still."""
    wait(1500)              # let the car settle after the button press
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
            event("AUTO RECAL: sensor S1 not found")
            return
        with open(path + "/mode", "w") as f:
            f.write("GYRO-CAL")
        wait(1500)
        with open(path + "/mode", "w") as f:
            f.write("GYRO-ANG")
        wait(1000)
        gyro = GyroSensor(Port.S1, Direction.CLOCKWISE)
        event("AUTO RECAL done (" + path + ")")
    except Exception as e:
        event("AUTO RECAL ERROR " + str(e))


def calibrate_gyro():
    global gyro, drift_rate, drift_t0

    attempt = 0
    auto_tries = 0
    while True:
        attempt += 1
        ev3.screen.clear()
        ev3.screen.print("GYRO CALIBRATION")
        ev3.screen.print("DO NOT TOUCH")

        try:
            drift_rate = measure_drift()
        except Exception as e:
            event("GYRO READ ERROR " + str(e))
            drift_rate = 999

        event("GYRO CAL try=" + str(attempt)
              + " drift_rate=" + str(round(drift_rate, 2)) + " deg/s")

        if abs(drift_rate) <= GYRO_DRIFT_MAX:
            break                   # acceptable drift

        event("WARNING GYRO DRIFT HIGH")

        if auto_tries < GYRO_AUTO_RECAL:
            auto_tries += 1
            ev3.screen.clear()
            ev3.screen.print("RECALIBRATION " + str(auto_tries))
            ev3.screen.print("DO NOT TOUCH")
            event("AUTO RECAL try=" + str(auto_tries))
            hw_recalibrate()
            continue                # measure again

        # No attempt left: start with the drift compensation
        event("START WITH HIGH DRIFT (competition)")
        break

    gyro.reset_angle(0)
    drift_t0 = clock.time()


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

    # ---------- Waiting state (rule 6.12) ----------
    # No measurement and no computation before the start.
    ev3.screen.clear()
    ev3.screen.print("WRO OPEN")
    ev3.screen.print(VERSION)
    ev3.screen.print("")
    ev3.screen.print("READY")
    ev3.screen.print("CENTER = START")
    ev3.speaker.beep()
    wait_button([Button.CENTER])
    event("START BUTTON")

    # ---------- Start: gyro calibration ----------
    calibrate_gyro()

    ev3.screen.clear()
    ev3.screen.print("RUN")

    init_us()

    event("RUN START L=" + str(hist_l[0])
          + " R=" + str(hist_r[0])
          + " heading=" + str(heading())
          + " gyro_raw=" + str(gyro.angle())
          + " steer=" + str(steering.angle()))

    open_count = 0          # consecutive readings showing an opening
    pending_side = 0        # side of the opening being confirmed

    # Measurements for the final stop
    d0 = None               # distance start -> 1st opening
    lap_segments = []       # lengths of the starting side (laps 2 and 3)
    last_turn_end = 0       # distance at the end of the last corner

    set_phase("STRAIGHT")
    drive_forward()

    # ==============================================================
    #  RACE LOOP: one iteration every LOOP_MS
    # ==============================================================
    while corner_count < TOTAL_CORNERS:

        check_stop()

        # 1) Centering in the corridor
        l, r, d, h, he, c, lr, rr = centering()
        drive_forward()

        # 2) Opening detection (end of the inner wall).
        #    RAW ultrasonic values are used (faster reaction).
        if direction == 0:
            # Direction not known yet: the first side that opens
            # (while the other one is closed) gives the direction.
            if lr > OPEN_DISTANCE and rr <= OPEN_DISTANCE:
                side = 1            # opening on the left
            elif rr > OPEN_DISTANCE and lr <= OPEN_DISTANCE:
                side = -1           # opening on the right
            else:
                side = 0
        else:
            # Direction known: only the inner side is watched
            opening = lr if direction == 1 else rr
            side = direction if opening > OPEN_DISTANCE else 0

        # 3) Confirmation: the opening must be seen several times in a
        #    row (avoids false detections caused by a missed echo).
        if side != 0 and side == pending_side:
            open_count += 1
        elif side != 0:
            pending_side = side
            open_count = 1
        else:
            pending_side = 0
            open_count = 0

        record(l, r, d, h, he, c, side, open_count, lr, rr)

        # 4) Opening confirmed: corner
        if open_count >= OPEN_CONFIRM:
            open_dist = distance_mm()
            event("OPENING side=" + str(side) + " L=" + str(lr) + " R=" + str(rr)
                  + " heading=" + str(h) + " dist=" + str(round(open_dist)))
            open_count = 0
            pending_side = 0

            # Measurements for the final stop:
            #   1st opening        -> d0
            #   5th and 9th opening -> length of the starting side
            opening_index = corner_count + 1
            if opening_index == 1:
                d0 = open_dist
                event("START SECTION d0=" + str(round(d0)) + "mm")
            elif opening_index in (5, 9):
                seg = open_dist - last_turn_end
                lap_segments.append(seg)
                event("START SIDE SEGMENT L=" + str(round(seg)) + "mm")

            # First corner: the driving direction is stored
            if direction == 0:
                direction = side
                event("DIRECTION = " + ("LEFT" if direction == 1 else "RIGHT"))

            if PRE_TURN_DISTANCE > 0:
                drive_distance(PRE_TURN_DISTANCE, "PRETURN")

            # Absolute target heading: 90 deg more at each corner
            target_heading -= TURN_ANGLE * direction

            do_turn()
            last_turn_end = distance_mm()
            corner_count += 1
            event("CORNER " + str(corner_count) + "/" + str(TOTAL_CORNERS) + " DONE")

            # Lock: move away from the corner before looking for the
            # next one (otherwise the same opening would be seen again)
            if corner_count < TOTAL_CORNERS:
                drive_distance(LOCK_DISTANCE, "LOCK")

            init_us()
            set_phase("STRAIGHT")

        wait(LOOP_MS)

    # ==============================================================
    #  FINAL STOP AT THE STARTING POSITION
    # ==============================================================
    if d0 is not None and lap_segments:
        L = sum(lap_segments) / len(lap_segments)
        final = L - d0 + FINAL_OFFSET
        event("FINAL AUTO L=" + str(round(L)) + " d0=" + str(round(d0))
              + " offset=" + str(FINAL_OFFSET) + " -> " + str(round(final)) + "mm")
    else:
        final = FINAL_DISTANCE      # measurement failed: fallback distance
        event("FINAL FALLBACK " + str(final) + "mm")

    # Fast part, then the last centimetres slowly (precise stop)
    final = max(0, final)
    fast_part = max(0, final - FINAL_SLOW_DIST)
    slow_part = final - fast_part

    if fast_part > 0:
        drive_distance(fast_part, "FINAL")
    if slow_part > 0:
        drive_distance(slow_part, "FINAL_SLOW", FINAL_SLOW_SPEED)

    # Firm stop, wheels held, steering back to straight
    motor_a.hold()
    motor_b.hold()
    steering.run_target(CORNER_STEERING_SPEED, 0, then=Stop.HOLD, wait=True)
    set_phase("END")
    event("FINISHED dist=" + str(round(distance_mm()))
          + " heading=" + str(heading()))

    ev3.screen.clear()
    ev3.screen.print("FINISHED")
    ev3.speaker.beep()

except Exception as e:
    # Any error (safety, sensor...) is written in the log
    event("ERROR " + str(e))
    sys.print_exception(e)

finally:
    # In every case: motors stopped and log saved
    stop_drive()
    steering.hold()
    event("STOP total_time=" + str(clock.time()) + "ms")
    write_log()