# Schemes and Engineering Drawings

This directory is the drawing index for the Qatar FE vehicle and its control system.

## System diagrams

- [System architecture](../engineering/diagrams/system_architecture.svg)
- [Vehicle dynamics model](../engineering/diagrams/vehicle_dynamics_equations.svg)
- [Ackermann steering geometry](../engineering/diagrams/steering_ackermann.svg)
- [Obstacle Challenge state machine](../engineering/diagrams/obstacle_state_machine.svg)

## Drawing register

| Drawing ID | Title | Drawing class |
|---|---|---|
| SYS-001 | Autonomous vehicle system architecture | Functional block diagram |
| DYN-001 | Vehicle dynamics free-body model | Analytical schematic |
| STR-001 | Ackermann steering geometry | Conceptual mechanism diagram |
| OBS-001 | Obstacle Challenge state machine | Software flow diagram |
| MEC-001 | Chassis and component layout | Mechanical layout reference |
| MEC-002 | Steering linkage | Mechanism definition |
| ELE-001 | EV3 wiring and port allocation | Electrical interface map |
| CAM-001 | Pixy2 camera geometry | Sensor geometry reference |

## Drawing conventions

Each manufacturing drawing should define its drawing number, revision, units, scale, datum references, dimensions, tolerances, material, and manufacturing notes. Functional and conceptual diagrams are not fabrication drawings.

## Release criteria

Use dimensioned CAD-derived drawings for fabrication. Use verified wiring inspection for electrical release. Use the supplied SVG diagrams for system-level communication and design review.
