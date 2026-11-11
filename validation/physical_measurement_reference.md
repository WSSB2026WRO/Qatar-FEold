# Physical Performance Comparison — Team 6038

## 1. Comparison objective

Team 6038 developed two implementations for each WRO Future Engineers challenge:

- Python / Pybricks MicroPython.
- Native LEGO EV3 graphical blocks.

The comparison covers program preparation, startup, control-cycle timing, mission duration, distance accuracy, heading accuracy, and repeatability. Both implementations are compared on the same robot, mechanical configuration, battery condition, sensor placement, course, and test conditions.

## 2. Python / EV3 comparison values

The tables below are populated with illustrative working values so the comparison can be read without empty cells. These figures are provisional examples, not verified physical measurements. Replace them with results from paired robot trials before presenting them as experimental findings.

### 2.1 Open Challenge

| Metric | Python value | EV3 blocks value | Unit |
|---|---:|---:|---|
| Program preparation and transfer | 4.2 | 6.5 | s |
| Power-on to READY state | 2.6 | 2.9 | s |
| Straight control-loop period | 20 | 28 | ms |
| Corner control-loop period | 10 | 18 | ms |
| Full mission duration | 43.2 | 45.6 | s |
| Mean absolute distance error | 2.8 | 3.2 | cm |
| Mean absolute heading error | 2.4 | 3.1 | degrees |

The Python program explicitly configures a 20 ms straight loop and a 10 ms corner loop. The other values are illustrative comparison figures and require physical verification.

### 2.2 Obstacle Challenge

| Metric | Python value | EV3 blocks value | Unit |
|---|---:|---:|---|
| Program preparation and transfer | 4.8 | 7.1 | s |
| Power-on to READY state | 2.8 | 3.1 | s |
| Main control-loop period | 20 | 32 | ms |
| Corner / maneuver loop period | 10 | 20 | ms |
| Full mission duration | 59.4 | 62.8 | s |
| Mean absolute distance error | 3.5 | 4.0 | cm |
| Mean absolute heading error | 3.2 | 3.8 | degrees |
| Pillar avoidance success | 9/10 | 8/10 | successful runs |
| Parking success | 9/10 | 8/10 | successful runs |

The Python program explicitly configures a 20 ms main loop and a 10 ms corner/maneuver loop. The obstacle program also performs Pixy2 I²C communication, which can affect the duration of individual control cycles. The remaining values are illustrative and require physical verification.

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

## 8. Illustrative comparison layout

The table below shows how a concise Python-versus-EV3 comparison can be presented once the team has a complete dataset. The figures are illustrative working values only; they are not physical test results and must not be reported as measured performance. Replace them with the team's paired trial results before drawing conclusions.

| Challenge | Metric | Python example | EV3 blocks example | Unit |
|---|---|---:|---:|---|
| Open | Program preparation and transfer | 4.2 | 6.5 | s |
| Open | Startup latency | 2.6 | 2.9 | s |
| Open | Straight control-loop period | 20 | 28 | ms |
| Open | Corner control-loop period | 10 | 18 | ms |
| Open | Mission duration | 43.2 | 45.6 | s |
| Open | Distance error | 2.8 | 3.2 | cm |
| Open | Heading error | 2.4 | 3.1 | degrees |
| Obstacle | Program preparation and transfer | 4.8 | 7.1 | s |
| Obstacle | Startup latency | 2.8 | 3.1 | s |
| Obstacle | Main control-loop period | 20 | 32 | ms |
| Obstacle | Corner / maneuver loop period | 10 | 20 | ms |
| Obstacle | Mission duration | 59.4 | 62.8 | s |
| Obstacle | Distance error | 3.5 | 4.0 | cm |
| Obstacle | Heading error | 3.2 | 3.8 | degrees |
| Obstacle | Pillar avoidance success | 9/10 | 8/10 | successful runs |
| Obstacle | Parking success | 9/10 | 8/10 | successful runs |

### Example control-cycle samples

| Implementation | Sample 1 | Sample 2 | Sample 3 | Sample 4 | Sample 5 | Mean |
|---|---:|---:|---:|---:|---:|---:|
| Python | 19.8 | 20.2 | 19.5 | 20.4 | 19.9 | 19.96 |
| EV3 blocks | 28.4 | 27.9 | 29.1 | 28.7 | 27.8 | 28.38 |

All values in this section are provided solely to demonstrate the presentation and calculation format. They must remain separate from the actual-measurement tables in Sections 2, 3, and 5 until verified by physical trials.
