# Custom 3D-Printed EV3 Components

The team supplied three STL mesh files described as modified components for the EV3 mechanical system. The files are indexed with mesh inspection data and individual technical descriptions.

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

## Dimensional interpretation

STL files do not store unit metadata. The inspected bounding-box proportions are consistent with centimetre-scale source coordinates for LEGO-compatible geometry, but the export unit convention must be confirmed in the originating CAD environment before manufacturing dimensions are released.

## Manufacturing and inspection

Preserve the supplied STL geometry as the source revision. Inspect mesh scale, connected components, normals, wall thickness, pin-hole geometry, and mating fit before printing. Record material, nozzle diameter, layer height, infill, print orientation, and post-processing for each production revision.

The exact installed position and mechanical load path of each component are defined by its mating assembly, not by the STL filename alone.
