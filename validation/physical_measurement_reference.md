# Physical Measurement Reference — Team 6038

> **DATA STATUS: SIMULATED EXAMPLE — NOT MEASURED ON THE TEAM'S ROBOT.**  
> Every numerical value in this document is illustrative. It is included to define a practical measurement format and demonstrate the comparison method. It is not a test report, not evidence of completed physical trials, and must never be cited as an observed result. The team's measured values take precedence and replace this example dataset.

## 1. Purpose

Team 6038 developed two implementations for each challenge:

- Python / Pybricks MicroPython.
- Native LEGO EV3 graphical blocks.

The comparison considers program preparation, EV3 startup, control-loop timing, mission duration, and repeatability. The same robot, mechanical configuration, battery condition, course, sensor placement, and environmental conditions form the basis of a fair paired comparison.

## 2. Illustrative dataset

The following numbers are **fictional demonstration values only**. They show the units, precision, and structure suitable for a results table; they do not describe the actual performance of either implementation.

### 2.1 Open Challenge — example values

| Metric | Python / MicroPython | EV3 blocks | Unit |
|---|---:|---:|---|
| Program preparation and transfer | 4.2 | 6.8 | s |
| Power-on to program ready | 2.6 | 2.9 | s |
| Representative control-cycle duration | 18.4 | 22.7 | ms |
| Mission duration | 42.6 | 44.1 | s |
| Mean absolute distance error | 2.8 | 3.1 | cm |
| Mean absolute heading error | 2.4 | 2.7 | degrees |

### 2.2 Obstacle Challenge — example values

| Metric | Python / MicroPython | EV3 blocks | Unit |
|---|---:|---:|---|
| Program preparation and transfer | 4.6 | 7.2 | s |
| Power-on to program ready | 2.7 | 3.0 | s |
| Representative control-cycle duration | 20.1 | 24.3 | ms |
| Mission duration | 58.3 | 60.5 | s |
| Mean absolute distance error | 3.4 | 3.7 | cm |
| Mean absolute heading error | 3.0 | 3.3 | degrees |

**Interpretation of this example:** the values illustrate how small timing differences can be displayed in milliseconds and how mission accuracy can be compared alongside speed. They do not establish that Python or EV3 blocks is faster or more accurate on the team's physical robot.

## 3. Physical measurement definitions

| Measurement | Start and end points | Suggested instrument or method |
|---|---|---|
| Program preparation and transfer | From initiating the defined preparation/transfer operation to the program being available on the EV3 | Same computer, cable or wireless method, and timing rule for both versions |
| Startup latency | From EV3 power-on to a clearly defined ready state immediately before mission execution | Video recording with visible time reference; repeat from a comparable power state |
| Control-cycle duration | Time between successive executions of the same control-loop section | Timestamp instrumentation where supported; otherwise high-frame-rate video or a repeatable external timing method |
| Mission duration | From the agreed start signal to the defined finish condition | Video or stopwatch; use the same start/finish definitions |
| Distance error | Absolute difference between commanded/target distance and measured physical distance | Marked course and tape measure |
| Heading error | Absolute difference between target heading and final measured heading | Printed angle reference or measured course geometry |
| Repeatability | Variation between repeated runs under the same conditions | At least five runs per implementation and challenge |

**Terminology:** Pybricks program transfer/bytecode preparation and the EV3 graphical environment's project preparation are not necessarily equivalent compiler operations. The comparison therefore uses the neutral term *program preparation and transfer* unless a precisely defined compilation stage is independently timed for both environments.

## 4. Measurement protocol

A paired trial uses the same physical robot and course for both implementations. The battery is brought to a comparable charge level, the robot is returned to the same starting position, and the same sensor and motor configuration is retained. Each implementation is run at least five times for each challenge.

For each metric, the record contains:
- Individual run values, not only the average.
- Arithmetic mean.
- Minimum and maximum.
- Standard deviation, when enough repeated values are available.
- Notes about interruptions, sensor loss, collisions, or invalid runs.

Sub-second timings are recorded in milliseconds (ms), with the measurement method and timing boundaries stated explicitly. A video-based measurement includes the frame rate and the frames used to identify start and end events.

## 5. Raw results record

The following blank structure is intended for the team's actual physical observations.

| Challenge | Implementation | Run | Preparation / transfer (s) | Startup (s) | Control cycle (ms) | Mission (s) | Distance error (cm) | Heading error (°) | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| Open | Python | 1 | — | — | — | — | — | — | |
| Open | EV3 blocks | 1 | — | — | — | — | — | — | |
| Obstacle | Python | 1 | — | — | — | — | — | — | |
| Obstacle | EV3 blocks | 1 | — | — | — | — | — | — | |

The run number is repeated for each additional trial. Summary statistics are calculated from valid measured runs only; the illustrative values in Section 2 are excluded.

## 6. Comparison principles

The comparison distinguishes software workflow from robot behaviour:

1. **Preparation time** describes the defined computer-to-EV3 workflow, not an assumed equivalent compilation process.
2. **Startup latency** describes how quickly each program reaches the same ready state.
3. **Control-cycle duration** describes execution timing at a stated measurement boundary.
4. **Mission duration and accuracy** describe physical robot performance on the same course.
5. **Repeatability** describes consistency across repeated runs, rather than the best single run.

No performance winner is inferred from the illustrative dataset. A conclusion about the better implementation is supported only by the team's own paired physical measurements and their recorded test conditions.
