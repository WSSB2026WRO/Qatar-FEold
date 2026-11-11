# Engineering Drawings and Schemes

## Drawing list

We keep this page as an index of the technical diagrams in the Qatar FE repository. The SVG files explain the system, calculations, and mechanisms. They are not dimensioned manufacturing drawings.

| Drawing ID | Title | Type | File |
|---|---|---|---|
| SYS-001 | Autonomous vehicle system architecture | Functional block diagram | `engineering/diagrams/system_architecture.svg` |
| DYN-001 | Vehicle dynamics free-body model | Analytical schematic | `engineering/diagrams/vehicle_dynamics_equations.svg` |
| STR-001 | Ackermann steering geometry | Conceptual mechanism diagram | `engineering/diagrams/steering_ackermann.svg` |
| OBS-001 | Obstacle Challenge state machine | Software flow diagram | `engineering/diagrams/obstacle_state_machine.svg` |
| MEC-001 | Chassis and component layout | Mechanical layout reference | `engineering/diagrams/chassis_component_layout.svg` |
| MEC-002 | Steering linkage | Conceptual mechanism reference | `engineering/diagrams/steering_linkage_reference.svg` |
| ELE-001 | EV3 port allocation | Electrical interface map | `engineering/diagrams/ev3_port_allocation.svg` |
| CAM-001 | Pixy2 camera geometry | Sensor geometry reference | `engineering/diagrams/pixy2_camera_geometry.svg` |

## EV3 connections shown in the diagrams

| EV3 port | Device | Purpose |
|---|---|---|
| A | Medium motor | Drive motor A |
| B | Medium motor | Drive motor B |
| C | Medium motor | Steering motor |
| D | No device assigned | Not used by either challenge program |
| S1 | Gyro sensor | Heading measurement |
| S2 | Ultrasonic sensor | Left-side distance |
| S3 | Ultrasonic sensor | Right-side distance |
| S4 | Pixy2 camera with integrated illumination | I²C pillar detection and camera illumination in the Obstacle Challenge |

The Pixy2 camera and its light are one assembly connected to S4. The illumination is not a separate motor-port device. Port D is not assigned to either challenge program.

## How to read the drawings

Mechanical reference dimensions are shown in millimetres, angular values in degrees, and analytical quantities use labelled symbols. We use the drawing IDs as stable references in the repository.

The diagrams have different purposes:
- Functional diagrams show how the system parts connect.
- Analytical diagrams show the variables used in calculations.
- Mechanism diagrams show the intended geometry.
- Software flow diagrams show the mission-state sequence.

The drawings do not add unrecorded dimensions, material specifications, tolerances, manufacturing approvals, or physical test results.

## Evidence and revisions

Numbers in the drawings use the same evidence labels as the related engineering notes: configured, assumed, calculated, simulated, or measured. The Python source files remain the executable reference for the challenge logic. The SVGs help explain the design and how the parts relate to each other.