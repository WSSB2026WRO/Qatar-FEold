# Autonomous Control System Design

## 1. What the control system needs to do

Our control system reads the sensors, estimates where the robot is, chooses what it should do next, and sends commands to the drive and steering motors. It also needs to respect the corridor, obstacle, and actuator limits.

We split the design into these parts:

1. Sensor readings.
2. Filtering and checks for unusual values.
3. Estimating the robot's state.
4. Managing the mission states.
5. Choosing a path or lane target.
6. Controlling heading and steering.
7. Sending commands to the motors.
8. Recording events and handling faults.

## 2. State estimate

A simple planar state can be written as:

[
\mathbf{x}=[s, y, \psi, v, \delta, q]^T
]

where:
- (s): distance along the track.
- (y): sideways distance from the corridor centre.
- (psi): heading compared with the corridor direction.
- (v): forward speed.
- (delta): estimated steering angle.
- (q): current mission state.

## 3. What each sensor tells us

- **Gyro:** change in heading and whether a turn is complete.
- **Drive encoders:** an estimate of distance travelled.
- **Ultrasonic sensors:** distance to the corridor walls and evidence of wall openings.
- **Pixy2:** pillar signature and image position in the Obstacle Challenge.

We treat sensor readings as information that can sometimes be wrong. We check their range, continuity, and whether they make sense for the current mission state.

## 4. Two-step steering control idea

The lateral controller can calculate a heading target from the sideways error:

[
\psi_{ref}=\operatorname{sat}(K_y e_y, -\psi_{max}, +\psi_{max})
]

The heading controller can then calculate the steering command:

[
\delta_{cmd}=\operatorname{sat}(K_\psi(\psi-\psi_{ref}), -\delta_{max}, +\delta_{max})
]

We define the steering direction so that the command reduces the measured error. Derivative or rate terms need care because sensor noise and loop timing can affect them.

## 5. Mission states

### Open Challenge

- INITIALIZE
- WAIT_FOR_START
- CALIBRATE
- FOLLOW_CORRIDOR
- IDENTIFY_DIRECTION
- APPROACH_CORNER
- TURN
- POST_TURN_LOCKOUT
- FINAL_APPROACH
- STOP_AND_LOG
- FAULT

### Obstacle Challenge

- INITIALIZE
- WAIT_FOR_START
- CALIBRATE
- UNPARK
- FOLLOW_AND_PERCEIVE
- AVOID_PILLAR
- CLEAR_PILLAR
- APPROACH_CORNER
- TURN
- PARK_APPROACH
- PARK_ALIGN
- PARK_EXECUTE
- STOP_AND_LOG
- FAULT

## 6. Safety supervisor

Safety checks should take priority over normal driving. The supervisor should monitor:
- Overall mission timeout.
- Sensor communication errors.
- Distance readings that do not make sense.
- Gyro angle outside the expected turn range.
- Motor encoder progress.
- Steering motor limits.
- Distance from the corridor boundaries.

If a critical fault occurs, the supervisor should stop the drive motors and put the steering mechanism in a defined safe condition.

## 7. Loop timing

The control loop has to read sensors, filter the values, calculate the next command, write logs, and send motor commands. Camera communication is slower than the steering loop, so vision updates can be handled separately. The controller should keep the latest valid camera detection with its timestamp.

## 8. Ways to check the software design

We can check the control system with:
- Unit tests for geometry calculations.
- Test examples for steering sign conventions.
- Replaying saved sensor readings.
- Boundary tests for limits and thresholds.
- Tests of mission-state changes.
- Fault tests with missing sensor readings.
- Regression comparisons with the preserved program source.