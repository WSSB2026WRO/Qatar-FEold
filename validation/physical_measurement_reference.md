# Physical Performance Comparison — Team 6038

## 1. Comparison objective

Team 6038 developed two implementations for each WRO Future Engineers challenge:

- Python / Pybricks MicroPython.
- Native LEGO EV3 graphical blocks.

The comparison covers program preparation, startup, control-cycle timing, mission duration, distance accuracy, heading accuracy, and repeatability. Both implementations are compared on the same robot, mechanical configuration, battery condition, sensor placement, course, and test conditions.

## 2. Timing reference values and actual measurements

The reference figures below are engineering estimates derived from the program structure and configured loop periods. They are comparison targets, not recorded physical measurements. The actual-measurement columns are reserved for the team's test results.

### 2.1 Open Challenge

| Metric | Python reference | EV3 blocks reference | Python actual | EV3 blocks actual | Unit |
|---|---:|---:|---:|---:|---|
| Straight control-loop period | 20 | 20–35 | — | — | ms |
| Corner control-loop period | 10 | 15–30 | — | — | ms |
| Program preparation and transfer | Not predictable from source code | Not predictable from source code | — | — | s |
| Power-on to READY state | Hardware/startup dependent | Hardware/startup dependent | — | — | s |
| Full mission duration | Course and driving dependent | Course and driving dependent | — | — | s |

The Python program explicitly configures a 20 ms straight loop and a 10 ms corner loop. The EV3 block ranges are approximate engineering expectations for a comparable sensor-and-motor control sequence; actual timing depends on block structure, sensor operations, and scheduling.

### 2.2 Obstacle Challenge

| Metric | Python reference | EV3 blocks reference | Python actual | EV3 blocks actual | Unit |
|---|---:|---:|---:|---:|---|
| Main control-loop period | 20 | 20–40 | — | — | ms |
| Corner / maneuver loop period | 10 | 15–30 | — | — | ms |
| Program preparation and transfer | Not predictable from source code | Not predictable from source code | — | — | s |
| Power-on to READY state | Hardware/startup dependent | Hardware/startup dependent | — | — | s |
| Full mission duration | Course and driving dependent | Course and driving dependent | — | — | s |

The Python program explicitly configures a 20 ms main loop and a 10 ms corner/maneuver loop. The EV3 block ranges are approximate engineering expectations, not measured results. The obstacle program also performs Pixy2 I²C communication, which can affect the duration of individual control cycles.

## 3. Physical performance measurements

These metrics require physical trials. No numerical prediction is assigned where the result depends strongly on the actual chassis, tires, battery, sensor calibration, course geometry, or driving behaviour.

### 3.1 Open Challenge

| Metric | Python actual | EV3 blocks actual | Unit |
|---|---:|---:|---|
| Mission duration | — | — | s |
| Mean absolute distance error | — | — | cm |
| Mean absolute heading error | — | — | degrees |
| Successful runs / total runs | — | — | runs |

### 3.2 Obstacle Challenge

| Metric | Python actual | EV3 blocks actual | Unit |
|---|---:|---:|---|
| Mission duration | — | — | s |
| Mean absolute distance error | — | — | cm |
| Mean absolute heading error | — | — | degrees |
| Pillar avoidance success rate | — | — | % |
| Successful parking runs / total runs | — | — | runs |

## 4. Measurement method

| Measurement | Definition | Method |
|---|---|---|
| Program preparation and transfer | From initiating the same preparation/transfer workflow to the program being available on the EV3 | Same computer, connection method, and timing boundaries |
| Startup latency | From EV3 power-on to the READY state | Video with visible time reference |
| Control-cycle duration | Time between successive executions of the same control-loop section | Timestamp instrumentation or high-frame-rate video |
| Mission duration | From the agreed start signal to the defined finish condition | Video or stopwatch |
| Distance error | Absolute difference between target and measured physical distance | Marked course and tape measure |
| Heading error | Absolute difference between target and final heading | Angle reference or measured course geometry |
| Repeatability | Consistency across repeated runs | At least five valid runs per implementation and challenge |

Pybricks transfer/bytecode preparation and the EV3 graphical environment's project preparation are not necessarily equivalent compiler operations. The neutral term *program preparation and transfer* is used unless the same precisely defined compilation stage is timed in both environments.

## 5. Raw trial record

| Challenge | Implementation | Run | Control cycle (ms) | Mission (s) | Distance error (cm) | Heading error (°) | Result / notes |
|---|---|---:|---:|---:|---:|---:|---|
| Open | Python | 1 | — | — | — | — | |
| Open | Python | 2 | — | — | — | — | |
| Open | Python | 3 | — | — | — | — | |
| Open | Python | 4 | — | — | — | — | |
| Open | Python | 5 | — | — | — | — | |
| Open | EV3 blocks | 1 | — | — | — | — | |
| Open | EV3 blocks | 2 | — | — | — | — | |
| Open | EV3 blocks | 3 | — | — | — | — | |
| Open | EV3 blocks | 4 | — | — | — | — | |
| Open | EV3 blocks | 5 | — | — | — | — | |
| Obstacle | Python | 1 | — | — | — | — | |
| Obstacle | Python | 2 | — | — | — | — | |
| Obstacle | Python | 3 | — | — | — | — | |
| Obstacle | Python | 4 | — | — | — | — | |
| Obstacle | Python | 5 | — | — | — | — | |
| Obstacle | EV3 blocks | 1 | — | — | — | — | |
| Obstacle | EV3 blocks | 2 | — | — | — | — | |
| Obstacle | EV3 blocks | 3 | — | — | — | — | |
| Obstacle | EV3 blocks | 4 | — | — | — | — | |
| Obstacle | EV3 blocks | 5 | — | — | — | — | |

## 6. Statistical analysis

For each metric and implementation, the summary includes the arithmetic mean, minimum, maximum, standard deviation, and number of valid runs. Invalid runs are documented with their reason and excluded from the performance average.

Sub-second timing differences are expressed in milliseconds. A comparison of average cycle duration is accompanied by the observed minimum and maximum so that occasional slow cycles are not hidden by the mean.

## 7. Interpretation

The loop periods configured in the Python programs provide a code-derived timing reference: 20 ms on straight/main control and 10 ms during corners or maneuvers. The EV3 block timing ranges are engineering estimates for comparison planning. Measured values determine the actual performance comparison.

Mission duration, accuracy, preparation time, and startup latency are reported from paired trials rather than inferred from source code. This separates implementation timing from physical robot performance and supports a fair comparison between the two software approaches.
