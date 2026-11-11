# Qatar FE — WRO Future Engineers

<p align="center">
  <strong>Autonomous Robotics Engineering Portfolio</strong><br>
  <em>Mechanical Design · Embedded Control · Perception · Vehicle Dynamics · Additive Manufacturing</em>
</p>

Qatar FE is a student engineering team developing an autonomous vehicle for the **World Robot Olympiad (WRO) Future Engineers** challenge. This repository presents the team's software, mechanical engineering, electronics, perception systems, analytical studies, and technical documentation.

## Team

| Member | Responsibility |
|---|---|
| Omar | Lead Programmer |
| Eissa | Team Leader / Chief of Team |
| Mohammed | Lead Designer |

## Challenge programs

| Program | Mission | Documentation |
|---|---|---|
| Open Challenge | Corridor following, wall-based centering, corner detection, heading control, lap tracking, and return to the start section | [Program and technical notes](software/open_challenge/README.md) |
| Obstacle Challenge | Visual pillar classification, colour-dependent passing, lane repositioning, corner navigation, and parking | [Program and technical notes](software/obstacle_challenge/README.md) |

Both programs target LEGO EV3 with Pybricks MicroPython. The Obstacle Challenge program additionally uses a Pixy2 camera over I²C.

## Engineering portfolio

- [Consolidated engineering portfolio](docs/engineering_portfolio.md) — project overview, hardware interfaces, software architecture, reference calculations, drawing register, verification evidence, and physical validation plan.
- [Repository completion status and remaining release gates](docs/repository_completion_status.md)
- [Verification evidence](docs/verification_evidence.md)
- [Automated tests](tests/test_reference_model.py) and [documentation integrity tests](tests/test_documentation_integrity.py)
- [Engineering release checklist](docs/engineering_release_checklist.md)
- [Repository guide](docs/repository_guide.md)

## Engineering library

- [Mechanical design — chassis and packaging](engineering/mechanical_design/chassis_and_packaging.md)
- [Mass distribution and vehicle dynamics](engineering/mechanical_design/mass_distribution_and_vehicle_dynamics.md)
- [Steering geometry](engineering/mechanical_design/steering_geometry.md)
- [Electrical architecture](engineering/electronics/electrical_architecture.md)
- [Control system design](engineering/software/control_system_design.md)
- [Pixy2 calibration and geometry](engineering/perception/pixy2_calibration_and_geometry.md)
- [Reliability and FMEA](engineering/reliability/risk_assessment.md)
- [Reference vehicle design case](engineering/design_basis/reference_vehicle_design_case.md)
- [Analytical simulation](engineering/simulation/README.md)

## Technical diagrams

- [System architecture](engineering/diagrams/system_architecture.svg)
- [Vehicle dynamics model](engineering/diagrams/vehicle_dynamics_equations.svg)
- [Ackermann steering geometry](engineering/diagrams/steering_ackermann.svg)
- [Obstacle Challenge state machine](engineering/diagrams/obstacle_state_machine.svg)

## Hardware and fabrication

- [Hardware architecture](hardware/README.md)
- [Custom 3D-printed components](hardware/custom_3d_printed_parts/README.md)
- [Additive manufacturing guidelines](engineering/mechanical_design/3d_printing_design_guidelines.md)
- [Engineering schemes](schemes/README.md)

## Project directories

| Directory | Purpose |
|---|---|
| [Mobility Management](Mobility%20Management/README.md) | Propulsion, steering, odometry, and navigation |
| [Obstacle Management](Obstacle%20Management/README.md) | Vision-based obstacle detection and avoidance |
| [Power and Sense Management](Power%20and%20Sense%20Management/README.md) | Electrical interfaces, power, and sensors |
| [src](src/README.md) | Software source index |

## Verification

- [Verification and validation plan](validation/README.md)
- [Test report format](validation/test_report_template.md)
- GitHub Actions checks Python syntax and executes the analytical parameter-sweep script on repository updates.

## Engineering data conventions

Software settings, theoretical design inputs, calculated outputs, simulations, and physical observations are treated as separate engineering data classes. Numerical examples are accompanied by their governing assumptions and equations. Physical performance claims are based on recorded test evidence.

The two challenge source programs are maintained as separate reference implementations. Experimental revisions should be versioned independently.
