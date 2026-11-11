# Sensor Calibration Procedures

This document defines repeatable procedures for collecting calibration evidence. A procedure is not evidence that calibration has already been performed. Record actual observations in a dated test record and retain the original log.

## 1. Gyroscope calibration

The vehicle must remain stationary during gyro calibration.

1. Place the vehicle on a level, vibration-free surface.
2. Ensure the steering and drive motors are idle.
3. Run the program's stationary drift measurement.
4. Complete the configured calibration sequence.
5. Record the initial heading, final heading, elapsed time, and calculated drift rate.
6. Confirm that the reported heading remains stable while the vehicle is stationary.
7. Repeat the check after any sensor remount or chassis modification.

For a stationary interval, calculate the average drift rate as:

`drift rate = (final heading - initial heading) / elapsed time`

State the angle and time units used (for example, degrees per second). Do not substitute a target or expected value for an observed result.

## 2. Ultrasonic range calibration

1. Align the sensor face perpendicular to a flat target.
2. Place the target at independently measured reference distances across the intended operating range.
3. Record the raw sensor reading at each position.
4. Repeat each point at least five times where practical to evaluate repeatability.
5. Calculate signed error (reading minus reference), absolute error, and mean error.
6. Inspect mounting angle, target geometry, and nearby reflective surfaces if the error is inconsistent.

Keep the reference distance, instrument used, test surface, sensor mounting configuration, and raw readings with the results.

## 3. Encoder distance calibration

For wheel diameter `D` in millimetres, motor rotation `theta` in degrees, and `G` defined as wheel revolutions per motor revolution:

`s = (theta / 360) × pi × D × G`

The calculated distance `s` is in millimetres. If the drivetrain ratio is documented as motor revolutions per wheel revolution, convert it to the reciprocal before using this expression.

Measure a straight-line travel distance on the intended surface and compare it with the encoder-derived distance. Repeat in both directions and evaluate the influence of wheel slip, backlash, tyre deformation, and drivetrain compliance. Record the wheel diameter and gear ratio used in the calculation.

## 4. Pixy2 range calibration

The Obstacle Challenge program uses the configured empirical vertical-image model:

`d = 20100 / (Y - 63)`

where `Y` is the selected vertical image feature in pixels and `d` is the estimated range in millimetres. The constants 20100 and 63 are configured model parameters, not proof of a completed physical calibration.

To validate the model, collect multiple observations at known target distances, retain the raw image coordinate for each observation, calculate predicted range and residual, and evaluate the error across the intended operating range. Document target dimensions, camera mounting position, image resolution, lighting, and the method used to identify the image feature.

The model and its geometric limitations are discussed in [Pixy2 Calibration and Geometry](../engineering/perception/pixy2_calibration_and_geometry.md).

## 5. Calibration record format

| Sensor | Reference condition | Observed value | Error / metric | Notes |
|---|---|---|---|---|
| Gyro | Stationary, timed interval | Initial/final heading | Drift rate | Record duration and repeat count |
| Ultrasonic left | Known target distance | Raw sensor reading | Reading − reference | Record target and instrument |
| Ultrasonic right | Known target distance | Raw sensor reading | Reading − reference | Record target and instrument |
| Drive encoder | Known travel distance | Encoder-derived distance | Calculated − reference | Record wheel diameter and ratio |
| Pixy2 | Known pillar range | Image coordinate and predicted range | Predicted − reference | Record camera and lighting setup |

## 6. Evidence and revision control

Each calibration session should include:

- Test ID, date, operator, and robot identifier.
- Hardware configuration and mounting revision.
- Software file name, version, and commit identifier.
- Reference instrument and its resolution or stated accuracy.
- Raw observations, units, repeat count, and environmental conditions.
- Calculation method, summary statistics, limitations, and reviewer.
- Original unedited log or data file.

Classify every result as **measured**, **calculated**, **configured**, or **inconclusive**. Never describe an unperformed procedure as a completed calibration.
