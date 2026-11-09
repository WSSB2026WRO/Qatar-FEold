# Obstacle Management

## System purpose

Obstacle Management documents the perception and manoeuvring functions used by the Obstacle Challenge program. The system identifies coloured pillars, estimates their position relative to the vehicle, selects a passing side, tracks clearance, and returns to corridor following.

Reference material:
- [Obstacle Challenge source](../software/obstacle_challenge/obstacle_challenge.py)
- [Obstacle Challenge technical documentation](../software/obstacle_challenge/README.md)
- [Pixy2 calibration and geometry](../engineering/perception/pixy2_calibration_and_geometry.md)
- [Obstacle state machine](../engineering/diagrams/obstacle_state_machine.svg)

## Perception hardware

| Interface | Device | Role |
|---|---|---|
| Sensor S4 | Pixy2 camera | Colour-signature block detection |
| I²C address | 0x54 | Camera communication |
| Signature 1 | Red | Red pillar class |
| Signature 2 | Green | Green pillar class |

## Passing policy

| Pillar class | Configured passing side |
|---|---|
| Red | Right |
| Green | Left |

The program filters detections by signature, block height, and block aspect ratio. A candidate must persist for a configured number of frames before it is accepted.

## Obstacle tracking sequence

1. Acquire Pixy2 blocks.
2. Reject blocks that do not meet the configured geometric filters.
3. Select the nearest candidate using its image position.
4. Confirm the candidate over consecutive frames.
5. Estimate range and lateral position.
6. Select the lane target required for the passing side.
7. Retain the estimated pillar position if the pillar temporarily leaves the camera view.
8. Confirm that the vehicle has cleared the pillar by the configured passing margin.
9. Return to the centre-lane target.

## Image-based range model

The supplied program uses:

`distance_{mm}=\frac{20100}{Y-63}`

where (Y) is the selected vertical image coordinate in pixels. This is an empirical model and depends on camera mounting and calibration. See the dedicated calibration document for the model, example calculations, and required measurement procedure.

## Safety and failure handling

- Consecutive camera communication errors are counted.
- Candidate detections require temporal confirmation.
- Wall-distance plausibility checks support lane positioning.
- Steering is bounded by the configured actuator limit.
- The global mission timeout remains active.

## Validation checklist

- [ ] Verify Pixy2 firmware and I²C output mode.
- [ ] Verify signature IDs in the final camera configuration.
- [ ] Confirm camera mounting angle and field of view.
- [ ] Calibrate range at multiple known distances.
- [ ] Test red-pillar passing independently.
- [ ] Test green-pillar passing independently.
- [ ] Confirm transition from AVOID to PASS and back to CENTER.
- [ ] Test obstacle detection near corridor openings.
- [ ] Record missed detections and false detections.

Do not classify a perception model as calibrated until the image coordinates have been recorded from the installed camera at known distances.
