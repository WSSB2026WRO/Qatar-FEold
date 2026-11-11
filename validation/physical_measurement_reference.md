# Physical Performance Comparison — Team 6038

## 1. What we want to compare

We have two software implementations for each WRO Future Engineers challenge:

- Python / Pybricks MicroPython.
- Native LEGO EV3 graphical blocks.

We want to compare program preparation, startup delay, control-cycle timing, mission duration, distance accuracy, heading accuracy, and repeatability. To make the comparison fair, both programs should use the same robot, mechanical setup, battery condition, sensor positions, course, and test conditions.

## 2. Example comparison values — not test results

The tables in this section contain example values to show how we could present the comparison. **They are not measurements from our robot and must not be presented as real test results.** We need to replace them with data from paired physical trials before drawing conclusions.

### 2.1 Open Challenge example

| Metric | Python example | EV3 blocks example | Unit |
|---|---:|---:|---|
| Program preparation and transfer | 4.2 | 6.5 | s |
| Power-on to READY state | 2.6 | 2.9 | s |
| Straight control-loop period | 20 | 28 | ms |
| Corner control-loop period | 10 | 18 | ms |
| Full mission duration | 43.2 | 45.6 | s |
| Mean absolute distance error | 2.8 | 3.2 | cm |
| Mean absolute heading error | 2.4 | 3.1 | degrees |

The Python program sets a 20 ms straight loop and a 10 ms corner loop. The other values are examples only and still need physical verification.

### 2.2 Obstacle Challenge example

| Metric | Python example | EV3 blocks example | Unit |
|---|---:|---:|---|
| Program preparation and transfer | 4.8 | 7.1 | s |
| Power-on to READY state | 2.8 | 3.1 | s |
| Main control-loop period | 20 | 32 | ms |
| Corner / manoeuvre loop period | 10 | 20 | ms |
| Full mission duration | 59.4 | 62.8 | s |
| Mean absolute distance error | 3.5 | 4.0 | cm |
| Mean absolute heading error | 3.2 | 3.8 | degrees |
| Pillar avoidance success | 9/10 | 8/10 | example runs |
| Parking success | 9/10 | 8/10 | example runs |

The Python program sets a 20 ms main loop and a 10 ms corner/manoeuvre loop. The Obstacle Challenge also communicates with the Pixy2 over I²C, which can change the duration of individual cycles. The other values are examples and need physical verification.

## 3. Example physical-performance tables

The values below repeat the examples from Section 2 so that the report layout is clear. They are **not physical test results**.

### 3.1 Open Challenge example

| Metric | Python example | EV3 blocks example | Unit |
|---|---:|---:|---|
| Mission duration | 43.2 | 45.6 | s |
| Mean absolute distance error | 2.8 | 3.2 | cm |
| Mean absolute heading error | 2.4 | 3.1 | degrees |
| Successful runs / total runs | 5/5 | 5/5 | example runs |

### 3.2 Obstacle Challenge example

| Metric | Python example | EV3 blocks example | Unit |
|---|---:|---:|---|
| Mission duration | 59.4 | 62.8 | s |
| Mean absolute distance error | 3.5 | 4.0 | cm |
| Mean absolute heading error | 3.2 | 3.8 | degrees |
| Pillar avoidance success rate | 90 | 80 | % in example data |
| Successful parking runs / total runs | 9/10 | 8/10 | example runs |

## 4. How we should measure

| Measurement | What it means | Suggested method |
|---|---|---|
| Program preparation and transfer | From starting the same preparation/transfer process until the program is ready on the EV3 | Use the same computer, connection, and timing points |
| Startup latency | From EV3 power-on to READY | Video with a visible time reference |
| Control-cycle duration | Time between repeated executions of the same control-loop section | Timestamp logging or high-frame-rate video |
| Mission duration | From the agreed start signal to the defined finish | Video or stopwatch |
| Distance error | Difference between target distance and measured travel | Marked course and tape measure |
| Heading error | Difference between target and final heading | Angle reference or measured course geometry |
| Repeatability | How consistent repeated runs are | At least five valid runs per implementation and challenge |

Pybricks transfer or bytecode preparation is not necessarily the same operation as preparing a project in the EV3 graphical environment. Unless we time equivalent compilation steps, we should use the neutral term *program preparation and transfer*.

## 5. Example run-by-run table — invented sample entries

The entries below are **made-up sample values used only to demonstrate the table format**. They are not logs from actual robot runs. The obstacle success percentages shown earlier are also example values, not results from ten completed attempts.

| Challenge | Program | Example run | Cycle (ms) | Mission (s) | Distance error (cm) | Heading error (°) | Example note |
|---|---|---:|---:|---:|---:|---:|---|
| Open | Python | 1 | 19.8 | 42.8 | 2.6 | 2.2 | Example only |
| Open | Python | 2 | 20.2 | 43.1 | 2.9 | 2.5 | Example only |
| Open | Python | 3 | 19.5 | 43.5 | 2.7 | 2.3 | Example only |
| Open | Python | 4 | 20.4 | 43.0 | 3.0 | 2.6 | Example only |
| Open | Python | 5 | 19.9 | 43.6 | 2.8 | 2.4 | Example only |
| Open | EV3 blocks | 1 | 28.4 | 45.1 | 3.0 | 2.9 | Example only |
| Open | EV3 blocks | 2 | 27.9 | 45.8 | 3.3 | 3.2 | Example only |
| Open | EV3 blocks | 3 | 29.1 | 45.4 | 3.1 | 3.0 | Example only |
| Open | EV3 blocks | 4 | 28.7 | 46.0 | 3.4 | 3.3 | Example only |
| Open | EV3 blocks | 5 | 27.8 | 45.7 | 3.2 | 3.1 | Example only |
| Obstacle | Python | 1 | 19.8 | 59.0 | 3.3 | 3.0 | Example only |
| Obstacle | Python | 2 | 20.2 | 59.5 | 3.6 | 3.3 | Example only |
| Obstacle | Python | 3 | 19.5 | 59.2 | 3.4 | 3.1 | Example only |
| Obstacle | Python | 4 | 20.4 | 59.8 | 3.7 | 3.4 | Example only |
| Obstacle | Python | 5 | 19.9 | 59.5 | 3.5 | 3.2 | Example only |
| Obstacle | EV3 blocks | 1 | 31.4 | 62.2 | 3.8 | 3.6 | Example only |
| Obstacle | EV3 blocks | 2 | 32.1 | 62.6 | 4.1 | 3.9 | Example only |
| Obstacle | EV3 blocks | 3 | 32.8 | 63.0 | 3.9 | 3.7 | Example only |
| Obstacle | EV3 blocks | 4 | 31.7 | 62.8 | 4.2 | 4.0 | Example only |
| Obstacle | EV3 blocks | 5 | 32.0 | 63.4 | 4.0 | 3.8 | Example only |

## 6. Analysing the measurements

For each measurement and each program, we should calculate the mean, minimum, maximum, standard deviation, and number of valid runs. If a run is invalid, we should record why and keep it separate from the performance average.

For differences smaller than one second, we should use milliseconds. We should also show the minimum and maximum cycle times so that a few slow cycles are not hidden by the average.

## 7. What the current program settings tell us

Our Python programs are configured for a 20 ms straight or main loop and a 10 ms loop during corners or manoeuvres. These are settings in the source code, not measured cycle times. The EV3 block timing figures in the examples are planning values; physical tests are needed to find the actual timing.

We should report mission time, accuracy, preparation time, and startup delay only after paired trials. That will help us separate software timing from the robot's physical performance.

## 8. Example summary layout — not measured results

This final table shows how we could present a short comparison after collecting a complete dataset. The figures are illustrative working values only. They are not physical results and must be replaced before we make a conclusion.

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
| Obstacle | Corner / manoeuvre loop period | 10 | 20 | ms |
| Obstacle | Mission duration | 59.4 | 62.8 | s |
| Obstacle | Distance error | 3.5 | 4.0 | cm |
| Obstacle | Heading error | 3.2 | 3.8 | degrees |
| Obstacle | Pillar avoidance success | 9/10 | 8/10 | example runs |
| Obstacle | Parking success | 9/10 | 8/10 | example runs |

### Example control-cycle samples

| Program | Sample 1 | Sample 2 | Sample 3 | Sample 4 | Sample 5 | Example mean |
|---|---:|---:|---:|---:|---:|---:|
| Python | 19.8 | 20.2 | 19.5 | 20.4 | 19.9 | 19.96 |
| EV3 blocks | 28.4 | 27.9 | 29.1 | 28.7 | 27.8 | 28.38 |

Everything in this section is here to demonstrate the layout and calculations. It must remain separate from real measurement records until we have checked the robot and saved the actual trial data.