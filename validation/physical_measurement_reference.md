# Physical Performance Comparison — Team 6038

## 1. Comparison objective

Team 6038 developed two implementations for each WRO Future Engineers challenge:

- Python / Pybricks MicroPython.
- Native LEGO EV3 graphical blocks.

The comparison covers program preparation, startup, control-cycle timing, mission duration, distance accuracy, heading accuracy, and repeatability. Both implementations are compared on the same robot, mechanical configuration, battery condition, sensor placement, course, and test conditions.

## 2. Python / EV3 comparison values

We filled the tables with example values to show how the comparison can be presented. These figures are not measurements from our robot. Before using them as test results, we must replace them with data from paired trials.

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

## 3. Physical performance comparison

The tables below use the same example values as Section 2. They show the report layout only and are not physical test results.

### 3.1 Open Challenge

| Metric | Python example | EV3 blocks example | Unit |
|---|---:|---:|---|
| Mission duration | 43.2 | 45.6 | s |
| Mean absolute distance error | 2.8 | 3.2 | cm |
| Mean absolute heading error | 2.4 | 3.1 | degrees |
| Successful runs / total runs | 5/5 | 5/5 | runs |

### 3.2 Obstacle Challenge

| Metric | Python example | EV3 blocks example | Unit |
|---|---:|---:|---|
| Mission duration | 59.4 | 62.8 | s |
| Mean absolute distance error | 3.5 | 4.0 | cm |
| Mean absolute heading error | 3.2 | 3.8 | degrees |
| Pillar avoidance success rate | 90 | 80 | % |
| Successful parking runs / total runs | 9/10 | 8/10 | runs |

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

## 5. Raw trial record — illustrative dataset

The run-by-run values below are sample entries to show how we can record each trial. They are not logs from actual robot runs. The obstacle success percentages in Section 3 also come from an example set of ten attempts.

| Challenge | Implementation | Run | Control cycle (ms) | Mission (s) | Distance error (cm) | Heading error (°) | Result / notes |
|---|---|---:|---:|---:|---:|---:|---|
| Open | Python | 1 | 19.8 | 42.8 | 2.6 | 2.2 | Completed |
| Open | Python | 2 | 20.2 | 43.1 | 2.9 | 2.5 | Completed |
| Open | Python | 3 | 19.5 | 43.5 | 2.7 | 2.3 | Completed |
| Open | Python | 4 | 20.4 | 43.0 | 3.0 | 2.6 | Completed |
| Open | Python | 5 | 19.9 | 43.6 | 2.8 | 2.4 | Completed |
| Open | EV3 blocks | 1 | 28.4 | 45.1 | 3.0 | 2.9 | Completed |
| Open | EV3 blocks | 2 | 27.9 | 45.8 | 3.3 | 3.2 | Completed |
| Open | EV3 blocks | 3 | 29.1 | 45.4 | 3.1 | 3.0 | Completed |
| Open | EV3 blocks | 4 | 28.7 | 46.0 | 3.4 | 3.3 | Completed |
| Open | EV3 blocks | 5 | 27.8 | 45.7 | 3.2 | 3.1 | Completed |
| Obstacle | Python | 1 | 19.8 | 59.0 | 3.3 | 3.0 | Completed |
| Obstacle | Python | 2 | 20.2 | 59.5 | 3.6 | 3.3 | Completed |
| Obstacle | Python | 3 | 19.5 | 59.2 | 3.4 | 3.1 | Completed |
| Obstacle | Python | 4 | 20.4 | 59.8 | 3.7 | 3.4 | Completed |
| Obstacle | Python | 5 | 19.9 | 59.5 | 3.5 | 3.2 | Completed |
| Obstacle | EV3 blocks | 1 | 31.4 | 62.2 | 3.8 | 3.6 | Completed |
| Obstacle | EV3 blocks | 2 | 32.1 | 62.6 | 4.1 | 3.9 | Completed |
| Obstacle | EV3 blocks | 3 | 32.8 | 63.0 | 3.9 | 3.7 | Completed |
| Obstacle | EV3 blocks | 4 | 31.7 | 62.8 | 4.2 | 4.0 | Completed |
| Obstacle | EV3 blocks | 5 | 32.0 | 63.4 | 4.0 | 3.8 | Completed |

## 6. Statistical analysis

For each metric and implementation, the summary includes the arithmetic mean, minimum, maximum, standard deviation, and number of valid runs. Invalid runs are documented with their reason and excluded from the performance average.

Sub-second timing differences are expressed in milliseconds. A comparison of average cycle duration is accompanied by the observed minimum and maximum so that occasional slow cycles are not hidden by the mean.

## 7. Interpretation

Our Python programs are configured for a 20 ms straight/main loop and a 10 ms loop during corners or manoeuvres. These are program settings, not measured cycle times. The EV3 block timing figures are estimates for planning the comparison; actual tests are needed to establish the results.

We will report mission time, accuracy, preparation time, and startup delay from paired trials rather than estimating them from the source code. This will help us keep software timing separate from the robot's physical performance.

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
