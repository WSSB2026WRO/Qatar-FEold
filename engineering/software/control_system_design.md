# Autonomous Control System Design

## 1. Control objectives

The control system must estimate vehicle state, select a navigation target, and command propulsion and steering while respecting the physical corridor and obstacle constraints.

The architecture is divided into:
1. sensing;
2. filtering and plausibility checks;
3. state estimation;
4. mission-state management;
5. path and lane target generation;
6. heading and steering control;
7. actuator execution;
8. logging and fault handling.

## 2. State vector

A compact planar state estimate may be represented as:

[
\mathbf{x}=[s, y, \psi, v, \delta, q]^T
]

where:
- (s): longitudinal track coordinate;
- (y): lateral displacement from corridor centre;
- (psi): heading relative to corridor axis;
- (v): forward speed;
- (delta): steering angle estimate;
- (q): discrete mission state.

## 3. Sensor roles

- Gyro: short-term heading change and turn completion.
- Drive encoders: travelled distance estimate.
- Ultrasonic sensors: corridor-relative lateral position and wall-opening evidence.
- Pixy2: pillar signature and image location in Obstacle Challenge.

No single sensor should be treated as infallible. Measurements should be checked for range, continuity, and consistency with the current mission state.

## 4. Cascaded control concept

The lateral controller produces a desired heading from lateral error:

[
\psi_{ref}=\operatorname{sat}(K_y e_y, -\psi_{max}, +\psi_{max})
]

The heading controller produces a steering command:

[
\delta_{cmd}=\operatorname{sat}(K_\psi(\psi-\psi_{ref}), -\delta_{max}, +\delta_{max})
]

The sign convention must be calibrated so that the command reduces the measured error. A derivative or rate term may be introduced only after noise and sampling behaviour are understood.

## 5. Mission state machine

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

The safety supervisor should have priority over nominal control. It monitors:
- global timeout;
- sensor communication errors;
- implausible range values;
- gyro angle beyond expected turn limits;
- motor encoder progress;
- steering actuator limits;
- proximity to corridor boundaries.

On a critical fault, the supervisor stops propulsion and places the steering mechanism in a defined safe condition.

## 7. Sampling and timing

The control loop should have a measured execution-time budget. Sensor acquisition, filtering, control calculations, logging, and actuator commands must be profiled together. If camera communication increases execution time, the vision update can be scheduled separately from the fast steering loop, while retaining a timestamped latest valid detection.

## 8. Software verification

- unit tests for geometric transformations;
- test vectors for sign conventions;
- replay of logged sensor traces;
- boundary tests for saturations and thresholds;
- state-transition tests;
- fault-injection tests for missing sensors;
- regression comparison against the preserved source program.
