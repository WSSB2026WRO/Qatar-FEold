# Engineering Overview

This folder brings together the engineering work behind our Qatar FE autonomous vehicle. We have separated the notes by topic so it is easier to find the design details, calculations, and software decisions.

## Areas we worked on

- Chassis layout and component placement
- Drive and steering mechanisms
- Mass distribution and vehicle dynamics
- Sensor mounting and camera geometry
- Control and navigation software
- 3D-printed parts and mechanical connections
- Reliability and verification planning

## Mechanical design

Our mechanical notes describe the chassis, drive system, steering, sensor mounts, and the way the electrical parts fit on the vehicle.

For the centre of gravity, we use the component masses and their positions:

[
x_{CG}=\frac{\sum m_i x_i}{\sum m_i},\quad
y_{CG}=\frac{\sum m_i y_i}{\sum m_i},\quad
z_{CG}=\frac{\sum m_i z_i}{\sum m_i}
]

This gives the calculation method. The reference design case contains example inputs and calculated values; they are not measurements of the finished robot.

## Vehicle dynamics

We use the dynamics model to think about longitudinal and lateral load transfer, traction, yaw inertia, steering geometry, and the geometric rollover margin. These calculations help us compare design choices, but they do not replace physical testing.

## Electrical and sensors

The EV3 port map is in [Hardware Architecture](../hardware/README.md). Our programs use a gyro, two ultrasonic sensors, two drive motors, and one steering motor. The Obstacle Challenge program also communicates with the Pixy2 over I²C.

## Software

We keep separate programs for the Open Challenge and Obstacle Challenge. Each one has its own mission sequence, sensor processing, steering control, corner handling, and logging.

## Reference calculations

The reference vehicle design case gives us one consistent set of inputs for mass and vehicle-dynamics calculations. The equations and assumptions are written down so the results can be checked and calculated again.

## Words we use in the documents

| Term | Meaning in our project |
|---|---|
| Configured | A value set in the source program |
| Assumed | An input we selected for a calculation |
| Calculated | A result obtained from stated inputs and equations |
| Measured | A value read from the physical vehicle using an instrument |
| Validated | A result supported by repeatable tests and acceptance criteria |