# Qatar-FE — Engineering Drawing Set

**WRO Future Engineers · Team 6038 · Revision A**

This drawing set presents the robot's system architecture, vehicle dynamics, steering geometry, mission logic, mechanical packaging, electrical interfaces and camera geometry. The diagrams are intended for engineering communication and design review; they are not fabrication drawings.

## Drawing register

| Drawing | Subject | Primary use |
|---|---|---|
| [SYS-001 — Autonomous vehicle system architecture](SYS-001_autonomous_vehicle_architecture.svg) | Sensor-to-controller-to-actuator signal flow | System overview |
| [DYN-001 — Vehicle dynamics](DYN-001_vehicle_dynamics.svg) | Longitudinal forces and cornering model | Dynamics analysis |
| [STR-001 — Ackermann steering geometry](STR-001_ackermann_steering.svg) | Inner/outer wheel angles and turning centre | Steering analysis |
| [OBS-001 — Obstacle Challenge state machine](OBS-001_obstacle_state_machine.svg) | Mission states and safety stop | Software design |
| [MEC-001 — Chassis layout](MEC-001_chassis_layout.svg) | Indicative top and side component placement | Mechanical design |
| [MEC-002 — Steering linkage](MEC-002_steering_linkage.svg) | Motor C, rack and tie-rod arrangement | Mechanism definition |
| [ELE-001 — EV3 wiring](ELE-001_ev3_wiring.svg) | Motor and sensor port allocation | Electrical integration |
| [CAM-001 — Pixy2 camera geometry](CAM-001_pixy2_camera_geometry.svg) | Field of view and image-coordinate model | Vision calibration |

## Drawing previews

### SYS-001 — System architecture
![SYS-001 system architecture](SYS-001_autonomous_vehicle_architecture.svg)

### DYN-001 — Vehicle dynamics
![DYN-001 vehicle dynamics](DYN-001_vehicle_dynamics.svg)

### STR-001 — Ackermann steering
![STR-001 Ackermann steering geometry](STR-001_ackermann_steering.svg)

### OBS-001 — Obstacle Challenge state machine
![OBS-001 obstacle state machine](OBS-001_obstacle_state_machine.svg)

### MEC-001 — Chassis layout
![MEC-001 chassis layout](MEC-001_chassis_layout.svg)

### MEC-002 — Steering linkage
![MEC-002 steering linkage](MEC-002_steering_linkage.svg)

### ELE-001 — EV3 wiring
![ELE-001 EV3 wiring](ELE-001_ev3_wiring.svg)

### CAM-001 — Pixy2 camera geometry
![CAM-001 Pixy2 camera geometry](CAM-001_pixy2_camera_geometry.svg)

## Revision control

Every significant change to a drawing or its associated engineering definition should include:

- purpose of the change;
- affected subsystem;
- source version;
- parameter changes;
- test evidence;
- rollback path.

Record the revision in the drawing title block and update the drawing register. Where a change affects physical dimensions, wiring, sensor placement, calibration or software interfaces, identify the affected drawing IDs and supporting source files. Do not describe analytical or illustrative values as measured test evidence.

### Revision history

| Revision | Date | Drawing / subsystem | Change purpose | Source version | Parameter changes | Test evidence | Rollback path |
|---|---|---|---|---|---|---|---|
| A | 2026-11-11 | Initial drawing set | Initial engineering reference diagrams | Repository source snapshot | No physical dimensions asserted; confirm on robot | Drawing files checked into GitHub; physical verification pending | Revert the drawing-set commit or restore the previous SVG revision |

## Engineering control notes

- Dimensions marked as measured or requiring measurement must be confirmed on the assembled robot.
- Camera calibration depends on the actual Pixy2 mounting height, tilt and image geometry.
- Steering ratio, backlash and mechanical stops must be measured before setting final software limits.
- Verify sensor and motor ports against the physical wiring before each competition configuration.
- Update the revision and drawing register when the robot hardware or software interfaces change.

**Document status:** Engineering reference diagrams. Confirm dimensions, calibration constants and hardware details against the current robot before using them for fabrication, inspection or performance claims.
