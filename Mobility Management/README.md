# Mobility Management

## What we worked on

This section explains how our EV3 vehicle moves around the track. It covers the drive motors, steering, corridor following, corner turns, lap counting, and the return-to-start manoeuvre.

We use these files as the main references:
- [Open Challenge program](../software/open_challenge/open_challenge.py)
- [Open Challenge notes](../software/open_challenge/README.md)
- [Control system design](../engineering/software/control_system_design.md)

## Motor and sensor setup

| Port | Device | What we use it for |
|---|---|---|
| Motor A | EV3 Medium Motor | Driving |
| Motor B | EV3 Medium Motor | Driving |
| Motor C | EV3 Medium Motor | Steering |
| Sensor S1 | Gyro | Checking the heading |
| Sensor S2 | Ultrasonic | Measuring the left wall distance |
| Sensor S3 | Ultrasonic | Measuring the right wall distance |

## How the vehicle moves

### Following the corridor
We read the two ultrasonic sensors and use their distances to estimate whether the vehicle is closer to the left or right wall. The controller then adjusts the steering to keep the vehicle near the centre. The gyro reading is also used to help keep the vehicle pointed along the corridor.

### Steering
Motor C moves the steering mechanism. In the program, we limit the steering command so it stays within the configured range. We use a separate target when the vehicle needs to turn at a corner. The link between the motor encoder and the actual wheel angle depends on the steering mechanism.

### Turning at corners
We look for a wall opening and compare it with the change in heading from the gyro. The program checks that an opening is present before starting the turn. It then uses the gyro angle as the turn target.

### Estimating distance
We use the drive motor encoder angles, the configured wheel diameter, and the gear ratio to estimate how far the vehicle has travelled. This estimate can be affected by wheel slip and small movements in the drivetrain.

## Current Open Challenge settings

These are the values configured in the program. They should not be read as a record of measured performance.

| Parameter | Configured value |
|---|---:|
| Drive speed | 300 deg/s |
| Wheel diameter | 56 mm |
| Straight steering limit | 10 deg |
| Corner steering command | 20 deg |
| Lateral gain | 0.09 |
| Heading gain | 0.6 |
| Corner target | 90 deg |
| Route count | 12 corners |

## Checks before running

This is the checklist we use when setting up or checking the mobility system:

1. Check that both drive motors turn in the correct direction and that their encoders respond.
2. Set the steering encoder reference while the road wheels are straight.
3. Measure encoder travel over a known distance.
4. Check the steering movement to the left and right.
5. Check the gyro direction and measure its drift while the vehicle is still.
6. Try corridor centering at a lower speed first.
7. Test both left and right corner turns.
8. Review the encoder and gyro logs after each run.