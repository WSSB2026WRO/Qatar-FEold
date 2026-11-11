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
| D | Front LED lamp (drawing-register item) | Not configured in current source; physical installation and wiring require confirmation |
| D | Front LED lamp | Camera illumination |
| S1 | Gyro sensor | Heading measurement |
| S2 | Ultrasonic sensor | Left-side distance |
| S3 | Ultrasonic sensor | Right-side distance |
| S4 | Pixy2 camera | I²C pillar detection; address 0x54 |

This is the port allocation documented by the current source and project records. Verify it against the assembled robot after any wiring change.

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

The diagrams are not automatically manufacturing drawings. Fabrication release requires a controlled CAD-derived drawing with units, datums, dimensions, critical tolerances, material, process, revision and review status.

## 7. Software verification evidence

The repository records a successful GitHub Actions **Python Validation** run:

- Run: [#77 — successful](https://github.com/WSSB2026WRO/Qatar-FE/actions/runs/42708351971)
- Recorded date: 9 November 2026
- Commit checked: `cae0fa6eda6c39e48a51990fe60056934c4980a0`
- Checks: compile Open Challenge, Obstacle Challenge and analytical parameter sweep; execute the sweep; upload its CSV artifact.
- Sweep coverage: 30 combinations (five longitudinal acceleration values from 0.2 to 1.0 m/s² and six lateral acceleration values from 0.2 to 1.2 m/s²).

This proves the recorded source files passed the workflow's compilation checks and the analytical sweep completed. It does **not** prove execution on the EV3, sensor accuracy, steering accuracy, obstacle clearance, lap completion, parking accuracy or competition performance.

## 8. Physical validation programme

The following tests are required before physical-performance claims are made.

| Test ID | Objective | Evidence required |
|---|---|---|
| VAL-01 | Gyro stability | Stationary heading log, drift rate and repeat runs |
| VAL-02 | Ultrasonic accuracy | Known target distances, raw readings and absolute error |
| VAL-03 | Drive distance scale | Known travel distance versus encoder-derived distance |
| VAL-04 | Steering response | Commanded versus observed wheel angle, repeatability and backlash |
| VAL-05 | Pillar detection | Red/green detection logs, missed/false detections and measured range |
| VAL-06 | Obstacle passing | Passing-side decision and minimum-clearance observations |
| VAL-07 | Cornering and lap tracking | Corner count, heading trace and recovery notes |
| VAL-08 | Parking repeatability | Final position and orientation across repeated runs |

For every physical run, retain the unedited source log and record date, robot configuration, software revision, conditions, instrument, method, raw observations, acceptance criteria and outcome. A result may be pass, fail or inconclusive.

## 9. Engineering release checklist

- **Mechanical:** wheel alignment, motor mounting, steering-linkage clearance, battery retention, sensor-bracket rigidity, fastener retention and service access.
- **Electrical:** verified port allocation, secure connectors, cable strain relief, operating limits, sensor communication and power stability.
- **Software:** syntax/import integrity, sensor initialisation, calibration, steering sign conventions and limits, bounded actuator commands, mission transitions, timeout/fault handling and logs.
- **Validation:** test objective, hardware/software revision, operating conditions, measurement method, raw observations, acceptance criteria, outcome and corrective action.

## 10. Data classification

Every numerical item must be identified as one of the following:

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
