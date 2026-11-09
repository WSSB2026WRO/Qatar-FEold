# Chassis Architecture and Packaging Study

## 1. Design objectives

The chassis must provide a stiff reference structure for the drive train, steering mechanism, sensors, and controller while maintaining a compact envelope and practical service access.

Primary design objectives:
- maintain wheel alignment under dynamic load;
- minimize torsional and bending compliance;
- protect wiring and sensor connectors;
- keep the centre of gravity low;
- provide repeatable steering geometry;
- allow rapid battery replacement and maintenance;
- avoid interference between wheels, steering links, and body structures.

## 2. Conceptual structural architecture

A modular two-level layout is recommended for the theoretical design case.

**Lower mechanical plane**
- drive motors and wheel interfaces;
- steering actuator and linkage;
- battery pack mounted low;
- structural cross-members;
- protective lower perimeter.

**Upper electronics plane**
- EV3 controller;
- sensor interface routing;
- camera mounting structure for the obstacle configuration;
- cable guides and strain relief.

This arrangement separates mechanical loads from sensor mounting and reduces the need to route cables through moving steering components.

## 3. Structural load paths

Drive torque travels from each motor mounting interface into the chassis rails and then to the wheel contact patches. Steering reaction loads travel from the road wheels through steering arms and linkage into the steering actuator support. Impact loads should be carried by dedicated structural members rather than by sensor brackets or printed electronics mounts.

## 4. Chassis stiffness

For a simplified beam segment, bending deflection scales with applied load and span and inversely with elastic modulus and second moment of area. A design comparison should therefore evaluate:
- member span;
- cross-section geometry;
- material modulus;
- joint stiffness;
- load direction;
- fastener spacing.

A stiff chassis improves sensor alignment but excessive mass should be avoided. Reinforce high-load joints rather than increasing thickness uniformly.

## 5. Steering clearance envelope

The full swept volume of the steering arm, tie rod, wheel, and cable loop must be checked at both steering limits. A clearance allowance should include:
- manufacturing tolerance;
- joint backlash;
- frame deflection;
- wheel runout;
- cable movement.

No cable should cross a moving linkage path.

## 6. Serviceability

Use accessible fasteners, keyed connectors, labelled ports, and a repeatable assembly sequence. Critical components should be removable without dismantling the entire chassis.

## 7. Design review checklist

- [ ] Wheel alignment is referenced to a common chassis datum.
- [ ] Drive motor mounts resist torque reaction.
- [ ] Steering actuator mount resists cyclic loads.
- [ ] Full steering sweep has no mechanical interference.
- [ ] Battery is mechanically retained.
- [ ] Camera field of view is unobstructed.
- [ ] Ultrasonic sensor faces are aligned with the intended corridor axes.
- [ ] Cable strain relief is provided.
- [ ] Printed components are inspected for cracks and layer separation.
- [ ] Fasteners remain accessible for inspection.
