# Verification and Validation

## Purpose

This plan defines the verification activities for the Qatar FE autonomous vehicle and its two challenge programs.

**Current evidence status:** This directory contains the validation plan and report template. No completed physical test reports or raw robot logs are currently stored here. Test rows below are planned verification activities, not claims of completed tests.

## Test matrix

| ID | Subsystem | Verification method | Acceptance criterion |
|---|---|---|---|
| V-01 | Drive | Compare encoder distance with a measured straight run | Error remains within the project-defined distance tolerance |
| V-02 | Steering | Measure wheel angle at commanded positions | Monotonic response and repeatable left/right travel |
| V-03 | Gyro | Record stationary drift over the calibration interval | Drift remains within the configured acceptance threshold |
| V-04 | Ultrasonic | Compare readings with known target distances | Readings remain within the defined sensor tolerance |
| V-05 | Corridor control | Run repeated straight corridor trials | Vehicle remains inside the permitted corridor envelope |
| V-06 | Corner control | Execute left and right corner trials | Target heading reached without timeout |
| V-07 | Pixy2 | Verify red and green signature detection | Correct signature classification across repeated observations |
| V-08 | Obstacle avoidance | Run pillar-passing trials | Required passing side and clearance are maintained |
| V-09 | Parking | Repeat final parking manoeuvre | Vehicle stops within the defined parking region |
| V-10 | Logging | Inspect generated CSV records | Required fields and event records are present |

## Test procedure

Each test should define:
- test identifier and objective;
- software version;
- hardware configuration;
- environmental conditions;
- procedure and number of repetitions;
- acceptance criteria;
- recorded observations;
- final result and corrective actions.

## Safety

- Raise or support driven wheels during initial polarity checks.
- Keep hands clear of steering linkages and rotating wheels.
- Start at reduced speed after mechanical or software changes.
- Stop the run if sensor data become implausible or communication is lost.
- Inspect printed components and fasteners after impact or abnormal loading.

## Result classification

- **Pass:** all acceptance criteria are satisfied.
- **Fail:** one or more acceptance criteria are not satisfied.
- **Inconclusive:** the test conditions or observations do not support a decision.


