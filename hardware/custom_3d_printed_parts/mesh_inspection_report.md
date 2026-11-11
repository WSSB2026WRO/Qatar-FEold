# STL Mesh Inspection Report

**Asset availability:** The three source STL files referenced by this report are not present in the current repository tree. The values below are retained inspection records and cannot be independently reproduced from the current checkout until the original meshes are added.

## Method

The three supplied STL files were loaded as triangle meshes and checked for vertex count, face count, bounding-box extents, connected components, watertightness, winding consistency, and mesh volume. No geometry was overwritten.

## Summary

| File | Vertices | Faces | Components | Watertight |
|---|---:|---:|---:|---|
| I lego.stl | 1,518 | 3,064 | 2 | Yes |
| 4 I modified lego.stl | 1,134 | 2,628 | 4 | No |
| 1x3 modified.stl | 1,504 | 3,024 | 1 | Yes |

## Units

STL does not encode physical units. The coordinate extents are therefore recorded in native STL units. The proportions of the 1×3-style model are suggestive of a centimetre-scale export, but that inference is not sufficient to declare the units. Confirm the CAD export convention before converting the values to millimetres or creating dimensioned manufacturing drawings.

## Topology findings

- `I lego.stl`: two watertight shells.
- `4 I modified lego.stl`: four connected shells; each shell is individually watertight, but the overall mesh is not one watertight solid.
- `1x3 modified.stl`: one watertight shell.

## Recommended next action

Open each mesh in its originating CAD application, confirm body structure and units, then export a revision with documented units and a matching native CAD source. Keep original exports unchanged for traceability.
