# Verification and Validation Framework

## Purpose

This document defines the verification framework associated with the Qatar FE autonomous vehicle and its Open Challenge and Obstacle Challenge programs.

## Verification coverage

| ID | Subsystem | Defined evidence type |
|---|---|---|
| V-01 | Drive | Encoder distance compared with measured travel |
| V-02 | Steering | Commanded wheel angle, observed angle, repeatability and backlash |
| V-03 | Gyro | Stationary drift and calibration observations |
| V-04 | Ultrasonic sensors | Readings compared with known target distances |
| V-05 | Corridor control | Vehicle path relative to the corridor envelope |
| V-06 | Corner control | Heading response and corner execution |
| V-07 | Pixy2 | Red/green signature classification and detection records |
| V-08 | Obstacle avoidance | Passing-side decision and clearance observations |
| V-09 | Parking | Final vehicle position and orientation |
| V-10 | Logging | CSV fields and mission event records |

## Evidence status

The repository includes the verification framework and the engineering test-record format. No completed physical test reports or raw EV3 mission logs are stored in this repository snapshot. The automated GitHub Actions results and analytical model outputs are recorded separately in [Verification Evidence](../docs/verification_evidence.md).

## Safety context

The validation framework accounts for rotating wheels, steering linkages, moving mechanisms, electrical connections, sensor faults, and abnormal vehicle behaviour. Safety controls are part of the test context and are distinct from performance results.

## Result terminology

- **Pass:** the recorded observations satisfy the stated acceptance criteria.
- **Fail:** one or more acceptance criteria are not satisfied.
- **Inconclusive:** the recorded conditions or observations do not support a decision.
