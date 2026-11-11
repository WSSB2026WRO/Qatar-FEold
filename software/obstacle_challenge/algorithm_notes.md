# Obstacle Challenge — Perception and Control Notes

## Perception state pipeline

| Stage | Input | Decision |
|---|---|---|
| Acquisition | Pixy2 blocks | Read signature and bounding box |
| Geometric filter | Width, height, ratio | Reject weak candidates |
| Temporal confirmation | Repeated frames | Confirm stable detection |
| Classification | Signature ID | Red or green |
| Ground projection | Image x/y, calibration constants | Estimate bearing and range |
| Track update | Vehicle odometry and heading | Estimate pillar position relative to route |
| Avoidance state | Pillar colour and position | Select passing side and lane target |
| Clearance check | Travel since estimated pillar position | Return to centre state |

## Pillar passing policy

- Red signature 1: pass on the right.
- Green signature 2: pass on the left.

The lane controller computes a lateral target while respecting corridor boundaries. The controller retains a pillar estimate when the object temporarily leaves the camera field of view and waits for a configured clearance margin before returning to the centre state.

## Image range model

The source uses `d = Y_K / (y - Y_0)`, where `y` is the vertical image coordinate and `Y_0` and `Y_K` are configured model constants. The repository's numerical example is a calculated reference dataset; it is not a record of physical camera observations.

## Parking strategy

The program records the unparking movements and later executes a reverse sequence. The parking-lot estimate is refined using detected wall transitions. The strategy depends on repeatability of encoder distance, steering geometry, traction, and gyro heading.

## Evidence status

The notes describe the configured perception and control logic. The repository does not contain physical Pixy2 calibration observations or completed mission logs, so camera accuracy and full-mission performance are not stated as measured results.
