# Custom 3D-Printed Mechanical Components

## Overview

The team supplied three STL mesh files described as modified or custom pieces intended to complement the EV3 mechanical system. They are catalogued here as design artifacts. The exact mechanical function, mating geometry, material, print orientation, and installed location have not yet been independently confirmed.

## Supplied mesh inventory

| Original filename | Repository filename | File size | Mesh status |
|---|---|---:|---|
| `I lego.stl` | `I_lego.stl` | 153,284 bytes | Watertight mesh; 2 connected components |
| `4 I modified lego.stl` | `4_I_modified_lego.stl` | 131,484 bytes | Non-watertight mesh; 4 connected components |
| `1x3 modified.stl` | `1x3_modified.stl` | 151,284 bytes | Watertight mesh; 1 connected component |

## Mesh inspection notes

The STL files do not carry a reliable unit declaration. The bounding-box extents measured from the meshes are therefore reported in **STL coordinate units**, not assumed millimetres:

| Part | X extent | Y extent | Z extent |
|---|---:|---:|---:|
| I LEGO | 3.9565 | 2.4333 | 0.7851 |
| 4 I modified LEGO | 0.7921 | 3.2973 | 0.7800 |
| 1×3 modified | 2.3989 | 0.7200 | 0.8000 |

The second mesh is not watertight and contains four connected components. It should be reviewed in CAD or mesh-repair software before manufacturing or structural use. A non-watertight STL may still be intentionally composed of separate surfaces, but print readiness cannot be assumed.

## Engineering release checklist

For each part, add the following before treating it as a released production component:

1. Confirm physical function and assembly location.
2. Confirm intended unit scale and critical dimensions.
3. Identify mating EV3/LEGO geometry and fit tolerances.
4. Record CAD source file and revision.
5. Record material, nozzle diameter, layer height, infill, wall count, and print orientation.
6. Inspect mesh closure, normals, self-intersections, and connected components.
7. Verify fit on the real assembly without forcing or stressing EV3 elements.
8. Inspect for cracks, layer separation, and deformation after use.
9. Record a photograph of the installed part and a dimensioned drawing.

## File release policy

Original STL geometry should be preserved. Any repaired, scaled, or redesigned mesh must be saved as a separate revision with a change note. Do not overwrite the original supplied file.

## Current status

The three STL meshes have been inspected locally, but their binary assets are not yet included in this repository. The inventory and inspection notes are documented; the actual STL files must be added as binary Git objects before this section can be considered complete.
