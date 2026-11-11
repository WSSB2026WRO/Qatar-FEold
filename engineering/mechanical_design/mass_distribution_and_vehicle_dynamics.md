# Mass Distribution and Vehicle Dynamics — Concept Study

![DYN-001 — Vehicle dynamics model](../../docs/drawings/DYN-001_vehicle_dynamics.svg)

> **Study type:** This is a conceptual engineering study. It explains a theoretical vehicle layout. It does not claim that the layout has been built, measured, or tested on our current robot.

## 1. Why we are studying mass distribution

Where we place the parts changes the load on each wheel. This can affect grip, braking, steering, cornering, vibration, and the stability of our sensor readings. We use this study to understand the main relationships and to plan what we would need to measure on a real vehicle.

The questions we want to answer are:

1. Where should the heavy parts be placed?
2. How does their position change the static load on each wheel?
3. How does centre-of-gravity height affect load transfer?
4. How do steering geometry and tyre forces work together?
5. What measurements would we need to check the model?

## 2. Coordinates and reference point

We define a right-handed coordinate system:

- (x): forward along the vehicle centreline.
- (y): left across the vehicle.
- (z): upward from the ground.

The origin is at the centre of the rear axle, at ground level. The front axle is at (x=L), the rear axle is at (x=0), and the centreline is (y=0).

The main dimensions are:
- (L): wheelbase.
- (T_f): front track width.
- (T_r): rear track width.
- (h_{CG}): centre-of-gravity height.
- (x_{CG}, y_{CG}, z_{CG}): centre-of-gravity coordinates.

We do not assume numerical dimensions in this concept study unless a separate design case is stated.

## 3. Listing the component masses

We can treat the vehicle as a group of separate components. For each component (i), we should record:

| Variable | Meaning |
|---|---|
| (m_i) | Component mass |
| (x_i,y_i,z_i) | Component centre coordinates |
| (I_{xx,i},I_{yy,i},I_{zz,i}) | Principal moments of inertia |
| (R_i) | Component size and clearance envelope |
| (S_i) | Mounting interface |

The list should include the chassis, drive motors, steering motor, wheels, battery, controller, sensors, camera, wires, printed adapters, fasteners, and protective parts.

### 3.1 Centre of gravity

For separate component masses:

[
M=\sum_{i=1}^{n}m_i
]

[
x_{CG}=\frac{\sum m_i x_i}{M},\quad
y_{CG}=\frac{\sum m_i y_i}{M},\quad
z_{CG}=\frac{\sum m_i z_i}{M}
]

The centre of gravity is a mass-weighted position. It is not necessarily at the geometric centre of the chassis.

### 3.2 What the positions mean for the design

- A low battery position can reduce the centre-of-gravity height.
- Heavy parts near the centre can reduce yaw inertia compared with putting the same parts at the ends.
- A left/right mass offset gives unequal static wheel loads.
- A high camera or sensor mount can increase roll sensitivity and vibration.
- We should include cable loops and moving parts if their mass is significant.

## 4. Static load on the front and rear axles

For a vehicle on level ground, with total weight (W=Mg), wheelbase (L), and longitudinal centre-of-gravity coordinate (x_{CG}):

[
F_{z,front}=W\frac{x_{CG}}{L}
]

[
F_{z,rear}=W\left(1-\frac{x_{CG}}{L}\right)
]

These equations assume static balance, a rigid support plane, and no external force in the forward direction.

If the centre of gravity moves forward, the front axle carries more load and the rear carries less. Moving it backward has the opposite effect. The best balance also depends on which wheels drive and steer the vehicle, as well as the tyre characteristics.

## 5. Static left/right load

For equal front and rear track (T), a simplified lateral balance gives:

[
F_{z,left}=W\left(\frac{1}{2}+\frac{y_{CG}}{T}\right)
]

[
F_{z,right}=W\left(\frac{1}{2}-\frac{y_{CG}}{T}\right)
]

This is a simplified expression for a symmetric layout. If the front and rear tracks are different, we need to solve the four wheel reactions using force and moment balance.

## 6. Four-wheel reactions

The four contact points are:

- Front-left: ((L,+T_f/2))
- Front-right: ((L,-T_f/2))
- Rear-left: ((0,+T_r/2))
- Rear-right: ((0,-T_r/2))

The vertical wheel reactions (N_{FL},N_{FR},N_{RL},N_{RR}) must satisfy:

[
N_{FL}+N_{FR}+N_{RL}+N_{RR}=W
]

[
\sum M_y=0,\qquad \sum M_x=0
]

To find one unique answer for all four wheels, we also need an assumption about frame stiffness, suspension compliance, or measured support deflection. With a rigid four-wheel frame on an uneven surface, the load distribution may not be determined by statics alone.

## 7. Longitudinal load transfer

When the vehicle accelerates at (a_x), a simplified load-transfer magnitude is:

[
\Delta F_x=\frac{M a_x h_{CG}}{L}
]

During acceleration, load moves toward the rear axle. During braking, it moves toward the front.

This equation assumes a rigid body, level ground, no important aerodynamic forces, and a quasi-static pitch balance. It does not describe every part of a real transient movement.

## 8. Lateral load transfer and rollover

For lateral acceleration (a_y), a simplified total lateral load-transfer magnitude is:

[
\Delta F_y=\frac{M a_y h_{CG}}{T}
]

A wider track reduces this load-transfer estimate. A lower centre of gravity also reduces it.

For an ideal rigid vehicle with a symmetric track, the geometric static tip threshold is:

[
a_{y,tip}\approx g\frac{T}{2h_{CG}}
]

This is a theoretical threshold, not a safe speed or acceleration limit. Tyre sliding, sudden movement, frame flexibility, floor friction, and wheel lift can cause loss of control earlier.

## 9. Yaw inertia and turning

The yaw moment of inertia about the vertical axis is:

[
I_z=\sum_i\left(I_{z,i}+m_i[(x_i-x_{CG})^2+(y_i-y_{CG})^2]\right)
]

A component placed far from the centre of gravity adds more yaw inertia. A compact layout can make the robot respond to turning more easily, but we still need to leave room for cooling, cables, camera visibility, and maintenance.

## 10. Steering geometry and Ackermann condition

At low speed, ideal Ackermann steering makes the inner wheel turn more sharply than the outer wheel.

[
\cot(\delta_o)-\cot(\delta_i)=\frac{T}{L}
]

Here, (delta_i) and (delta_o) are the inner and outer wheel angles.

This relationship assumes pure rolling and a shared turning centre. A real linkage can only approximate it within the limits of its dimensions, clearances, and flexibility.

For a more complete steering study, we should record the pivot positions, tie-rod connection points, steering-arm lengths, actuator travel, mechanical stops, joint play, and measured wheel angles across the steering range.

## 11. Traction and drive force

A simple tyre friction limit is:

[
|F_x|\leq \mu N
]

Here, (mu) is the effective friction coefficient between the tyre and floor, and (N) is the normal load on the wheel.

For driven wheels, the theoretical drive force is limited by both motor torque and available grip:

[
F_{drive}\leq \min\left(\frac{\tau_{wheel}}{r},\mu N_{driven}\right)
]

This shows why motor torque alone does not tell us how quickly the robot will accelerate. If the driven wheels do not have enough load, more torque can make them slip instead of moving the robot forward.

## 12. Sensor movement and vibration

A sensor can detect both the vehicle's movement and vibration from its mounting. A high centre of gravity, flexible frame, loose bracket, or long camera support can increase image movement and gyro disturbance.

Some design points we should consider:
- Mount the gyro close to a rigid part of the chassis.
- Keep sensor brackets short where possible.
- Add support without making the mount too flexible.
- Route cables so they do not pull on the sensors.
- Use vibration isolation only if it does not affect sensor alignment.

## 13. Battery placement

The battery can be one of the heaviest parts we can move. In the design, we should consider its height, distance from the vehicle centre, left/right position, retention during turns, access for replacement, and protection from impacts and cable strain.

The centre-of-gravity values in the reference model are assumptions. They have not been measured on our robot.

## 14. How we could check the model

### 14.1 Weigh the components
Weigh each removable component with a calibrated scale. Record the scale resolution and repeat the readings.

### 14.2 Measure component positions
Measure each component centre from the coordinate origin. For irregular parts, use CAD mass properties or a suitable balancing method to estimate the centre of mass.

### 14.3 Measure the four wheel loads
Place each wheel on a separate scale at the same height. Record the four readings at the same time. Repeat after moving the battery or another heavy component.

### 14.4 Estimate centre-of-gravity height
Use a controlled tilt-table or validated suspension method. Secure the robot so it cannot slide or fall. We should not estimate this value from a photograph.

### 14.5 Run dynamic tests
Start with low-speed acceleration, braking, and constant-radius turns. Record speed, heading, wheel slip, and any wheel unloading. Increase the test level gradually.

## 15. Design choices and trade-offs

| Design choice | Possible benefit | Possible trade-off |
|---|---|---|
| Lower battery | Lower centre of gravity and less load transfer | Less ground clearance or harder access |
| Central battery | Lower yaw inertia | More difficult packaging |
| Wider track | Higher geometric roll threshold | Wider robot |
| Longer wheelbase | Less pitch sensitivity for the same CG height | Larger turning space |
| Stiffer steering linkage | More repeatable wheel angle | Higher load on joints and motor |
| Shorter sensor mounts | Less vibration leverage | Possible field-of-view limits |

## 16. What we take from this study

For a small autonomous robot, mass placement can change how it grips, turns, and stays stable. To make a real design decision, we need a component mass list, measured positions, centre-of-gravity calculations, static wheel-load readings, and dynamic tests. The equations give us a starting point, but they do not describe measured performance of our physical robot.

## 17. Data still needed for a numerical report

- Total vehicle mass and individual component masses.
- Wheelbase and front/rear track measurements.
- Component centre coordinates.
- Tyre radius and an estimate of floor friction.
- Motor torque-speed data and gear ratio.
- Steering pivot and tie-rod coordinates.
- Measured acceleration and turning radius.
- Four-wheel static load readings.
- Sensor positions and vibration observations.