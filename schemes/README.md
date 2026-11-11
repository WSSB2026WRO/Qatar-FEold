# Engineering Drawings and Schemes

## Drawing register

This index identifies the technical diagrams included in the Qatar FE engineering repository. SVGs are functional, analytical, or conceptual illustrations. They communicate the documented system design and are not represented as dimensioned manufacturing drawings.

| Drawing ID | Title | Class | Repository file |
|---|---|---|---|
| SYS-001 | Autonomous vehicle system architecture | Functional block diagram | `engineering/diagrams/system_architecture.svg` |
| DYN-001 | Vehicle dynamics free-body model | Analytical schematic | `engineering/diagrams/vehicle_dynamics_equations.svg` |
| STR-001 | Ackermann steering geometry | Conceptual mechanism diagram | `engineering/diagrams/steering_ackermann.svg` |
| OBS-001 | Obstacle Challenge state machine | Software flow diagram | `engineering/diagrams/obstacle_state_machine.svg` |
| MEC-001 | Chassis and component layout | Mechanical layout reference | `engineering/diagrams/chassis_component_layout.svg` |
| MEC-002 | Steering linkage | Conceptual mechanism reference | `engineering/diagrams/steering_linkage_reference.svg` |
| ELE-001 | EV3 port allocation | Electrical interface map | `engineering/diagrams/ev3_port_allocation.svg` |
| CAM-001 | Pixy2 camera geometry | Sensor geometry reference | `engineering/diagrams/pixy2_camera_geometry.svg` |

## EV3 interface allocation

| EV3 port | Device | Function |
|---|---|---|
| A | Medium motor | Drive motor A |
| B | Medium motor | Drive motor B |
| C | Medium motor | Steering actuator |
| D | No device assigned | Unused by both challenge programs |
| S1 | Gyro sensor | Heading measurement |
| S2 | Ultrasonic sensor | Left-side distance measurement |
| S3 | Ultrasonic sensor | Right-side distance measurement |
| S4 | Pixy2 camera with integrated illumination | I²C pillar detection and camera illumination in Obstacle Challenge |

The Pixy2 camera and its illumination are one camera assembly connected through sensor port S4. The illumination is not a separate EV3 motor-port device. Port D has no assigned device in either challenge program.

## Drawing conventions

The drawing set uses millimetres for mechanical reference dimensions, degrees for angular values, and explicit symbols for analytical quantities. Drawing identifiers are stable references within the repository. Functional diagrams describe system relationships; analytical diagrams describe model variables; conceptual mechanism diagrams illustrate intended geometry; software flow diagrams describe mission-state logic.

The diagrams contain reference geometry and system relationships. They do not assert unrecorded dimensions, material specifications, tolerances, manufacturing approvals, or physical test results.

## Evidence and revision context

Numerical values shown in diagrams retain the same evidence classification as the associated engineering documents: configured, assumed, calculated, simulated, or measured. The source Python programs remain the executable reference for challenge logic. The SVG files are explanatory engineering records.
