# Qatar FE — WRO Future Engineers 2026
## Our Autonomous Robotics Engineering Portfolio

**Repository:** [WSSB2026WRO/Qatar-FE](https://github.com/WSSB2026WRO/Qatar-FE)  
**WRO team number:** **6038**  
**Branch:** `main`

> **How we label evidence:** We keep measured observations, calculations, simulations, software settings, and assumptions separate. We only call something a physical test result when there is a dated measurement record or original log to support it.

## 1. Project overview

We are Team **6038**, and we are developing an autonomous vehicle for the World Robot Olympiad (WRO) Future Engineers challenge. We have written the two mission programs in Python using Pybricks MicroPython and in the native LEGO EV3 block environment.

This portfolio brings together our programs, EV3 connections, Pixy2 obstacle-detection setup, mechanical and electrical notes, vehicle-dynamics calculations, drawings, and software checks.

## 2. Our team

| Role | Member | Main responsibility |
|---|---|---|
| Lead Programmer | Omar | Embedded software, navigation logic, and software maintenance |
| Team Leader / Chief of Team | Eissa | Team coordination and mission integration |
| Lead Designer | Mohammed | Mechanical layout, design communication, and fabrication planning |

## 3. Two software versions

We programmed the robot in two ways: Python/Pybricks MicroPython and LEGO EV3 graphical blocks. Using the same EV3 platform lets us compare the two approaches and use test results to decide which is more suitable for each mission.

| Challenge | Python program | LEGO EV3 block project |
|---|---|---|
| Open Challenge | `software/open_challenge/open_challenge.py` | `OpenChallenge.ev3` (native project file included) |
| Obstacle Challenge | `software/obstacle_challenge/obstacle_challenge.py` | `ObstacleChallenge.ev3` (native project file included) |

The native `.ev3` projects are the graphical versions of the Python programs. We explain the comparison in [Dual-Implementation Technical Comparison](../software/implementation_comparison.md).

### 3.1 What we compare

| Topic | Python / Pybricks MicroPython | LEGO EV3 blocks |
|---|---|---|
| Program format | Text source with functions, variables, and control flow | Visual blocks for sequences, loops, conditions, motors, and sensors |
| Complex algorithms | Flexible for calculations, state machines, filtering, and modular logic | Possible with nested blocks and data operations; large programs can become visually complex |
| Editing and review | Useful for structured changes and text-based version control | Easy to inspect the program flow visually |
| Build and deployment | Python source handling and deployment; we must name the exact timed step | EV3 software prepares the graphical project for execution |
| Runtime | MicroPython interpreter and Pybricks APIs | EV3 runtime executing the block program |
| Debugging | Source inspection, logs, variables, and timestamps | Visual inspection and EV3 debugging tools |
| Maintenance | Useful for modular programs and shared parameters | Useful for clear visual sequences and accessible program structure |

We do not assume one approach is faster. We need comparable measurements on the same robot and under the same mission conditions.

### 3.2 Measuring times below one second

We want to understand how long each program takes to prepare and start, and how quickly it responds while the robot is moving. Some of these times may be shorter than one second, so we record them in milliseconds where possible.

We keep four measurements separate:

- **Build or preparation time:** time needed by the programming environment to prepare a runnable program. For Python, we must say whether we measured upload, bytecode preparation, or deployment. We should not call it native compilation if that is not what happened.
- **Startup latency:** time from the start command to the first confirmed program action.
- **Control-cycle duration:** time for the same sensor, decision, and motor-command cycle.
- **Mission time:** time to complete the same defined task.

For a fair comparison, we need equivalent timing start and end points and repeated trials. We have included both implementations and described the method, but we do not yet have paired timing results from controlled tests. We therefore do not claim that one version is faster.

## 4. Hardware connections

| Port | Device | Purpose |
|---|---|---|
| A | Medium motor | Drive motor A |
| B | Medium motor | Drive motor B |
| C | Medium motor | Steering motor |
| D | No device assigned | Not used by either challenge program |
| S1 | Gyro sensor | Heading measurement |
| S2 | Ultrasonic sensor | Left-side distance |
| S3 | Ultrasonic sensor | Right-side distance |
| S4 | Pixy2 camera with integrated illumination | I²C camera and illumination in the Obstacle Challenge |

The Pixy2 camera and its light are one assembly connected through S4. The light is not a separate motor-port device, and port D is unused by both challenge programs.

## 5. Obstacle detection

In our Python source, Pixy2 signature 1 is assigned to red and signature 2 to green. The program filters candidate blocks by signature and image shape, then checks repeated observations before starting an avoidance action.

The configured image-to-range model is:

`d = 20100 / (Y - 63)`

Here, `Y` is the selected vertical image coordinate in pixels and `d` is the estimated range in millimetres. This is a configured empirical model. It is not a measured calibration result unless we support it with physical camera observations.

## 6. Reference vehicle calculations

The values below are for an illustrative model. They are not confirmed physical specifications of our competition robot.

| Parameter | Reference value | Type |
|---|---:|---|
| Total mass | 0.85 kg | Illustrative assumption |
| Overall size | 180 × 110 × 210 mm | Illustrative envelope |
| Wheelbase / track | 100 / 100 mm | Design assumptions |
| Wheel diameter / radius | 56 / 28 mm | Software reference / derived value |
| Centre-of-gravity height | 45 mm | Illustrative assumption |
| Longitudinal acceleration | 0.80 m/s² | Scenario input |
| Lateral acceleration | 1.20 m/s² | Scenario input |
| Friction coefficient | 0.65 | Illustrative surface-dependent input |

### Calculated reference values

| Quantity | Calculation | Result |
|---|---|---:|
| Vehicle weight | 0.85 × 9.81 | 8.3385 N |
| Static load per wheel | 8.3385 ÷ 4, equal-load assumption | 2.0846 N |
| Longitudinal load transfer | m·aₓ·h/L | 0.3060 N |
| Lateral load transfer | m·aᵧ·h/T | 0.4590 N |
| Idealised lateral tip acceleration | g·T/(2h) | 10.90 m/s² |
| Simplified friction-force bound | 0.65 × 8.3385 | 5.420 N |
| Ideal speed at 250°/s | ω·r; 1:1 ratio, no slip | 0.1222 m/s |
| Ideal speed at 300°/s | ω·r; 1:1 ratio, no slip | 0.1466 m/s |

These are estimates from equations. The model does not include full tyre behaviour, motor torque limits, frame flexibility, floor changes, transient roll, or wheel slip.

## 7. Engineering drawings

We have eight SVG drawings to explain the robot's system and main design ideas.

| Drawing | What it shows |
|---|---|
| SYS-001 | System architecture |
| DYN-001 | Vehicle dynamics model |
| STR-001 | Ackermann steering geometry |
| OBS-001 | Obstacle Challenge state machine |
| MEC-001 | Chassis and component layout |
| MEC-002 | Steering linkage |
| ELE-001 | EV3 wiring and port allocation |
| CAM-001 | Pixy2 camera geometry |

We use these files as engineering references, not as dimensioned manufacturing drawings.

## 8. Automated software checks

The repository records a successful GitHub Actions **Python Validation** run:

- Run: [#216 — successful](https://github.com/WSSB2026WRO/Qatar-FE/actions/runs/43079056309)
- Date recorded: 11 November 2026.
- Commit checked: `a9530e7c626da46464fa999080a308a67cd770dd`.
- Checks: compile both Python challenge programs, run eight analytical and documentation-integrity tests, run the analytical parameter sweep, and upload its CSV file.
- Sweep: 30 combinations using five longitudinal acceleration values from 0.2 to 1.0 m/s² and six lateral acceleration values from 0.2 to 1.2 m/s².

This shows that the Python files passed the workflow's compilation checks and that the tests and analytical sweep completed. It does not show that the programs ran successfully on the EV3, or that the sensors, steering, obstacle passing, lap completion, or parking have been physically validated. The Python workflow also does not test the native EV3 block projects.

## 9. What physical evidence is still missing

We have automated software checks and analytical results in the repository. We have not yet included completed physical test reports, raw EV3 mission logs, or paired timing measurements for Python and EV3 blocks.

Because of this, we do not present physical sensor accuracy, steering repeatability, obstacle clearance, lap performance, parking accuracy, sub-second build-time differences, or relative runtime performance as measured results.

## 10. What we check during design reviews

Our engineering notes cover wheel alignment and part retention, electrical connections and power stability, software initialization and bounded motor commands, mission-state changes, fault handling, and test evidence. These are the points we use when reviewing the project.

## 11. How we label project data

- **Measured:** taken from a physical instrument or robot log, with date and method.
- **Calculated:** worked out from stated equations and inputs.
- **Simulated:** generated by a computational model.
- **Configured:** set in source code or controller settings.
- **Assumed:** a provisional input that still needs confirmation.

## 12. Repository map

| Folder | What we keep there |
|---|---|
| `Mobility Management/` | Propulsion, steering, odometry, and navigation |
| `Obstacle Management/` | Camera-based obstacle detection and avoidance |
| `Power and Sense Management/` | Electrical interfaces, power, and sensors |
| `engineering/` | Mechanical, electrical, perception, control, and simulation notes |
| `hardware/` | Hardware setup, calibration, and custom printed-part records |
| `software/` | Python challenge programs and software comparison |
| Native LEGO EV3 project files | Original `.ev3` graphical projects |
| `schemes/` | Drawing list and engineering diagram index |
| `validation/` | Test planning and test-record format |
| `docs/` | Portfolio, verification evidence, and repository guide |
| `t-photos/`, `v-photos/`, `video/` | Team and vehicle media indexes |

## 13. Main project references

The main references are the repository README, verification evidence, release checklist, reference vehicle design case, analytical simulation, Python challenge programs, native EV3 block projects, sensor calibration procedure, and drawing register.

**Repository:** https://github.com/WSSB2026WRO/Qatar-FE

## Revision control

When we make an important change, we record why we made it, which subsystem it affects, the source version, parameter changes, test evidence, and how to return to the previous version.

We use this for software, mechanical, electrical, camera, and validation changes. We also label information as source-derived, configured, assumed, calculated, simulated, or measured. Reading code or documentation is not the same as testing the physical robot.

For each revision, we list the files that changed and the Git commit. If we change hardware or calibration, we also record the robot setup and test conditions so the check can be repeated. We keep an earlier working commit or release as a rollback point.