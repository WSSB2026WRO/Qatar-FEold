# Sensor Calibration Procedures

This page explains how we can collect calibration evidence. A procedure does not mean that we have already completed the calibration. When we carry out a check, we need to save the actual readings in a dated test record and keep the original log.

## 1. Gyro calibration

The robot must stay still while we calibrate the gyro.

1. Put the robot on a level surface where it will not vibrate.
2. Make sure the drive and steering motors are not moving.
3. Run the stationary drift measurement in the program.
4. Complete the configured calibration sequence.
5. Record the starting heading, ending heading, elapsed time, and calculated drift rate.
6. Check that the heading stays stable while the robot remains still.
7. Repeat the check after moving the sensor or changing the chassis.

For a stationary time interval, we calculate the average drift rate as:

`drift rate = (final heading - initial heading) / elapsed time`

Write down the angle and time units, for example degrees per second. Do not write an expected value as if it were an observed result.

## 2. Ultrasonic range calibration

1. Point the sensor face directly at a flat target.
2. Put the target at reference distances measured independently.
3. Record the raw sensor reading at each distance.
4. Repeat each point at least five times when practical.
5. Calculate signed error (reading minus reference), absolute error, and mean error.
6. If the readings vary, check the sensor angle, target shape, and nearby reflective surfaces.

Keep the reference distance, measuring instrument, test surface, sensor mounting setup, and raw readings with the results.

## 3. Encoder distance calibration

For wheel diameter `D` in millimetres, motor rotation `theta` in degrees, and `G` defined as wheel revolutions per motor revolution:

`s = (theta / 360) × pi × D × G`

The result `s` is in millimetres. If the drivetrain ratio is written as motor revolutions per wheel revolution, convert it to the reciprocal before using this formula.

Measure a straight-line distance on the surface used for the robot and compare it with the encoder estimate. Repeat in both directions. We should consider wheel slip, backlash, tyre deformation, and drivetrain flexibility. Record the wheel diameter and gear ratio used.

## 4. Pixy2 range calibration

In the Obstacle Challenge, the Pixy2 camera assembly, including its built-in illumination, is connected to sensor port S4. The program uses this empirical model based on the vertical image coordinate:

`d = 20100 / (Y - 63)`

Here, `Y` is the selected vertical image feature in pixels and `d` is the estimated range in millimetres. The constants 20100 and 63 are configured model values. They do not prove that we have completed a physical camera calibration.

To check the model, we need to record images at several known distances, save the raw image coordinates, calculate the predicted range and error, and review the error over the intended operating range. We should also record the pillar size, camera position, image resolution, lighting, and the method used to select the image feature.

The model and its limitations are explained in [Pixy2 Calibration and Geometry](../engineering/perception/pixy2_calibration_and_geometry.md).

## 5. Calibration record table

| Sensor | Reference condition | What we record | Error or metric | Notes |
|---|---|---|---|---|
| Gyro | Stationary for a timed interval | Starting and ending heading | Drift rate | Record duration and repeat count |
| Ultrasonic left | Target at known distance | Raw sensor reading | Reading − reference | Record target and instrument |
| Ultrasonic right | Target at known distance | Raw sensor reading | Reading − reference | Record target and instrument |
| Drive encoder | Known travel distance | Encoder distance estimate | Calculated − reference | Record wheel diameter and ratio |
| Pixy2 | Pillar at known range | Image coordinate and predicted range | Predicted − reference | Record camera and lighting setup |

## 6. Saving the evidence

For each calibration session, we should save:

- Test ID, date, operator, and robot identifier.
- Hardware setup and mounting revision.
- Software file name, version, and commit.
- Reference instrument and its resolution or stated accuracy.
- Raw readings, units, number of repeats, and test conditions.
- Calculation method, summary statistics, limitations, and reviewer.
- Original log or data file without edits.

Each result should be labelled **measured**, **calculated**, **configured**, or **inconclusive**. We should never describe a procedure as a completed calibration if we have not carried it out.