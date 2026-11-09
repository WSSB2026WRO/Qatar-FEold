# Mobility Management 

## System purpose

Mobility Management covers vehicle propulsion, steering, corridor tracking, heading regulation, corner execution, lap counting, and the return-to-start manoeuvre.

Reference implementation:
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
The Open Challenge controller uses left and right ultrasonic readings to estimate the vehicle's lateral position relative to the corridor centre. A heading correction term maintains alignment with the corridor axis.

### Steering control
The steering actuator is commanded through motor C. The source program uses a bounded steering command and a separate steering target for cornering. The actuator-to-road-wheel mapping defines the relationship between motor encoder position and physical wheel angle.

### Corner navigation
Wall-opening detection is combined with gyro heading change. The program confirms an opening before accepting a corner and uses an angular target to complete the turn.

### Distance estimation
Drive motor encoder angles are converted into travelled distance using the configured wheel diameter and gear ratio. Wheel slip and drivetrain compliance influence odometry accuracy.

## Open Challenge configuration

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

## Mobility commissioning

1. Verify drive motor polarity and encoder response.
2. Set the steering encoder reference with the road wheels straight.
3. Measure encoder distance over a known track length.
4. Check left and right steering travel.
5. Verify gyro sign convention and stationary drift.
6. Evaluate corridor centering at reduced speed.
7. Test left and right corner manoeuvres.
8. Review encoder and gyro logs after each run.
