# Software Engineering

Two independent programs are maintained for the two WRO Future Engineers formats. The source files are preserved as supplied; documentation explains their configured behavior and identifies the assumptions that require physical validation.

## Program index

| Challenge | Source | Version | Main sensing |
|---|---|---|---|
| Open | [open_challenge.py](open_challenge/open_challenge.py) | OPEN-COMP-2 | Gyro + dual ultrasonic + encoders |
| Obstacle | [obstacle_challenge.py](obstacle_challenge/obstacle_challenge.py) | OBST-1 | Gyro + dual ultrasonic + encoders + Pixy2 |

## Shared software principles

- Explicit initialization before motion.
- Gyro drift measurement before autonomous navigation.
- Encoder-based distance estimation.
- Heading-aware wall measurements.
- State-based corner detection.
- Timeouts and safety limits around manoeuvres.
- CSV logging for post-run analysis.

## Runtime notes

The supplied files target Pybricks MicroPython and EV3 hardware. They are not ordinary desktop Python applications. A successful desktop syntax check does not validate device APIs, motor polarity, sensor addressing, timing, or physical behavior.

## Change control

- Keep known reference versions intact.
- Make experiments in separately named files or branches.
- Record source hashes for competition builds.
- Change one tuning family at a time.
- Store test logs and conditions with every performance claim.
