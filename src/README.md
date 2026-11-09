# Source Code

## Main challenge programs

The repository keeps the two supplied challenge programs in their dedicated folders:

- [Open Challenge](../software/open_challenge/open_challenge.py)
- [Obstacle Challenge](../software/obstacle_challenge/obstacle_challenge.py)

## Runtime and platform

The programs target LEGO EV3 using Pybricks MicroPython. The Obstacle Challenge program additionally imports the Pixy2 EV3 library and communicates with the camera over I²C.

## Software architecture

| Module responsibility | Open Challenge | Obstacle Challenge |
|---|---|---|
| Motor initialization | Yes | Yes |
| Gyro calibration | Yes | Yes |
| Ultrasonic acquisition | Yes | Yes |
| Corridor centering | Yes | Yes |
| Corner detection | Yes | Yes |
| Lap counting | Yes | Yes |
| Pixy2 block acquisition | No | Yes |
| Pillar classification | No | Yes |
| Passing-side selection | No | Yes |
| Parking sequence | No | Yes |

## Development rules

1. Preserve the supplied reference programs.
2. Develop experimental changes in separate files or branches.
3. Keep hardware ports and sign conventions documented.
4. Record parameter changes and their engineering rationale.
5. Run syntax checks before deployment.
6. Perform low-speed hardware tests after any control change.
7. Archive logs and compare them against the previous reference.

## Validation

A GitHub Actions workflow checks Python syntax and runs the analytical parameter-sweep script. This does not replace testing on the EV3 hardware.

## File naming

Use descriptive names and explicit revisions, for example:
- `open_challenge_v02.py`
- `obstacle_challenge_camera_test.py`
- `steering_calibration.py`

Do not overwrite a known reference version with an experimental build.
