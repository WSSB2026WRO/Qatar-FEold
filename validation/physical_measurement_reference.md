# Physical Measurement and Performance Comparison — Team 6038

## 1. Objective

Team 6038 developed two software implementations for each WRO Future Engineers challenge:

- Python / Pybricks MicroPython.
- Native LEGO EV3 graphical blocks.

The comparison covers program preparation and transfer, EV3 startup latency, control-cycle duration, mission execution time, distance accuracy, heading accuracy, and repeatability. Both implementations are evaluated using the same robot, mechanical configuration, battery condition, sensor placement, course, and test conditions.

## 2. Open Challenge — measurement results

| Metric | Python / MicroPython | EV3 blocks | Unit |
|---|---:|---:|---|
| Program preparation and transfer | — | — | s |
| Power-on to program ready | — | — | s |
| Representative control-cycle duration | — | — | ms |
| Mission duration | — | — | s |
| Mean absolute distance error | — | — | cm |
| Mean absolute heading error | — | — | degrees |

## 3. Obstacle Challenge — measurement results

| Metric | Python / MicroPython | EV3 blocks | Unit |
|---|---:|---:|---|
| Program preparation and transfer | — | — | s |
| Power-on to program ready | — | — | s |
| Representative control-cycle duration | — | — | ms |
| Mission duration | — | — | s |
| Mean absolute distance error | — | — | cm |
| Mean absolute heading error | — | — | degrees |

## 4. Physical measurement definitions

| Measurement | Start and end points | Instrument or method |
|---|---|---|
| Program preparation and transfer | From initiating the defined preparation/transfer operation to the program being available on the EV3 | Same computer, connection method, and timing rule for both versions |
| Startup latency | From EV3 power-on to a clearly defined ready state immediately before mission execution | Video recording with a visible time reference |
| Control-cycle duration | Time between successive executions of the same control-loop section | Timestamp instrumentation where supported, or a repeatable external timing method |
| Mission duration | From the agreed start signal to the defined finish condition | Video or stopwatch with identical start/finish definitions |
| Distance error | Absolute difference between target distance and measured physical distance | Marked course and tape measure |
| Heading error | Absolute difference between target heading and final measured heading | Angle reference or measured course geometry |
| Repeatability | Variation between repeated runs under the same conditions | Repeated trials for each implementation and challenge |

**Timing terminology:** Pybricks program transfer/bytecode preparation and the EV3 graphical environment's project preparation are not necessarily equivalent compiler operations. The neutral term *program preparation and transfer* is used unless the same precisely defined compilation stage can be timed in both environments.

## 5. Trial protocol

A paired comparison uses the same physical robot and course for both implementations. Battery charge, starting position, sensor and motor configuration, and environmental conditions are kept as consistent as possible. Each implementation is evaluated over at least five valid runs for each challenge.

Each run records:
- Individual measured values.
- Any interruption, sensor loss, collision, or invalid run.
- The measurement method and timing boundaries.

Sub-second timings are expressed in milliseconds (ms). Video-based measurements include the recording frame rate and the frames used to identify the start and end events.

## 6. Raw measurement record

| Challenge | Implementation | Run | Preparation / transfer (s) | Startup (s) | Control cycle (ms) | Mission (s) | Distance error (cm) | Heading error (°) | Notes |
|---|---|---:|---:|---:|---:|---:|---:|---:|---|
| Open | Python | 1 | — | — | — | — | — | — | |
| Open | Python | 2 | — | — | — | — | — | — | |
| Open | Python | 3 | — | — | — | — | — | — | |
| Open | Python | 4 | — | — | — | — | — | — | |
| Open | Python | 5 | — | — | — | — | — | — | |
| Open | EV3 blocks | 1 | — | — | — | — | — | — | |
| Open | EV3 blocks | 2 | — | — | — | — | — | — | |
| Open | EV3 blocks | 3 | — | — | — | — | — | — | |
| Open | EV3 blocks | 4 | — | — | — | — | — | — | |
| Open | EV3 blocks | 5 | — | — | — | — | — | — | |
| Obstacle | Python | 1 | — | — | — | — | — | — | |
| Obstacle | Python | 2 | — | — | — | — | — | — | |
| Obstacle | Python | 3 | — | — | — | — | — | — | |
| Obstacle | Python | 4 | — | — | — | — | — | — | |
| Obstacle | Python | 5 | — | — | — | — | — | — | |
| Obstacle | EV3 blocks | 1 | — | — | — | — | — | — | |
| Obstacle | EV3 blocks | 2 | — | — | — | — | — | — | |
| Obstacle | EV3 blocks | 3 | — | — | — | — | — | — | |
| Obstacle | EV3 blocks | 4 | — | — | — | — | — | — | |
| Obstacle | EV3 blocks | 5 | — | — | — | — | — | — | |

## 7. Statistical summary

For every metric and implementation, the results are summarized using the arithmetic mean, minimum, maximum, and standard deviation. Only valid runs are included. The number of valid runs is reported alongside each summary.

## 8. Comparison framework

The comparison separates software workflow from physical robot behaviour:

1. **Preparation time** describes the defined computer-to-EV3 workflow.
2. **Startup latency** describes the time required to reach the same ready state.
3. **Control-cycle duration** describes execution timing at a defined measurement boundary.
4. **Mission duration and accuracy** describe physical performance on the same course.
5. **Repeatability** describes consistency across repeated runs.

The implementation comparison is based on the recorded measurements and stated test conditions. Sub-second differences are retained in milliseconds to avoid hiding small but potentially meaningful timing variations.
