# Qatar FE — WRO Future Engineers 2026
## Autonomous Robotics Engineering Portfolio

**Repository:** [WSSB2026WRO/Qatar-FE](https://github.com/WSSB2026WRO/Qatar-FE)  
**WRO team number:** **6038**  
**Branch:** `main`  
> **Evidence convention.** This portfolio separates measured observations, calculated values, simulations, configured software parameters, and provisional assumptions. No physical test is claimed unless a dated source log or measurement record exists.

## 1. Executive overview

We are developing an autonomous vehicle for the World Robot Olympiad (WRO) Future Engineers challenge as Team **6038**. We have written both mission programs in Python with Pybricks MicroPython and in the native LEGO EV3 block environment. This portfolio brings together our program files, EV3 hardware connections, Pixy2 obstacle-detection setup, mechanical and electrical design work, vehicle-dynamics calculations, and software checks.

## 2. Team

| Role | Member | Responsibility |
|---|---|---|
| Lead Programmer | Omar | Embedded software, navigation logic and software maintenance |
| Team Leader / Chief of Team | Eissa | Team coordination, mission integration and project oversight |
| Lead Designer | Mohammed | Mechanical layout, design communication and fabrication planning |

## 3. Dual software implementation

We programmed the robot in two ways: Python/Pybricks MicroPython and LEGO EV3 graphical blocks. By running both approaches on the same EV3 platform, we can compare them and use test results to decide which is more suitable for each mission.

| Challenge | Python implementation | LEGO EV3 block implementation |
|---|---|---|
| Open Challenge | `software/open_challenge/open_challenge.py` | `OpenChallenge.ev3` (native project file supplied with this delivery) |
| Obstacle Challenge | `software/obstacle_challenge/obstacle_challenge.py` | `ObstacleChallenge.ev3` (native project file supplied with this delivery) |

The native `.ev3` projects are the graphical-program counterparts to the Python source files. The comparison is documented in [Dual-Implementation Technical Comparison](../software/implementation_comparison.md).

### 3.1 Comparison criteria

| Dimension | Python / Pybricks MicroPython | LEGO EV3 blocks |
|---|---|---|
| Program representation | Textual source, functions, variables and explicit control flow | Visual blocks representing sequences, loops, conditions, motors and sensors |
| Complex algorithms | Well suited to custom calculations, state machines, filtering and modular logic | Possible through nested blocks and data operations; visual complexity grows with algorithm size |
| Editing and review | Efficient for structured changes, refactoring and text-based version control | Intuitive visual inspection of program flow |
| Build and deployment | Python workflow involves source handling and deployment; the exact timed stage must be named (upload, bytecode preparation or startup) | EV3 environment prepares the graphical project for execution |
| Runtime | MicroPython interpreter and Pybricks APIs | EV3 runtime executing the generated block program |
| Debugging | Source inspection, logs, explicit variables and timestamps | Visual flow inspection and EV3 environment debugging |
| Maintainability | Strong for modular and parameterized software | Strong for clear visual sequences and accessible program structure |

Neither approach is assumed to be faster by definition. The preferred implementation is determined by equivalent measurements on the same robot and mission conditions.

### 3.2 Sub-second compilation and performance comparison

One part of our comparison focuses on timing. We want to measure how long each version takes to prepare and start, as well as how quickly it responds during a run. These timings can be below one second, so we record them in milliseconds where possible. These timing categories are kept distinct:

- **Build/compilation duration:** time required by the relevant programming environment to prepare a runnable program. For Python, the timed operation is identified precisely; upload or bytecode preparation is not mislabeled as native compilation.
- **Startup latency:** time from the start command to the first confirmed program action.
- **Control-cycle duration:** time for an equivalent sensing, decision and actuation cycle.
- **Mission execution time:** time to complete the same defined mission.

Sub-second measurements are expressed in milliseconds or at a stated decimal precision. The timing boundaries and test conditions must be equivalent before the results can support a comparison.

We have included both implementations, but we have not yet added paired timing results from controlled tests. We therefore do not claim that one version is faster. The comparison method is described here; measured results will be added when we have completed the tests.

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

## 5. Obstacle Challenge perception

The Python source maps Pixy2 signature 1 to red and signature 2 to green. Candidate blocks are filtered by signature and image geometry, then confirmed over consecutive observations before triggering avoidance. The configured empirical range model is:

`d = 20100 / (Y - 63)`

where `Y` is the selected vertical image feature in pixels and `d` is estimated range in millimetres. This is a configured model, not a calibrated measurement unless supported by a physical calibration dataset.

## 6. Reference vehicle design case

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

## 7. Engineering drawings

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

We use these SVG files to explain the system and its main design ideas. They are not dimensioned drawings for manufacturing parts.

## 8. Software verification evidence

The repository records a successful GitHub Actions **Python Validation** run:

- Run: [#216 — successful](https://github.com/WSSB2026WRO/Qatar-FE/actions/runs/43079056309)
- Recorded date: 11 November 2026
- Commit checked: `a9530e7c626da46464fa999080a308a67cd770dd`
- Checks: compile both Python challenge programs, execute eight analytical/documentation integrity tests, run the analytical sweep, and upload its CSV artifact.
- Sweep coverage: 30 combinations (five longitudinal acceleration values from 0.2 to 1.0 m/s² and six lateral acceleration values from 0.2 to 1.2 m/s²).

This confirms that the Python files passed the workflow's compilation checks and that the analytical sweep finished. It does **not** show that the programs have run successfully on the EV3, or verify sensor accuracy, steering, obstacle clearance, lap completion, parking, or competition performance. The block projects are native EV3 assets and are not covered by the Python syntax-compilation workflow.

## 9. Evidence and validation scope

We have automated checks for the Python source and results from the analytical model. We have not yet included completed physical test reports, raw EV3 mission logs, or paired timing measurements comparing Python with EV3 blocks. Consequently, physical sensor accuracy, steering repeatability, obstacle clearance, lap performance, parking accuracy, sub-second compilation differences and relative runtime performance are not represented as measured results in this portfolio.

## 10. Engineering design and verification criteria

The repository's engineering criteria cover mechanical alignment and retention, electrical interface integrity and power stability, software initialization and bounded control, mission-state handling, fault response, and traceable validation evidence. These criteria describe the engineering basis used throughout the project.

## 11. Data classification

Numerical values in this portfolio are classified as follows:

- **Measured:** obtained from a physical instrument or recorded robot log, with date and method.
- **Calculated:** derived from stated equations and input values.
- **Simulated:** generated by a computational model with assumptions and limitations.
- **Configured:** a value used by source code or controller settings.
- **Assumed:** a provisional design input awaiting confirmation.

## 12. Repository structure

| Directory | Purpose |
|---|---|
| `Mobility Management/` | Propulsion, steering, odometry and navigation |
| `Obstacle Management/` | Vision-based obstacle detection and avoidance |
| `Power and Sense Management/` | Electrical interfaces, power and sensors |
| `engineering/` | Mechanical, electrical, perception, control and simulation studies |
| `hardware/` | Hardware architecture, calibration and custom printed-part records |
| `software/` | Python challenge programs and comparative implementation analysis |
| Native LEGO EV3 graphical project files | Supplied as original `.ev3` files with this delivery |
| `schemes/` | Drawing register and engineering diagram index |
| `validation/` | Validation framework and test-record format |
| `docs/` | Repository guide, verification evidence and release criteria |
| `t-photos/`, `v-photos/`, `video/` | Technical and vehicle media |

## 13. Source references

Primary references are the repository README, verification evidence, engineering release criteria, reference vehicle design case, analytical simulation, Python challenge source programs, native EV3 block projects, sensor calibration procedure and schemes register.

**Repository:** https://github.com/WSSB2026WRO/Qatar-FE

## Revision control

When we make an important engineering change, we record:

- purpose of the change;
- affected subsystem;
- source version;
- parameter changes;
- test evidence;
- rollback path.

We use this record for software, mechanical, electrical, vision, and validation changes. We also label information clearly as source-derived, configured, assumed, calculated, simulated, or measured. Reviewing code or documentation does not count as a physical test.

For each revision, we list the files we changed and the Git commit containing those changes. If we change hardware or calibration, we also record the robot setup and test conditions so we can repeat the test. We keep the previous working commit or release as a rollback point.
