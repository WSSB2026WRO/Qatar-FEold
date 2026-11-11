# Source Code

## Main challenge programs

We keep the two challenge programs in their own folders:

- [Open Challenge](../software/open_challenge/open_challenge.py)
- [Obstacle Challenge](../software/obstacle_challenge/obstacle_challenge.py)

## Platform

Both programs are written for the LEGO EV3 using Pybricks MicroPython. The Obstacle Challenge program also imports the Pixy2 EV3 library and communicates with the camera over I²C.

## What the programs include

| Function | Open Challenge | Obstacle Challenge |
|---|---|---|
| Motor initialization | Yes | Yes |
| Gyro calibration | Yes | Yes |
| Ultrasonic readings | Yes | Yes |
| Corridor centering | Yes | Yes |
| Corner detection | Yes | Yes |
| Lap counting | Yes | Yes |
| Pixy2 block readings | No | Yes |
| Pillar colour classification | No | Yes |
| Passing-side selection | No | Yes |
| Parking sequence | No | Yes |

## How we manage changes

1. Keep the supplied reference programs available.
2. Make experimental changes in separate files or branches.
3. Keep the hardware ports and steering direction conventions documented.
4. Record parameter changes and why we made them.
5. Run syntax checks before uploading a program.
6. After a control change, start with low-speed hardware checks.
7. Save the logs and compare them with the previous version.