# Verification and Validation

## Why we keep these records

We use this folder to plan checks for our EV3 robot and its Open Challenge and Obstacle Challenge programs. It helps us decide what to measure and what evidence to save.

## Checks we have planned

| ID | Part of the robot | Evidence to collect |
|---|---|---|
| V-01 | Drive | Compare encoder distance with measured travel |
| V-02 | Steering | Commanded and observed wheel angle, repeatability, and backlash |
| V-03 | Gyro | Stationary drift and calibration readings |
| V-04 | Ultrasonic sensors | Compare readings with known target distances |
| V-05 | Corridor control | Compare the robot path with the corridor boundaries |
| V-06 | Corner control | Record heading response and corner movement |
| V-07 | Pixy2 | Save red/green signature detections |
| V-08 | Obstacle avoidance | Record passing-side decisions and clearance |
| V-09 | Parking | Measure final robot position and direction |
| V-10 | Logging | Check CSV fields and mission event records |

## Evidence currently in the repository

We have included the verification plan and a test-record format. The current repository snapshot does not contain completed physical test reports or raw EV3 mission logs.

The GitHub Actions results and analytical model calculations are recorded separately in [Verification Evidence](../docs/verification_evidence.md).

## Safety during checks

When we test the robot, we need to consider the rotating wheels, steering links, moving parts, electrical connections, sensor faults, and unexpected movement. Safety checks are part of the test setup; they are not performance results.

## How we label a result

- **Pass:** the recorded observations meet the acceptance criteria written before the test.
- **Fail:** at least one acceptance criterion is not met.
- **Inconclusive:** the observations or test conditions are not enough to make a decision.