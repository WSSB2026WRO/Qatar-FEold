# Obstacle Challenge — How the Detection and Control Work

## From camera reading to passing a pillar

| Step | What goes in | What the program does |
|---|---|---|
| Read camera | Pixy2 blocks | Reads the signature and bounding box |
| Check shape | Width, height, and ratio | Removes candidates that do not fit the filters |
| Confirm over time | Repeated frames | Checks that the detection stays stable |
| Identify colour | Signature ID | Selects red or green |
| Estimate position | Image x/y and calibration constants | Estimates bearing and range |
| Update pillar position | Robot distance and heading | Estimates where the pillar is relative to the route |
| Choose passing action | Pillar colour and position | Selects the passing side and lane target |
| Check clearance | Travel since estimated pillar position | Returns to the centre state when clear |

## Which side we pass

- Red signature 1: pass on the right.
- Green signature 2: pass on the left.

The lane controller calculates a target while staying within the corridor boundaries. If the pillar disappears from the camera for a short time, the program keeps its last estimated position. It waits for the configured clearance margin before returning to the centre state.

## Image range equation

The source uses:

`d = Y_K / (y - Y_0)`

Here, `y` is the vertical image coordinate, while `Y_0` and `Y_K` are configured model constants. The numerical example in the repository is a calculated reference table, not a set of real camera observations.

## Parking

The program saves the movements used to leave the parking area and later runs them in reverse order. It also uses changes in wall readings to improve the parking-area estimate. This depends on encoder distance, steering geometry, grip, and gyro heading being repeatable.

## What evidence is available

These notes describe the settings and logic in our Python program. The repository does not contain physical Pixy2 calibration readings or completed mission logs, so we do not report camera accuracy or full-mission performance as measured results.