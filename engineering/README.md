# Engineering Overview

This section documents the mechanical, electrical, software, and analytical engineering of the Qatar FE autonomous vehicle.

## Engineering disciplines

- Vehicle packaging and structural layout
- Drive-train and steering architecture
- Mass properties and vehicle dynamics
- Sensor integration and perception geometry
- Embedded control and navigation algorithms
- Additive manufacturing and custom mechanical interfaces
- Reliability analysis and verification planning

## Mechanical design

The mechanical design is organized around a compact chassis, independently documented drive and steering functions, protected sensor mounting, and serviceable electrical packaging.

Mass distribution is evaluated using a component-based model:

\[
x_{CG}=\frac{\sum m_i x_i}{\sum m_i},\quad
y_{CG}=\frac{\sum m_i y_i}{\sum m_i},\quad
z_{CG}=\frac{\sum m_i z_i}{\sum m_i}
\]

The equations define the calculation method. Numerical examples are provided in the reference design case.

## Vehicle dynamics

The engineering model considers longitudinal and lateral load transfer, traction limits, yaw inertia, steering geometry, and geometric rollover margin. These relationships support design comparison and control-system reasoning.

## Electrical and sensing architecture

The EV3 port map is documented in [Hardware Architecture](../hardware/README.md). The control programs use a gyro, two ultrasonic sensors, drive motors, and a steering motor. The Obstacle Challenge program additionally interfaces with Pixy2 over I²C.

## Software architecture

The software is separated into two independent challenge programs. Each program has its own mission state sequence, sensor processing, steering control, corner handling, and logging structure.

## Analytical design basis

The reference vehicle design case provides a consistent numerical framework for evaluating mass properties and vehicle dynamics. All calculations are reproducible from the stated equations and input parameters.

## Engineering terminology

| Term | Meaning |
|---|---|
| Configured | A value defined in the source program |
| Assumed | A design input selected for analytical study |
| Calculated | A value derived mathematically from stated inputs |
| Measured | A value obtained from an instrumented physical observation |
| Validated | A result supported by repeatable tests and acceptance criteria |

This terminology keeps design calculations, software settings, and physical observations technically distinct.
