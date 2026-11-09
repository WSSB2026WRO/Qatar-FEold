# Qatar FE — WRO Future Engineers

<p align="center">
  <strong>Autonomous Robotics Engineering Portfolio</strong><br>
  <em>Mechanical Design · Embedded Control · Perception · Vehicle Dynamics · Additive Manufacturing</em>
</p>

---

## Project overview

Qatar FE is a student engineering team developing an autonomous vehicle for the **World Robot Olympiad (WRO) Future Engineers** challenge. This repository is the team's technical record: it documents the system architecture, mechanical concepts, embedded software, sensing strategy, control methods, custom components, engineering calculations, and validation work for both competition formats.

The repository separates the two challenge programs:

- **Open Challenge** — autonomous corridor following, wall-based centering, corner detection, heading control, lap tracking, and return to the start section.
- **Obstacle Challenge** — the Open Challenge navigation foundation extended with visual pillar classification, colour-dependent passing strategy, obstacle tracking, lane repositioning, and a parking sequence.

The software supplied for documentation targets a LEGO EV3 platform running Pybricks MicroPython. The Obstacle Challenge program also uses a Pixy2 camera through the `pixycamev3` library.

## Team

| Member | Responsibility |
|---|---|
| Omar | Lead Programmer |
| Eissa | Team Leader / Chief of Team |
| Mohammed | Lead Designer |

## Repository map

| Area | Contents |
|---|---|
| [Software](software/) | Challenge source code, program notes, algorithm documentation |
| [Hardware](hardware/) | EV3 configuration, sensors, actuators, custom 3D-printed parts |
| [Engineering](engineering/) | Mechanical design, vehicle dynamics, system architecture, calculations |
| [Validation](validation/) | Test procedures, calibration records, data-log interpretation |
| [Media](media/) | Team-approved photographs, diagrams, and technical illustrations |

## System at a glance

| Subsystem | Open Challenge | Obstacle Challenge |
|---|---|---|
| Controller | LEGO EV3 | LEGO EV3 |
| Drive | Two medium motors, ports A and B | Two medium motors, ports A and B |
| Steering | Medium motor, port C | Medium motor, port C |
| Heading | Gyro, port S1 | Gyro, port S1 |
| Left/right ranging | Ultrasonic sensors, S2 and S3 | Ultrasonic sensors, S2 and S3 |
| Vision | Not used by the supplied program | Pixy2 on S4, I²C address 0x54 |
| Main navigation reference | Wall geometry + gyro + encoders | Wall geometry + gyro + encoders |
| Additional task | Three-lap route and start return | Pillar passing, three-lap route and parking |

## Engineering approach

The project is organized around traceable engineering decisions:

1. **Define the operating task** and the constraints of each challenge.
2. **Map the hardware** and document each device's role and interface.
3. **Explain the control architecture** from sensor acquisition to actuator commands.
4. **Expose tunable parameters** with units, purpose, and calibration method.
5. **Separate measured values from assumptions** and conceptual design studies.
6. **Validate incrementally** using repeatable tests and recorded data.
7. **Preserve source history** so experimental changes do not overwrite known reference programs.

## Important interpretation notes

- The checked-in source programs are the reference versions supplied for this repository. Their presence does not, by itself, prove a particular competition result or physical test outcome.
- Values copied from source code are identified as **configured parameters**, not as independently verified measurements.
- Conceptual engineering studies may explore designs beyond the currently documented physical build. They are labelled accordingly.
- The STL files are retained as supplied design artifacts. Their mesh dimensions are not assigned physical units unless the CAD/export convention is confirmed.
- No performance claim should be made without a corresponding test record.

## Quick navigation

- [Software overview](software/README.md)
- [Open Challenge documentation](software/open_challenge/README.md) · [Algorithm notes](software/open_challenge/algorithm_notes.md)
- [Obstacle Challenge documentation](software/obstacle_challenge/README.md) · [Algorithm notes](software/obstacle_challenge/algorithm_notes.md)
- [Hardware architecture](hardware/README.md) · [Sensor calibration](hardware/sensor_calibration.md)
- [Custom 3D-printed parts](hardware/custom_3d_printed_parts/README.md) · [Mesh inspection](hardware/custom_3d_printed_parts/mesh_inspection_report.md)
- [Engineering studies](engineering/README.md) · [Mass distribution](engineering/mechanical_design/mass_distribution_and_vehicle_dynamics.md) · [Steering geometry](engineering/mechanical_design/steering_geometry.md)
- [3D printing guidelines](engineering/mechanical_design/3d_printing_design_guidelines.md) · [Risk assessment](engineering/risk_assessment.md)
- [Validation plan](validation/README.md) · [Test report template](validation/test_report_template.md)

## Development status

The repository is being populated from the team's supplied source programs and CAD exports. Test logs, verified dimensions, material specifications, CAD source files, and approved team photographs should be added as they become available.

---

**Qatar FE — WRO Future Engineers**
