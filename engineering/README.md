# Engineering Studies

This section is the technical design record for the Qatar FE vehicle. It separates source-derived facts, conceptual models, and future validation requirements.

## Study areas

### 1. Mechanical architecture
- Chassis packaging and component placement
- Steering linkage geometry
- Drive-train layout and gear ratio
- Wheelbase, track width, ground clearance, and body envelope
- Fasteners, interfaces, and service access

### 2. Mass properties and vehicle dynamics
- Component mass inventory
- Three-dimensional centre of gravity
- Static axle and wheel loads
- Longitudinal load transfer under acceleration and braking
- Lateral load transfer during cornering
- Rollover margin and stability
- Traction limits and wheel-load sensitivity

### 3. Steering geometry
- Steering axis and tie-link geometry
- Ackermann condition
- Inner and outer wheel angles
- Steering travel and mechanical stops
- Backlash, compliance, and repeatability

### 4. Sensor placement and perception
- Ultrasonic field of view and mounting angle
- Gyro alignment and drift
- Camera field of view and optical axis
- Camera offset relative to vehicle reference point
- Image calibration and pillar range estimation

### 5. System integration
- EV3 port map
- Electrical and mechanical interfaces
- Cable management and vibration isolation
- Access for battery changes and maintenance

## Fundamental equations

### Centre of gravity

For discrete components with masses (m_i) located at ((x_i,y_i,z_i)):

`x_{CG}=\frac{\sum m_i x_i}{\sum m_i},\quad
y_{CG}=\frac{\sum m_i y_i}{\sum m_i},\quad
z_{CG}=\frac{\sum m_i z_i}{\sum m_i}`

The calculation requires measured component masses and coordinates. Without these inputs, a numerical centre of gravity must not be claimed.

### Longitudinal load transfer

A simplified quasi-static estimate is:

`\Delta F_x=\frac{M a_x h_{CG}}{L}`

where (M) is total mass, (a_x) is longitudinal acceleration, (h_{CG}) is centre-of-gravity height, and (L) is wheelbase.

### Lateral load transfer

A simplified quasi-static estimate is:

`\Delta F_y=\frac{M a_y h_{CG}}{T}`

where (a_y) is lateral acceleration and (T) is track width. Actual load transfer depends on suspension and chassis compliance, which must be represented if the model is refined.

### Ideal Ackermann relation

For wheelbase (L), track width (T), inner steering angle (delta_i), and outer steering angle (delta_o):

`\cot(\delta_o)-\cot(\delta_i)=\frac{T}{L}`

This is a geometric idealization. The actual steering linkage must be measured before comparing its performance with ideal Ackermann geometry.

## Engineering evidence levels

| Label | Meaning |
|---|---|
| Source-derived | Explicitly present in the supplied source code or uploaded design file |
| Configured | A parameter value set in software |
| Measured | Obtained through a documented physical measurement |
| Calculated | Derived from stated inputs and an explicit equation |
| Conceptual | A proposed design or theoretical model, not a claim of implementation |
| Validated | Supported by a repeatable test record and acceptance criterion |

## Required technical records

- Dimensioned chassis drawing
- Component mass and coordinate register
- Steering geometry drawing
- Wheel and motor specifications
- Electrical wiring diagram
- Sensor mounting drawings
- CAD source files for printed parts
- Test conditions and raw measurements
- Revision history and engineering change notes
