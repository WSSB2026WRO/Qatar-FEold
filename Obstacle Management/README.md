# Obstacle Management

## What this section covers

In the Obstacle Challenge, our robot has to detect coloured pillars, choose the correct side to pass, and then return to following the corridor. This page describes the camera setup and the steps used by our obstacle program.

Main project files:
- [Obstacle Challenge program](../software/obstacle_challenge/obstacle_challenge.py)
- [Obstacle Challenge notes](../software/obstacle_challenge/README.md)
- [Pixy2 calibration and geometry](../engineering/perception/pixy2_calibration_and_geometry.md)
- [Obstacle state machine diagram](../engineering/diagrams/obstacle_state_machine.svg)

## Camera setup

| Interface | Device or setting | Purpose |
|---|---|---|
| Sensor S4 | Pixy2 camera | Detecting coloured blocks |
| I²C address | 0x54 | Camera communication |
| Signature 1 | Red | Red pillar |
| Signature 2 | Green | Green pillar |

## Which side do we pass?

| Pillar colour | Configured passing side |
|---|---|
| Red | Right |
| Green | Left |

The program checks the detected signature, block height, and block shape. A detection must remain present for the configured number of frames before the program accepts it. This helps avoid reacting to a single incorrect camera reading.

## Steps used by the program

1. Read the blocks detected by the Pixy2.
2. Ignore blocks that do not match the configured size and shape checks.
3. Choose the closest suitable candidate using its image position.
4. Check the candidate over several frames.
5. Estimate its distance and position relative to the vehicle.
6. Set the lane target for the required passing side.
7. Keep the last estimated position for a short time if the pillar disappears from the camera view.
8. Check that the vehicle has passed the pillar by the configured margin.
9. Set the target back to the centre of the lane.

## Estimating distance from the image

The program uses this empirical model:

`distance_mm = 20100 / (Y - 63)`

Here, `Y` is the selected vertical image coordinate in pixels. The result depends on the camera position and calibration. The equation is part of the configured model; it should not be treated as a new physical measurement. The calibration page explains the model and the measurements still needed to check it on the vehicle.

## Checks and failure handling

The program counts repeated camera communication errors, confirms detections over time, checks whether wall readings are reasonable, and limits the steering command. The overall mission timeout also remains active.

Before relying on the obstacle behaviour, we still need to check the following on the assembled vehicle:

- [ ] Check the Pixy2 firmware and I²C output mode.
- [ ] Check the signature IDs in the camera configuration.
- [ ] Check the camera angle and field of view.
- [ ] Compare the range estimate with several known distances.
- [ ] Test passing a red pillar on its own.
- [ ] Test passing a green pillar on its own.
- [ ] Check the AVOID, PASS, and CENTER state changes.
- [ ] Check detections near corridor openings.
- [ ] Record missed detections and false detections.