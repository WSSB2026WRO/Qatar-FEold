# Verification and Validation Plan

## Purpose

This plan defines repeatable checks for the Open Challenge and Obstacle Challenge programs. It is a proposed validation framework; no test is marked as passed until a dated record and supporting evidence are added.

## Test matrix

| ID | Subsystem | Test | Evidence |
|---|---|---|---|
| V-01 | Drive | Compare encoder distance with a measured straight run | Raw distance table |
| V-02 | Steering | Verify zero, left/right sign, and repeatability | Angle readings and video |
| V-03 | Gyro | Measure stationary drift over the configured interval | Drift log |
| V-04 | Ultrasonic | Compare readings with known distances and wall angles | Range table |
| V-05 | Open navigation | Test centering at low, medium, and high speeds | CSV logs |
| V-06 | Corner control | Repeat left and right 90-degree turns | Heading traces |
| V-07 | Start return | Compare calculated stop position with start reference | Position error |
| V-08 | Pixy2 | Confirm red/green signatures and stable acquisition | Image/frame record |
| V-09 | Pillar ranging | Compare image-based range estimate with measured range | Calibration dataset |
| V-10 | Obstacle passing | Test red-right and green-left passing separately | Video and clearance record |
| V-11 | Parking | Repeat unpark and reverse-replay parking | Final pose measurements |
| V-12 | Endurance | Run repeated missions under controlled battery conditions | Run summary and logs |

## Test record template

For every test, record:
- Test ID and objective
- Software version and source hash
- Hardware configuration
- Date and venue
- Battery condition
- Surface and environmental conditions
- Parameter values
- Procedure
- Raw observations
- Acceptance criterion
- Result: Pass / Fail / Inconclusive
- Deviations and corrective action

## Safety

- Raise or support driven wheels during initial polarity checks.
- Keep hands clear of steering linkages and rotating wheels.
- Begin tuning at reduced speed.
- Keep a clear emergency-stop path.
- Stop testing if a cable, sensor, or printed part becomes loose or damaged.
- Do not run autonomous tests near people or fragile objects.

## Data handling

Keep raw CSV logs unchanged. Derived plots and analysis should be stored separately and identify the source log, script version, and processing assumptions.
