# House style

## Palette and typography as parameters

The palette and typography belong to the project, so the skill carries their slots and the project fills them. Record the palette in `tools/audit-config.json` as `diagram_palette`, a list of hex colors; the acceptance check fails on any color outside it. An empty or absent list skips the check.

| Slot | Holds | Typical use |
|---|---|---|
| Primary | The brand's main color | The system in focus, primary boxes |
| Ink | Near-black | Text, outlines, arrows |
| Paper | Off-white or white | Background, inverse text |
| Accent | One contrasting color | The one thing the viewer must notice |
| Neutral | Mid grey | External systems, de-emphasized elements |

Typography: one family, with a generic fallback (`font-family="<Brand family>, sans-serif"`), set on the root element. Never reference a web font by URL; the canvas must render offline and the check fails on any external reference.

## SVG constraints

- A `viewBox` on the root element, so the asset scales.
- Text as `<text>` elements, never converted to paths, so a diff shows what changed and the check can read the labels.
- No `<image>`, no external `href`, no `@import`, no `url(` pointing outside the file.
- Labels match the brief character for character. Line breaks inside a label are `<tspan>` children of one `<text>`.
- Arrowheads defined once in `<defs>` and reused.
- The legend states the arrow kind: "Arrows show dependencies" or "Arrows show data flow". List the legend text under "Other text on canvas" in the brief.

## The simplified executive view

For a slide, derive a separate asset from the full view:

1. The client's own module names replace internal component names.
2. Three colors at most, from the palette.
3. No actor figures; people appear as labeled boxes or not at all.
4. One relationship kind, with the legend saying which.
5. No identifier of any kind: no register reference, asset ID, marker or version.

Register it with its own ID and brief, with the audience set to client, and run the check with `--client-facing`.

## Exports

A PNG or PDF render for a deck or print goes to `generated/` and is never committed. Regenerate it from the SVG when the SVG changes. One way to render for visual review:

```bash
python3 -c "import cairosvg; cairosvg.svg2png(url='arc42/assets/xyz-ctx-01.svg', write_to='generated/xyz-ctx-01.png', output_width=1600)"
```
