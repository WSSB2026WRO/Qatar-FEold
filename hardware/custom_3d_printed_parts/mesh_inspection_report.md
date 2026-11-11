# STL Mesh Inspection Report

## Inspection record scope

This report preserves the inspection results recorded for three source STL meshes. The referenced STL files are not included in the current repository snapshot, so the measurements below are retained inspection records rather than a fresh inspection of files in the current checkout.

## Method

The original triangle meshes were inspected for vertex count, face count, bounding-box extents, connected components, watertightness, winding consistency, and mesh volume. The source geometry was not overwritten.

## Summary

| File | Vertices | Faces | Components | Watertight |
|---|---:|---:|---:|---|
| I lego.stl | 1,518 | 3,064 | 2 | Yes |
| 4 I modified lego.stl | 1,134 | 2,628 | 4 | No |
| 1x3 modified.stl | 1,504 | 3,024 | 1 | Yes |

## Units

STL does not encode physical units. The coordinate extents are recorded in native STL units. The proportions of the 1×3-style model are consistent with a centimetre-scale export, but the originating CAD export convention is not recorded in this repository.

## Topology findings

- `I lego.stl`: two watertight shells.
- `4 I modified lego.stl`: four connected shells; each shell is individually watertight, while the complete mesh is not one watertight solid.
- `1x3 modified.stl`: one watertight shell.

The measurements in this report are historical mesh-inspection records associated with the three named source files.
