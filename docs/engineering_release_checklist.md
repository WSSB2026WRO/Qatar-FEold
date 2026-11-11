# Engineering Release Criteria

## Documentation quality

Engineering records use descriptive titles, consistent terminology, SI units, defined variables, and revision context. Numerical values include units and a stated calculation or evidence basis.

## Mechanical design criteria

The mechanical design record covers chassis datums and wheel alignment, drive-motor mounting, steering-actuator support, linkage geometry, battery retention, sensor mounting, printed-part geometry, fastener retention, and service access.

## Electrical design criteria

The electrical record covers EV3 port allocation, connector interfaces, cable routing, moving-part clearance, component operating limits, sensor communication, and power integrity during drive and steering operation.

## Software design criteria

The software record covers Python syntax and imports, sensor initialization, calibration sequence, steering sign conventions and limits, bounded actuator commands, mission-state transitions, timeout handling, fault response, and event logging.

## Verification evidence structure

A physical test record is defined by its test identifier, hardware and software revision, operating conditions, measurement method, instrument, raw observations, acceptance criteria, result classification, and associated logs.

## Evidence interpretation

The [Verification Evidence](verification_evidence.md) document records the automated checks and analytical calculations. Automated software checks and calculated outputs are distinguished from measurements obtained from the physical vehicle. The repository's evidence classification is used consistently across the portfolio and engineering documents.
