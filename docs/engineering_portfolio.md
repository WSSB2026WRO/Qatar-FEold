# Qatar FE — WRO Future Engineers 2026
## Autonomous Robotics Engineering Portfolio

**Repository:** [WSSB2026WRO/Qatar-FE](https://github.com/WSSB2026WRO/Qatar-FE)  
**Branch:** `main`  
> **Evidence convention.** This portfolio separates measured observations, calculated values, simulations, configured software parameters, and provisional assumptions. No physical test is claimed unless a dated source log or measurement record exists.

## 1. Executive overview

Qatar FE is a student engineering project developing an autonomous vehicle for the World Robot Olympiad (WRO) Future Engineers challenge. The repository documents two mission programs, an EV3-based hardware interface, a Pixy2 vision subsystem for obstacle handling, mechanical and electrical design references, analytical vehicle-dynamics calculations, and software validation procedures.

## 2. Team

| Role | Member | Responsibility |
|---|---|---|
| Lead Programmer | Omar | Embedded software, navigation logic and software maintenance |
| Team Leader / Chief of Team | Eissa | Team coordination, mission integration and project oversight |
| Lead Designer | Mohammed | Mechanical layout, design communication and fabrication planning |

## 3. Challenge programs

| Program | Mission functions | Implementation |
|---|---|---|
| Open Challenge | Corridor following, wall-based centering, corner detection, heading control, lap tracking and return to the start section | LEGO EV3 with Pybricks MicroPython |
| Obstacle Challenge | Pillar detection and classification, colour-dependent passing, lane repositioning, corner navigation and parking | LEGO EV3 with Pybricks MicroPython and Pixy2 camera over I²C |

### Obstacle Challenge perception

The source maps Pixy2 signature 1 to red and signature 2 to green. Candidate blocks are filtered by signature and image geometry, then confirmed over consecutive observations before triggering avoidance. The configured empirical range model is:

`d = 20100 / (Y - 63)`

where `Y` is the selected vertical image feature in pixels and `d` is estimated range in millimetres. This is a configured model, not a calibrated measurement unless supported by a physical calibration dataset.

## 4. Hardware interface

| Port | Device | Function |
|---|---|---|
| A | Medium motor | Drive motor A |
| B | Medium motor | Drive motor B |
| C | Medium motor | Steering actuator |
| D | No device assigned | Unused by both challenge programs |
| S1 | Gyro sensor | Heading measurement |
| S2 | Ultrasonic sensor | Left-side distance |
| S3 | Ultrasonic sensor | Right-side distance |
| S4 | Pixy2 camera with integrated illumination | I²C vision and camera illumination in Obstacle Challenge |


The Pixy2 camera and its illumination form one assembly connected through S4. The illumination is not a separate motor-port device; port D is unused by both challenge programs.

## 5. Reference vehicle design case

The following values define an illustrative analytical model. They are not verified physical specifications of the competition robot.

| Parameter | Reference value | Classification |
|---|---:|---|
| Total mass | 0.85 kg | Illustrative assumption |
| Overall envelope | 180 × 110 × 210 mm | Illustrative envelope |
| Wheelbase / track | 100 / 100 mm | Design assumptions |
| Wheel diameter / radius | 56 / 28 mm | Software configuration reference / derived |
| Centre-of-gravity height | 45 mm | Illustrative assumption |
| Longitudinal acceleration | 0.80 m/s² | Scenario input |
| Lateral acceleration | 1.20 m/s² | Scenario input |
| Friction coefficient | 0.65 | Illustrative, surface-dependent input |

### Calculated reference results

| Quantity | Method | Result |
|---|---|---:|
| Vehicle weight | 0.85 × 9.81 | 8.3385 N |
| Static load per wheel | 8.3385 ÷ 4; symmetric assumption | 2.0846 N |
| Longitudinal load transfer | m·aₓ·h/L | 0.3060 N |
| Lateral load transfer | m·aᵧ·h/T | 0.4590 N |
| Idealised lateral tip acceleration | g·T/(2h) | 10.90 m/s² |
| Simplified friction-force bound | 0.65 × 8.3385 | 5.420 N |
| Ideal speed at 250°/s | ω·r; 1:1 ratio, no slip | 0.1222 m/s |
| Ideal speed at 300°/s | ω·r; 1:1 ratio, no slip | 0.1466 m/s |

These are analytical estimates. They do not model full tyre dynamics, motor torque limits, compliance, floor variation, transient roll, or wheel slip.

## 6. Engineering drawings

The repository includes system-level or conceptual SVG diagrams for system architecture, vehicle dynamics, Ackermann steering, obstacle state flow, camera geometry, chassis layout and EV3 port allocation.

| Drawing ID | Subject | Status / intended use |
|---|---|---|
| SYS-001 | System architecture | Functional block diagram |
| DYN-001 | Vehicle dynamics model | Analytical schematic |
| STR-001 | Ackermann steering geometry | Conceptual mechanism diagram |
| OBS-001 | Obstacle Challenge state machine | Software flow diagram |
| MEC-001 | Chassis/component layout | Mechanical layout reference |
| MEC-002 | Steering linkage | Mechanism definition |
| ELE-001 | EV3 wiring and port allocation | Electrical interface map |
| CAM-001 | Pixy2 camera geometry | Sensor geometry reference |

The SVG files are system-level or conceptual engineering diagrams. They are not dimensioned manufacturing drawings.

## 7. Software verification evidence

The repository records a successful GitHub Actions **Python Validation** run:

- Run: [#165 — successful](https://github.com/WSSB2026WRO/Qatar-FE/actions/runs/43076407683)
- Recorded date: 11 November 2026
- Commit checked: `e8df0173e62e590f069ea6b69e32df2440a67bd4`
- Checks: compile both challenge programs, execute eight analytical/documentation integrity tests, run the analytical sweep, and upload its CSV artifact.
- Sweep coverage: 30 combinations (five longitudinal acceleration values from 0.2 to 1.0 m/s² and six lateral acceleration values from 0.2 to 1.2 m/s²).

This proves the recorded source files passed the workflow's compilation checks and the analytical sweep completed. It does **not** prove execution on the EV3, sensor accuracy, steering accuracy, obstacle clearance, lap completion, parking accuracy or competition performance.

## 8. Evidence and validation scope

The repository contains automated source validation and analytical model results. It does not contain completed physical test reports or raw EV3 mission logs. Consequently, physical sensor accuracy, steering repeatability, obstacle clearance, lap performance and parking accuracy are not represented as measured results in this portfolio.

## 9. Engineering design and verification criteria

The repository's engineering criteria cover mechanical alignment and retention, electrical interface integrity and power stability, software initialization and bounded control, mission-state handling, fault response, and traceable validation evidence. These criteria describe the engineering basis used throughout the project.

## 10. Data classification

Numerical values in this portfolio are classified as follows:

- **Measured:** obtained from a physical instrument or recorded robot log, with date and method.
- **Calculated:** derived from stated equations and input values.
- **Simulated:** generated by a computational model with assumptions and limitations.
- **Configured:** a value used by source code or controller settings.
- **Assumed:** a provisional design input awaiting confirmation.

## 11. Repository structure

| Directory | Purpose |
|---|---|
| `Mobility Management/` | Propulsion, steering, odometry and navigation |
| `Obstacle Management/` | Vision-based obstacle detection and avoidance |
| `Power and Sense Management/` | Electrical interfaces, power and sensors |
| `engineering/` | Mechanical, electrical, perception, control and simulation studies |
| `hardware/` | Hardware architecture, calibration and custom printed-part records |
| `software/` | Open Challenge and Obstacle Challenge source programs |
| `schemes/` | Drawing register and engineering diagram index |
| `validation/` | Validation plan and test report template |
| `docs/` | Repository guide, verification evidence and release checklist |
| `t-photos/`, `v-photos/`, `video/` | Technical and vehicle media |

## 12. Source references

Primary references are the repository README, verification evidence, engineering release checklist, reference vehicle design case, analytical simulation, challenge source programs, sensor calibration procedure and schemes register.

**Repository:** https://github.com/WSSB2026WRO/Qatar-FE
