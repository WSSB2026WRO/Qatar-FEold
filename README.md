# Qatar FE — WRO Future Engineers

<p align="center">
  <strong>Autonomous Robotics Engineering Portfolio</strong><br>
  <em>Mechanical Design · Embedded Control · Perception · Vehicle Dynamics · Additive Manufacturing</em>
</p>

**WRO team number: 6038**

Qatar FE is a student engineering team developing an autonomous vehicle for the **World Robot Olympiad (WRO) Future Engineers** challenge. This repository presents the team's software, mechanical engineering, electronics, perception systems, analytical studies, and technical documentation.

## Team

| Member | Responsibility |
|---|---|
| Omar | Lead Programmer |
| Eissa | Team Leader / Chief of Team |
| Mohammed | Lead Designer |

## Challenge programs and software implementations

The team developed two programming implementations for each challenge: Python using Pybricks MicroPython and graphical LEGO EV3 block programming. This dual implementation supports a direct comparison of development workflow, build/compilation time, startup latency, control-cycle timing, mission execution and reliability.

| Program | Mission | Python source | EV3 block project |
|---|---|---|---|
| Open Challenge | Corridor following, wall-based centering, corner detection, heading control, lap tracking, and return to the start section | [open_challenge.py](software/open_challenge/open_challenge.py) | [OpenChallenge.ev3](software/ev3_blocks/open_challenge/OpenChallenge.ev3) |
| Obstacle Challenge | Visual pillar classification, colour-dependent passing, lane repositioning, corner navigation, and parking | [obstacle_challenge.py](software/obstacle_challenge/obstacle_challenge.py) | [ObstacleChallenge.ev3](software/ev3_blocks/obstacle_challenge/ObstacleChallenge.ev3) |

Both implementations target the LEGO EV3 platform. The Python Obstacle Challenge additionally uses a Pixy2 camera over I²C. The Pixy2's integrated illumination is part of the camera assembly and is connected with the camera through sensor port S4; motor port D is unused.

- [Software directory and program index](software/README.md)
- [Dual-implementation technical comparison](software/implementation_comparison.md)
- [EV3 Blocks — Open Challenge documentation](software/ev3_blocks/open_challenge/README.md)
- [EV3 Blocks — Obstacle Challenge documentation](software/ev3_blocks/obstacle_challenge/README.md)

## Engineering portfolio

- [Consolidated engineering portfolio](docs/engineering_portfolio.md) — project overview, hardware interfaces, software architecture, reference calculations, drawing register, and verification evidence.
- [Repository completion status](docs/repository_completion_status.md)
- [Verification evidence](docs/verification_evidence.md)
- [Automated tests](tests/test_reference_model.py) and [documentation integrity tests](tests/test_documentation_integrity.py)
- [Engineering release criteria](docs/engineering_release_checklist.md)
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
| [software](software/README.md) | Python/Pybricks mission programs, native EV3 block projects, and comparative software documentation |
| [Mobility Management](Mobility%20Management/README.md) | Propulsion, steering, odometry, and navigation |
| [Obstacle Management](Obstacle%20Management/README.md) | Vision-based obstacle detection and avoidance |
| [Power and Sense Management](Power%20and%20Sense%20Management/README.md) | Electrical interfaces, power, and sensors |
| [src](src/README.md) | Software source index |
| [t-photos](t-photos/README.md) | Team photographs |
| [v-photos](v-photos/README.md) | Vehicle photographs |
| [video](video/README.md) | Demonstration-video index; no videos currently committed |

## Verification

- [Verification and validation framework](validation/README.md)
- [Test report format](validation/test_report_template.md)
- GitHub Actions compiles both Python challenge programs, runs analytical/documentation integrity tests, executes the analytical parameter sweep, and uploads its CSV output.

## Engineering data conventions

Software settings, theoretical design inputs, calculated outputs, simulations, and physical observations are treated as separate engineering data classes. Numerical examples are accompanied by their governing assumptions and equations. Physical performance claims are based on recorded test evidence.

A key engineering characteristic of Team 6038 is its comparative approach to software: Python and EV3 block versions are maintained to evaluate their relative performance. Build/compilation duration, startup latency and control-cycle timing are treated as measurable quantities at sub-second resolution. Numerical performance conclusions are reported only when supported by paired measurements.
