# Engineering Release Standard

## Documentation standard

Every engineering document uses a descriptive title, consistent terminology, SI units, defined variables, and a clear revision history. Numerical values are accompanied by their units and calculation basis.

## Mechanical release

A mechanical assembly is reviewed for:
- chassis datum and wheel alignment;
- drive motor mounting stiffness;
- steering actuator support and linkage clearance;
- battery retention and service access;
- sensor bracket rigidity and field of view;
- printed-part geometry, material, and manufacturing orientation;
- fastener retention and inspection access.

## Electrical release

The electrical architecture is reviewed for:
- verified EV3 port allocation;
- connector security and cable strain relief;
- moving-part clearance;
- battery and motor operating limits;
- sensor communication integrity;
- power stability during simultaneous drive and steering operation.

## Software release

A software revision is reviewed for:
- Python syntax and import integrity;
- sensor initialization and calibration sequence;
- steering sign conventions and mechanical limits;
- bounded actuator commands;
- mission-state transitions;
- timeout and fault handling;
- logging fields and event traceability;
- regression comparison against the reference version.

## Validation release

A validation record contains:
- test objective and identifier;
- hardware and software revision;
- operating conditions;
- measurement method and instrument;
- raw observations;
- acceptance criteria;
- pass, fail, or inconclusive result;
- corrective actions and regression outcome.

## Evidence management

Retain original logs and measurement records. Store derived plots and calculations separately with the source record, processing method, and software revision identified.
