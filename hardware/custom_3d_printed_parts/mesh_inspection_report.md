# STL Mesh Inspection Report

## What this report covers

We kept the inspection results for three source STL meshes in this report. The STL files themselves are not included in the current repository snapshot. The values below are therefore saved inspection records, not a new inspection of files in the current checkout.

## Inspection method

The original triangle meshes were checked for vertex count, face count, bounding-box size, connected components, watertightness, winding consistency, and mesh volume. The source geometry was not overwritten.

## Summary

| File | Vertices | Faces | Components | Watertight |
|---|---:|---:|---:|---|
| I lego.stl | 1,518 | 3,064 | 2 | Yes |
| 4 I modified lego.stl | 1,134 | 2,628 | 4 | No |
| 1x3 modified.stl | 1,504 | 3,024 | 1 | Yes |

## Units

An STL file does not say whether its coordinates are in millimetres, centimetres, or another unit. We have kept the bounding-box values in the native STL units. The 1×3-style model has proportions that look consistent with a centimetre-scale export, but the CAD export convention is not recorded in this repository.

## What we found in the meshes

- `I lego.stl`: two watertight shells.
- `4 I modified lego.stl`: four connected shells. Each shell is watertight on its own, but the complete mesh is not one watertight solid.
- `1x3 modified.stl`: one watertight shell.

These values belong to the earlier inspections of the three named source files.