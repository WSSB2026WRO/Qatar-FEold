# Schemes and Engineering Drawings

This directory is the drawing index for the Qatar FE vehicle.

## System diagrams

- [System architecture](../engineering/diagrams/system_architecture.svg)
- [Vehicle dynamics free-body model](../engineering/diagrams/vehicle_dynamics_equations.svg)
- [Conceptual Ackermann steering geometry](../engineering/diagrams/steering_ackermann.svg)
- [Obstacle Challenge state machine](../engineering/diagrams/obstacle_state_machine.svg)

## Drawing register

| Drawing ID | Title | Status |
|---|---|---|
| SYS-001 | Autonomous vehicle system architecture | Published schematic |
| DYN-001 | Vehicle dynamics conceptual model | Published schematic |
| STR-001 | Ackermann steering geometry | Published conceptual drawing |
| OBS-001 | Obstacle Challenge state machine | Published software diagram |
| MEC-001 | Chassis top-view and mounting layout | Required for measured CAD release |
| MEC-002 | Steering linkage dimensioned drawing | Required for measured CAD release |
| ELE-001 | EV3 wiring and port layout | Port map documented; physical wiring drawing pending |
| CAM-001 | Pixy2 camera mounting and field of view | Mounting dimensions pending |

## Drawing conventions

Every released drawing should include:
- drawing number and title;
- revision identifier;
- units and scale;
- projection method where applicable;
- datum references;
- dimensions and tolerances;
- material and manufacturing notes;
- authoring date and review status.

## Release rule

Conceptual diagrams must be labelled as schematic. Dimensioned manufacturing drawings require measurements or CAD source geometry. Do not use schematic diagrams as fabrication drawings.
