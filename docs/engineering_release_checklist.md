# Engineering Release Checklist

We use this checklist to review the project files before sharing a version of our work. It helps us check that the main design details are documented and that calculations are not confused with physical test results.

## Documentation

- Use clear titles and the same names for parts throughout the repository.
- Include units with numerical values.
- Explain variables used in equations.
- State where a value comes from, such as a program setting, calculation, datasheet, or physical measurement.
- Include the relevant revision when a result depends on a particular version.

## Mechanical design

Our mechanical notes should explain the chassis reference points, wheel alignment, drive motor mounting, steering support and linkage, battery mounting, sensor positions, printed-part geometry, fasteners, and access for maintenance.

## Electrical design

Our electrical notes should show the EV3 port allocation, connectors, cable routing, clearance around moving parts, component operating limits, sensor communication, and power behaviour while the motors are running.

## Software

Before sharing the programs, we check Python syntax and imports, sensor startup, calibration, steering direction and limits, motor command limits, mission-state changes, timeout handling, fault handling, and event logging.

## Physical test records

For a physical test, we record:
- Test ID and date.
- Hardware and software versions.
- Conditions during the test.
- How the measurement was taken.
- The instrument used.
- Raw observations.
- The acceptance criteria.
- The result and related logs.

## How we describe evidence

The [Verification Evidence](verification_evidence.md) page explains the automated checks and calculations in this repository. We keep these separate from measurements made on the physical robot. A calculation or software check should not be described as a successful physical test.