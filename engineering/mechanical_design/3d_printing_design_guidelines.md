# Additive Manufacturing — Design and Inspection Guidelines

## Purpose

Custom printed components can provide geometry that is not available in the standard EV3 element set, including adapters, compact links, spacers, and special connection pieces. Their use should be supported by dimensioned drawings and fit checks.

## Design considerations

- Orient layer lines to avoid placing peak tensile stress across layer interfaces.
- Use generous fillets at transitions and around pin holes.
- Maintain adequate wall thickness around holes and narrow necks.
- Avoid sharp internal corners that concentrate stress.
- Allow for printer-specific hole shrinkage and dimensional compensation.
- Avoid excessive press-fit interference on brittle printed features.
- Provide tool access for assembly and disassembly.
- Keep the part envelope clear of moving steering and drive components.

## Print record

For each production print, record:
- Printer and nozzle diameter
- Filament manufacturer and material grade
- Nozzle and bed temperatures
- Layer height and line width
- Wall/perimeter count
- Infill pattern and density
- Print orientation and support strategy
- Part mass
- Critical dimensions after printing
- Fit inspection and failure observations

## Mechanical verification

A printed part should be checked for:
1. Dimensional accuracy.
2. Hole and pin alignment.
3. Fit without forcing mating parts.
4. Interference through full mechanism travel.
5. Crack initiation around holes and thin sections.
6. Layer separation after repeated loading.

## STL release requirements

STL files should be accompanied by a native CAD source, a dimensioned drawing, declared units, revision, and a mesh integrity report. Original supplied files must be preserved when repairs or redesigns are made.
