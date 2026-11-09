# Sensor Calibration Procedures

## Gyro sensor

1. Place the vehicle on a stable, level surface.
2. Ensure the chassis is stationary and steering is not being moved.
3. Run the program's stationary drift measurement.
4. Record raw drift, accepted drift, calibration duration, and temperature if available.
5. Rotate the vehicle clockwise and counter-clockwise by a known angle to confirm sign and scale.
6. Repeat the test after remounting the sensor.

Acceptance criteria must be defined from measured repeatability and the steering error budget.

## Ultrasonic sensors

1. Measure sensor-face separation and mounting height.
2. Place a flat target at known distances.
3. Record at least ten samples per distance and orientation.
4. Repeat with oblique target angles and near wall edges.
5. Calculate median error, spread, and invalid-reading rate.
6. Confirm left/right orientation and sensor-to-wall geometry.

Do not assume the ultrasonic sensor reports perpendicular distance when the vehicle is angled relative to the wall.

## Pixy2 camera

1. Confirm firmware mode and I²C output.
2. Confirm the configured I²C address.
3. Set and verify red/green signatures using the competition lighting.
4. Record bounding-box coordinates at multiple known ranges.
5. Fit the vertical image-to-distance model and report residual error.
6. Calibrate horizontal field of view and optical-axis alignment.
7. Recheck after any camera mount or lighting change.

## Encoder distance

Measure a straight-line travel distance on the intended surface. Compare it with encoder-derived distance and repeat in both directions. Record wheel diameter, gear ratio, and any scale correction separately.
