# Repository Engineering Status — 11 November 2026

## Scope

This record summarizes the repository-level engineering review and distinguishes completed software/documentation work from tasks that require the assembled vehicle, instruments, or original CAD models.

## Completed repository work

- Corrected malformed mathematical notation and Markdown equation delimiters in the vehicle-dynamics, reference-design, control-system, and Pixy2 geometry documents.
- Clarified that the Pixy2 range table is a calculated reference dataset, not a physical camera calibration log.
- Aligned port-D documentation with the source files: the drawing register lists a front LED lamp, but neither current challenge program configures or controls a device on port D.
- Updated the Obstacle Challenge source comment so its two range-model anchors are not presented as a complete physical calibration record.
- Added standard-library unit tests for the analytical reference-vehicle calculation.
- Extended GitHub Actions to run the unit tests before generating the analytical parameter-sweep artifact.

## Automated verification

The recorded full GitHub Actions verification run below completed successfully on 11 November 2026:

- [Python Validation — run #153, successful](https://github.com/WSSB2026WRO/Qatar-FE/actions/runs/43076407683)
- Commit: `e8df0173e62e590f069ea6b69e32df2440a67bd4`
- Challenge source syntax compilation: passed for Open Challenge and Obstacle Challenge.
- Analytical model unit tests and documentation integrity tests (8 tests): passed.
- Analytical parameter sweep: passed and generated the 30-case CSV artifact.

These checks establish source syntax validity and repeatability of the repository's analytical calculation. They do not establish runtime behaviour on the EV3 or physical vehicle performance.

## Open physical and manufacturing release gates

| ID | Required work | Evidence required before closure |
|---|---|---|
| HW-01 | Confirm whether the front LED lamp is physically installed and connected to port D | Inspection of the assembled robot and an updated verified wiring record |
| CAL-01 | Calibrate the Pixy2 range model in its final mount | Raw image coordinates at independently measured target distances, fitted constants, residuals, and dated test record |
| CAL-02 | Calibrate gyro, ultrasonic sensors, drive distance scale, and steering mapping | Raw observations, instrument details, repeatability results, and accepted tolerances |
| VAL-01–10 | Execute the subsystem and mission validation matrix | Completed test reports and original logs for each executed test |
| CAD-01 | Add the three referenced STL files and confirm their unit convention and original CAD geometry | Original mesh files, native CAD source, unit declaration, dimensions, and mating-interface review |
| CAD-02 | Resolve the four-component topology of C3DP-02 | CAD inspection and a manufacturing-intent revision if the design requires a single solid |
| CAD-03 | Release fabrication drawings | Controlled CAD-derived drawings with datums, dimensions, tolerances, material, revision, and approval |
| SYS-01 | Complete full-vehicle regression on the competition hardware | Repeated mission logs, obstacle-clearance evidence, corner/lap counts, and parking results |
| MEDIA-01 | Add demonstration videos if recordings are available | Committed video files with challenge, date, software revision, and context |

## Evidence rules

- **Measured** means obtained from a physical instrument or robot log, with date, method, and configuration.
- **Calculated** means derived from stated equations and inputs.
- **Simulated** means produced by an explicit computational model.
- **Configured** means read from the current source or controller settings.
- **Assumed** means provisional and awaiting confirmation.

Do not mark an open physical or manufacturing gate as complete using an analytical estimate, a source-code constant, a drawing, or a generated example dataset.

## Release statement

The repository's documentation corrections, analytical unit tests, and automated software checks are complete for the recorded revision. Physical validation, original STL/CAD asset availability, final CAD confirmation, demonstration media, and manufacturing release remain open until the evidence listed above is collected from the actual vehicle and its controlled design files.
