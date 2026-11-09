# Additive Manufacturing Design Guidelines

## 1. Purpose

Custom 3D-printed components extend the EV3 mechanical element set with adapters, compact links, spacers, and dedicated connection features. Their design must account for geometry, print orientation, material behaviour, fit, and load direction.

## 2. Geometry design

- Maintain adequate wall thickness around holes and narrow necks.
- Use generous fillets at transitions that carry repeated loads.
- Avoid abrupt section changes where stress concentration is likely.
- Provide suitable clearance for pins, axles, and mating elements.
- Account for printer dimensional accuracy and material shrinkage.
- Orient layer lines to support the dominant mechanical load.

## 3. Material selection

Material selection should consider:
- stiffness and tensile strength;
- impact resistance;
- fatigue behaviour;
- operating temperature;
- layer adhesion;
- print repeatability.

For highly loaded joints, evaluate the printed part in its actual load direction rather than relying only on nominal filament strength.

## 4. Print process definition

A manufacturing record should specify:
- material and filament grade;
- nozzle diameter;
- layer height;
- wall/perimeter count;
- infill pattern and density;
- print orientation;
- bed and nozzle temperature;
- post-processing method.

## 5. Dimensional and mesh inspection

Inspect:
- overall dimensions;
- pin and axle interface geometry;
- hole diameter and spacing;
- wall thickness;
- connected mesh components;
- watertightness and normal orientation;
- mating fit and moving clearances.

## 6. Mechanical verification

Evaluate the component under representative loading. Inspect for deformation, cracking, layer separation, excessive clearance, and wear after repeated operation.

## 7. CAD and file management

Maintain the STL export together with its native CAD model, dimensioned drawing, declared units, revision identifier, and mesh inspection record. Preserve original geometry when producing a modified design revision.
