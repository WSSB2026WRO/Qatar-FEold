# Mobility Management

## System purpose

Mobility Management covers vehicle propulsion, steering, corridor tracking, heading regulation, corner execution, lap counting, and the return-to-start manoeuvre.

The reference implementation is maintained in:
- [Open Challenge source](../software/open_challenge/open_challenge.py)
- [Open Challenge technical documentation](../software/open_challenge/README.md)
- [Control system design](../engineering/software/control_system_design.md)

## Drive configuration

| Interface | Configured device | Responsibility |
|---|---|---|
| Motor A | EV3 Medium Motor | Propulsion |
| Motor B | EV3 Medium Motor | Propulsion |
| Motor C | EV3 Medium Motor | Steering |
| Sensor S1 | Gyro | Heading feedback |
| Sensor S2 | Ultrasonic | Left wall distance |
| Sensor S3 | Ultrasonic | Right wall distance |

## Mobility functions

### Corridor following
The Open Challenge controller uses left and right ultrasonic readings to estimate the vehicle's lateral position relative to the corridor. A heading correction term helps keep the vehicle aligned with the corridor axis.

### Steering control
The steering actuator is commanded through motor C. The source code uses a bounded steering command and a separate steering target for cornering. The actuator-to-road-wheel mapping must be calibrated on the assembled mechanism.

### Corner navigation
Wall-opening detection is combined with gyro heading change. The program confirms an opening before accepting a corner and uses an angular target to complete the turn.

### Distance estimation
Drive motor encoder angles are converted into travelled distance using the configured wheel diameter and gear ratio. Wheel slip and drivetrain compliance can introduce odometry error.

## Configured Open Challenge values

| Parameter | Value |
|---|---:|
| Drive speed | 300 deg/s |
| Wheel diameter | 56 mm |
| Straight steering limit | 10 deg |
| Corner steering command | 20 deg |
| Lateral gain | 0.09 |
| Heading gain | 0.6 |
| Corner target | 90 deg |
| Route count | 12 corners |

## Engineering review checklist

- [ ] Confirm both drive motors rotate in the intended forward direction.
- [ ] Measure encoder distance over a known track length.
- [ ] Confirm steering zero with the wheels physically straight.
- [ ] Measure left and right steering travel.
- [ ] Verify gyro sign convention.
- [ ] Test corridor centering at reduced speed.
- [ ] Test left and right corner manoeuvres separately.
- [ ] Review encoder and gyro logs after each run.

## Records

Store mobility test logs, measured steering angles, wheel-distance calibration, and approved mechanical changes in this directory. Raw records should not be overwritten.
