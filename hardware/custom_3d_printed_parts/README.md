# Custom 3D-Printed EV3 Components

The project records describe three STL mesh files as modified components for the EV3 mechanical system. **The STL files themselves are not present in the current repository tree.** The catalogue below preserves the available inspection metadata and technical descriptions, but it is not a substitute for the source meshes or native CAD models and cannot be used alone to reproduce or release the parts for manufacture.

## Part catalogue

| Part ID | Source file | Mesh profile | Mesh condition |
|---|---|---|---|
| C3DP-01 | `I lego.stl` | I-profile / linkage-like geometry | Two watertight connected shells |
| C3DP-02 | `4 I modified lego.stl` | Elongated multi-feature geometry | Four connected components; complete mesh is not watertight |
| C3DP-03 | `1x3 modified.stl` | Narrow 1×3-style connector geometry | One watertight connected component |

## Technical records

- [Mesh inspection report](mesh_inspection_report.md)
- [C3DP-01 — I-profile component](part_01_i_lego.md)
- [C3DP-02 — Four-section modified component](part_02_four_i_modified.md)
- [C3DP-03 — Modified 1×3 component](part_03_one_by_three_modified.md)

## Source asset availability

The referenced filenames are `I lego.stl`, `4 I modified lego.stl`, and `1x3 modified.stl`. None is currently committed in this directory. Add the original files and, preferably, their native CAD sources in a controlled revision before attempting a fresh mesh inspection or manufacturing release.

## Dimensional interpretation

STL files do not store unit metadata. The inspected bounding-box proportions are consistent with centimetre-scale source coordinates for LEGO-compatible geometry, but the export unit convention must be confirmed in the originating CAD environment before manufacturing dimensions are released.

## Manufacturing and inspection

Preserve the supplied STL geometry as the source revision. Inspect mesh scale, connected components, normals, wall thickness, pin-hole geometry, and mating fit before printing. Record material, nozzle diameter, layer height, infill, print orientation, and post-processing for each production revision.

The exact installed position and mechanical load path of each component are defined by its mating assembly, not by the STL filename alone.
