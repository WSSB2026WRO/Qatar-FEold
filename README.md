# Qatar FE — WRO Future Engineers

<p align="center">
  <strong>Autonomous Robotics Engineering Portfolio</strong><br>
  <em>Mechanical Design · Embedded Control · Perception · Vehicle Dynamics · Additive Manufacturing</em>
</p>

Qatar FE is a student engineering team developing an autonomous vehicle for the **World Robot Olympiad (WRO) Future Engineers** challenge. This repository is the team's technical record for the Open Challenge and Obstacle Challenge programs, hardware architecture, mechanical design studies, analytical models, and verification planning.

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

The supplied source programs target LEGO EV3 with Pybricks MicroPython. The Obstacle Challenge program also uses a Pixy2 camera over I²C.

## Engineering library

- [Mechanical design — chassis and packaging](engineering/mechanical_design/chassis_and_packaging.md)
- [Mass distribution and vehicle dynamics](engineering/mechanical_design/mass_distribution_and_vehicle_dynamics.md)
- [Steering geometry](engineering/mechanical_design/steering_geometry.md)
- [Electrical architecture](engineering/electronics/electrical_architecture.md)
- [Control system design](engineering/software/control_system_design.md)
- [Pixy2 calibration and geometry](engineering/perception/pixy2_calibration_and_geometry.md)
- [Reliability and FMEA](engineering/reliability/risk_assessment.md)
- [Reference design case and calculations](engineering/design_basis/reference_vehicle_design_case.md)
- [Analytical simulation and parameter sweeps](engineering/simulation/README.md)

## Technical diagrams

- [System architecture](engineering/diagrams/system_architecture.svg)
- [Vehicle dynamics model](engineering/diagrams/vehicle_dynamics_equations.svg)
- [Ackermann steering geometry](engineering/diagrams/steering_ackermann.svg)
- [Obstacle Challenge state machine](engineering/diagrams/obstacle_state_machine.svg)

## Hardware

The documented EV3 port map is available in [Hardware Architecture](hardware/README.md). Custom EV3-compatible printed parts are catalogued in [Custom 3D-Printed Components](hardware/custom_3d_printed_parts/README.md).

## Verification

- [Verification and validation plan](validation/README.md)
- [Engineering release checklist](docs/engineering_release_checklist.md)
- [Repository guide and evidence classification](docs/repository_guide.md)

A GitHub Actions workflow performs Python syntax validation and runs the analytical parameter sweep when changes are pushed to `main` or submitted through a pull request.

## Engineering evidence and design assumptions

This repository distinguishes source-derived information, configured software parameters, conceptual design assumptions, calculated values, simulated outputs, measured data, and validated test results. The reference vehicle design case is an illustrative analytical model; it is not a claim that those assumed dimensions or calculated scenarios have been measured on the physical robot.

The source programs are preserved as supplied reference versions. Any future experimental variant should be maintained separately with a clear revision history.

## Project status

The repository contains the two supplied challenge programs and a growing engineering documentation set. Physical test records, confirmed CAD dimensions, native CAD source files, approved team photographs, and final manufacturing release data should be added when available.

---

**Qatar FE — WRO Future Engineers**
