# Schemes and Engineering Drawings

This directory is the drawing index for the Qatar FE autonomous vehicle and its control system. It identifies the diagrams required to explain the vehicle architecture, analytical design basis, mechanisms, electrical interfaces, and camera geometry.

The register is an index, not a claim that every listed item is already available as a released manufacturing drawing. The currently linked SVG files are system-level or conceptual engineering diagrams. Mechanical fabrication drawings and dimensioned assembly drawings must be produced from the controlled CAD model before parts are manufactured.

## Available system diagrams

- [SYS-001 — System architecture](../engineering/diagrams/system_architecture.svg)
- [DYN-001 — Vehicle dynamics model](../engineering/diagrams/vehicle_dynamics_equations.svg)
- [STR-001 — Ackermann steering geometry](../engineering/diagrams/steering_ackermann.svg)
- [OBS-001 — Obstacle Challenge state machine](../engineering/diagrams/obstacle_state_machine.svg)

## Drawing register

| Drawing ID | Title | Drawing class | Intended use |
|---|---|---|---|
| SYS-001 | Autonomous vehicle system architecture | Functional block diagram | Shows the relationship between the EV3 controller, drive and steering actuators, sensors, perception input, and control functions. |
| DYN-001 | Vehicle dynamics free-body model | Analytical schematic | Defines the forces, dimensions, and reference axes used in the vehicle-dynamics calculations. It is an analysis aid, not a measured force diagram. |
| STR-001 | Ackermann steering geometry | Conceptual mechanism diagram | Explains the steering geometry and the intended relationship between inner- and outer-wheel steering angles. Confirm dimensions against the final CAD assembly. |
| OBS-001 | Obstacle Challenge state machine | Software flow diagram | Documents the high-level mission sequence, including navigation, obstacle passing, lap/corner handling, and parking states. The source program remains the executable reference. |
| MEC-001 | Chassis and component layout | Mechanical layout reference | Identifies the chassis envelope, component positions, mounting interfaces, service access, and sensor/actuator locations. Requires a dimensioned CAD-derived release drawing for fabrication. |
| MEC-002 | Steering linkage | Mechanism definition | Defines the steering motor interface, linkage pivots, steering arms, joints, and travel limits. Critical dimensions and clearances must be taken from the final assembled CAD model. |
| ELE-001 | EV3 wiring and port allocation | Electrical interface map | Records the connection between each EV3 port and its device. Use the verified physical wiring as the authority if the installed configuration changes. |
| CAM-001 | Pixy2 camera geometry | Sensor geometry reference | Defines camera orientation, field of view, mounting offset, image reference axis, and the geometry used to estimate obstacle position. Calibration values must be identified as configured, assumed, or measured. |

## Drawing descriptions and technical content

### SYS-001 — Autonomous vehicle system architecture

The diagram should show the main functional blocks and their interfaces:

- EV3 programmable controller and the two challenge-specific control programs.
- Drive motors on ports A and B.
- Steering motor on port C.
- Front LED illumination on port D.
- Gyro sensor on input S1.
- Left and right ultrasonic sensors on inputs S2 and S3.
- Pixy2 camera on input S4 through the I²C interface for the Obstacle Challenge.
- The information flow from sensing to state estimation, navigation decisions, steering/drive commands, and mission-state transitions.

The diagram is functional: it explains what is connected and how information or commands flow. It does not replace a wiring diagram, connector pinout, or physical assembly drawing.

### DYN-001 — Vehicle dynamics free-body model

The analytical schematic should identify the vehicle coordinate system and the forces used in the design calculations:

- Longitudinal, lateral, and vertical axes, with the positive directions stated.
- Vehicle mass and centre-of-gravity location.
- Wheelbase, track width, and wheel radius where relevant.
- Normal reactions at the wheels or axles.
- Longitudinal tyre force, lateral tyre force, gravity, and inertial loading.
- Dimensions and symbols used by the accompanying equations.

Every numerical input must be labelled by evidence type. For example, a value may be a design assumption or a calculated reference value; it must not be presented as a physical measurement unless a measurement record exists.

### STR-001 — Ackermann steering geometry

The diagram should identify the steering axis or pivot locations, wheelbase, front track, steering links, and inner/outer wheel angles. It should explain the intended Ackermann relationship during a turn and identify the reference point used for angle measurements.

The diagram is conceptual unless it includes controlled dimensions and tolerances. Do not infer final steering angles or linkage lengths from a schematic that is not dimensioned.

### OBS-001 — Obstacle Challenge state machine

The flow diagram should show the mission states and the conditions that cause transitions between them. It should cover, as applicable to the released program:

- Initialisation and sensor checks.
- Leaving the starting/parking position.
- Lane following and obstacle detection.
- Red- and green-pillar passing decisions.
- Corner detection and turn execution.
- Lap/corner counting and return-to-start logic.
- Final alignment and parking.
- Stop, timeout, and fault-handling paths.

State names and transition conditions should be checked against the current source code whenever the program changes. The diagram is explanatory documentation and is not a substitute for the Python program.

### MEC-001 — Chassis and component layout

The released mechanical layout should include top, side, and front views where needed. It should identify:

- Overall chassis envelope and the coordinate datum.
- Wheel locations, wheelbase, and track.
- EV3 brick and battery positions.
- Drive and steering motor mounting positions.
- Sensor and camera mounting positions and viewing directions.
- Cable routing, connector access, fasteners, and service clearances.
- The centre-of-gravity reference point when it is supported by a defined mass model.

A layout reference may communicate approximate packaging. Fabrication requires a separate dimensioned drawing or controlled CAD model with tolerances and manufacturing information.

### MEC-002 — Steering linkage

The mechanism drawing should identify each link and joint, pivot centres, steering arm interfaces, motor connection, fasteners, and permitted movement. Include dimensions that control steering response and mechanical clearance, plus any assembly constraints or adjustment procedure.

Check for interference across the complete steering range, not only in the straight-ahead position. Record the CAD revision used for the check. Any measured steering travel or backlash should be reported separately in the validation records.

### ELE-001 — EV3 wiring and port allocation

The interface map should record the device, EV3 port, signal/interface type, and function. The current documented allocation is:

| EV3 port | Device | Function / interface |
|---|---|---|
| A | Medium motor | Left drive motor |
| B | Medium motor | Right drive motor |
| C | Medium motor | Steering actuator |
| D | Front LED lamp | Camera illumination |
| S1 | Gyro sensor | Heading measurement |
| S2 | Ultrasonic sensor | Left-side distance measurement |
| S3 | Ultrasonic sensor | Right-side distance measurement |
| S4 | Pixy2 camera | I²C obstacle/pillar detection |

The Pixy2 interface is documented as I²C. The wiring drawing should show the actual cable/interface arrangement and should be checked against the assembled robot before release. Do not add connector pin numbers or electrical ratings unless they have been verified from the hardware documentation.

### CAM-001 — Pixy2 camera geometry

The geometry reference should show:

- Camera optical axis and mounting orientation.
- Image coordinate directions and the image reference point used by the software.
- Camera field of view and mounting height/offset.
- Forward offset between the camera reference and the vehicle reference point.
- The image feature used for detection and the distance-estimation relationship, if used.
- Calibration parameters, their units, and how each was obtained.

Configured software constants are not automatically calibrated measurements. A calibration record should include the target dimensions or known distances, test setup, observations, fitted parameters, and uncertainty or limitations.

## Drawing conventions

### Identification block

Every controlled drawing should carry, at minimum:

| Field | Requirement |
|---|---|
| Drawing ID | Unique identifier from the drawing register, such as MEC-002. |
| Title | Short description of the component, assembly, or diagram. |
| Revision | Controlled revision letter or number. Start at Rev A for the first released issue and increment after an approved change. |
| Date | Date of issue. |
| Author / checker / approver | Names or roles responsible for preparation, checking, and release. |
| Units | Explicit units for all dimensions (for example, mm or degrees). Do not rely on an unstated default. |
| Scale | Drawing scale, or “NTS” when the view is not to scale. |
| Sheet | Sheet number and total number of sheets, where applicable. |
| Status | Concept, draft, for review, or released for manufacture. |

### Dimensions, datums, and tolerances

- Use millimetres for mechanical dimensions unless the drawing explicitly states otherwise.
- Define datum references from functional mounting or alignment surfaces. Use the same datum scheme across related part and assembly drawings where practical.
- Dimension from functional datums rather than creating chains of dimensions that accumulate avoidable tolerance.
- Apply tolerances to dimensions that affect fit, alignment, motion, sensor position, or safety. State a general tolerance standard or explicit tolerances; do not leave critical dimensions undefined.
- Identify hole diameters, slots, centre distances, angles, clearances, and mating interfaces clearly.
- Avoid duplicating dimensions in a way that creates conflicting requirements.
- For 3D-printed parts, specify the material, print orientation where functionally important, layer/process assumptions where relevant, and any post-processing or insert requirements.

### Materials and manufacturing notes

A manufacturing drawing should state the material and, where necessary, grade or specification. Include the manufacturing process, surface finish, support removal, drilling, tapping, inserts, adhesives, or assembly instructions when these affect the finished part.

For additive-manufactured parts, identify the CAD/STL file name and revision used to generate the part. STL files do not reliably carry units or full design intent; state the intended units and verify the imported model scale before slicing or manufacture.

### Diagram classes and release status

- **Functional block diagrams** describe system functions and interfaces.
- **Analytical schematics** define variables, forces, and relationships used in calculations.
- **Conceptual mechanism diagrams** explain intended mechanical behaviour but may omit manufacturing dimensions.
- **Software flow diagrams** describe program logic; the released source code remains authoritative.
- **Mechanical layout references** communicate packaging and component placement; they are not automatically manufacturing drawings.
- **Manufacturing drawings** define the dimensions, tolerances, material, and process information required to make or inspect a part.
- **Electrical interface maps** describe verified device and port connections; they do not replace detailed wiring or connector documentation where that is required.
- **Sensor geometry references** describe mounting and measurement geometry; calibration records provide the evidence for numerical parameters.

A drawing must not be labelled “released for manufacture” until its dimensions, tolerances, material, revision, and checking status are complete.

## Revision and change control

- Assign a unique drawing ID and maintain it when the drawing is revised.
- Increment the revision when geometry, interfaces, dimensions, tolerances, wiring, or functional meaning changes.
- Record a concise change description for each revision.
- Identify related CAD files, software versions, or calibration records affected by the change.
- Recheck dependent assemblies and interfaces after a change. For example, a camera mount change may affect CAM-001, MEC-001, and the obstacle-detection calibration.
- Keep obsolete revisions identifiable; do not silently overwrite a released drawing without recording the revision change.

## Release criteria

Before release, confirm that:

1. The drawing ID, title, revision, units, scale, and status are present.
2. Dimensions and datums are clear and consistent with the referenced CAD model or verified hardware.
3. Critical tolerances, materials, and manufacturing notes are specified for fabrication drawings.
4. Interfaces with adjacent parts, sensors, motors, and the EV3 brick have been checked.
5. The drawing has been reviewed and its change record updated.
6. Any related test or calibration requirement is linked to the relevant validation record.

The linked SVG diagrams are suitable for system-level communication and design review. Use dimensioned CAD-derived drawings for fabrication, and verify electrical diagrams against the physical wiring before relying on them during assembly or troubleshooting.
