# Sensor Calibration Procedures

## 1. Gyroscope calibration

The vehicle must remain stationary during gyro calibration.

1. Place the vehicle on a level, vibration-free surface.
2. Ensure the steering and drive motors are idle.
3. Run the program's stationary drift measurement.
4. Complete the configured calibration sequence.
5. Confirm that the reported heading remains stable while the vehicle is stationary.
6. Repeat the check after any sensor remount or chassis modification.

## 2. Ultrasonic range calibration

1. Align the sensor face perpendicular to a flat target.
2. Place the target at known distances across the operating range.
3. Record the sensor reading at each position.
4. Repeat each point to evaluate repeatability.
5. Compare the reading against the reference distance.
6. Inspect mounting angle and nearby reflective surfaces if the error is inconsistent.

## 3. Encoder distance calibration

For wheel diameter (D), motor rotation (	heta) in degrees, and gear ratio (G):

\[
s=\frac{\theta}{360^\circ}\,\pi D\,G
\]

Measure a straight-line travel distance on the intended surface and compare it with the encoder-derived distance. Repeat in both directions and evaluate the influence of wheel slip and drivetrain compliance.

## 4. Pixy2 range calibration

The Obstacle Challenge program uses the empirical vertical-image model:

\[
d=\frac{20100}{Y-63}
\]

where (Y) is the selected vertical image feature in pixels and (d) is the estimated range in millimetres. The calibration procedure and numerical model analysis are documented in [Pixy2 Calibration and Geometry](../engineering/perception/pixy2_calibration_and_geometry.md).

## 5. Calibration record format

| Sensor | Reference condition | Observed value | Error | Notes |
|---|---|---|---|---|
| Gyro | Stationary | Drift rate | — | Heading stability |
| Ultrasonic left | Known target distance | Sensor reading | Reading − reference | Repeatability |
| Ultrasonic right | Known target distance | Sensor reading | Reading − reference | Repeatability |
| Drive encoder | Known travel distance | Calculated distance | Calculated − reference | Wheel slip |
| Pixy2 | Known pillar range | Image coordinate | Range-model residual | Camera geometry |
