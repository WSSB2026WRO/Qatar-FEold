# Open Challenge — How Our Program Works

## Mission

![SYS-001 — Autonomous vehicle system architecture](../../docs/drawings/SYS-001_autonomous_vehicle_architecture.svg)

The vehicle dynamics and steering drawings are available in [DYN-001](../../docs/drawings/DYN-001_vehicle_dynamics.svg) and [STR-001](../../docs/drawings/STR-001_ackermann_steering.svg).

For the Open Challenge, our program follows a route with twelve corners. It tries to keep the robot near the centre of the corridor, corrects its heading, and works out the final approach back to the starting section.

## Hardware connections

| Port | Device | Use |
|---|---|---|
| A | EV3 Medium Motor | Drive channel as configured in the program |
| B | EV3 Medium Motor | Drive channel |
| C | EV3 Medium Motor | Steering |
| S1 | Gyro | Heading measurement |
| S2 | Ultrasonic | Left wall distance |
| S3 | Ultrasonic | Right wall distance |

## Settings in this program

| Parameter | Value |
|---|---:|
| Version | OPEN-COMP-2 |
| Drive speed | 300 deg/s |
| Wheel diameter | 56 mm |
| Gear ratio | 1 |
| Straight steering limit | 10 deg |
| Corner steering command | 20 deg |
| Lateral gain | 0.09 |
| Heading gain | 0.6 |
| Centre tolerance | 10 mm |
| Wall detection limit | 950 mm |
| Wall danger threshold | 150 mm |
| Corner target | 90 deg |
| Route corner count | 12 |

These are the current program settings. They are not a record of measured performance.

## Mission steps

1. Initialize the motors and sensors.
2. Wait for the operator to start the program.
3. Calibrate the gyro while the robot is still.
4. Read the left and right wall distances.
5. Estimate how far the robot is from the corridor centre.
6. Correct the lateral position and heading.
7. Confirm a corridor opening over several readings.
8. Work out the route direction and turn at the corner.
9. Ignore new opening detections for the configured distance after a turn.
10. Continue until the twelve-corner route is complete.
11. Calculate and drive the final approach.
12. Stop and save the run log.

## Keeping the robot near the corridor centre

We use both ultrasonic readings to estimate the robot's lateral position. The program combines a proportional correction for the sideways error with a heading correction. It limits the steering command to the configured straight-driving range.

## Finding and turning at corners

The program accepts an opening only after the distance threshold has been exceeded for several readings in a row. After a turn, it uses a distance lockout so that it does not detect the previous opening again. It estimates the route direction from the first opening and keeps that direction for the rest of the route.

## Returning to the start

The final approach uses the first opening distance and the route segments stored by the program. It calculates the remaining distance using these values and the configured offset. The last part of the approach uses a lower speed near the stopping point.

## Run log

The program writes `log_open.csv`. It records the phase, route progress, sensor readings, heading, steering, and event information so the run can be reviewed later.

## What the software checks tell us

This page describes the program settings and control logic. Our automated checks verify Python syntax and documentation consistency. They do not replace a route test with the physical EV3 robot. The current repository snapshot does not include a completed physical mission log.