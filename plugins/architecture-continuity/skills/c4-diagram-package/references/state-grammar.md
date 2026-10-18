# State grammar

Every diagram in a package encodes the lifecycle state of every element with the same grammar. A reader who learns it on the first diagram reads the rest without a legend.

## The seven states

| State | Meaning | Mermaid class | Glyph and word in the label | Look |
|---|---|---|---|---|
| focus | The system in focus (L1 only) | `focus` | none | Heavy solid border, filled with the accent color, white text |
| present | Operational today | `present` | none | Solid border, full fill, solid connectors |
| sunsetting | Being retired | `sunsetting` | `⟢ SUNSETTING` | Amber dashed border |
| planned | Not there yet, or emerging | `planned` | `◇ PLANNED` | Blue dotted border, hollow fill |
| partial | Partly delivered | `planned` | `◐ PARTIAL` | Same look as planned, tagged with the half-filled glyph |
| parked | Deliberately deferred | `parked` | `⏸ PARKED` | Grey dotted border |
| superseded | A discarded design path | `superseded` | `✕ SUPERSEDED` | Red dashed border |

Partial has no class of its own. It reuses `planned` and carries the `◐` tag, because a partly delivered element is still partly not there.

## The canonical class block

Paste this block, unchanged except for the `focus` fill, at the foot of every `.mmd` file.

```
  classDef focus fill:#111111,stroke:#111111,stroke-width:3px,color:#ffffff;
  classDef present fill:#eef2ff,stroke:#111111,stroke-width:2px,color:#111111;
  classDef sunsetting fill:#fff4e5,stroke:#e08600,stroke-width:2px,stroke-dasharray:6 3,color:#111111;
  classDef planned fill:#f5faff,stroke:#1f6feb,stroke-width:2px,stroke-dasharray:2 3,color:#0b4ea2;
  classDef parked fill:#f2f2f2,stroke:#8a8a8a,stroke-width:2px,stroke-dasharray:2 3,color:#555555;
  classDef superseded fill:#ffecec,stroke:#c0111a,stroke-width:2px,stroke-dasharray:6 3,color:#8a0f16;
```

Set the `focus` fill to the client's brand color when the audience expects it. The other five stay fixed so the grammar travels between engagements. When refreshing an existing package, copy its `focus` color and leave it alone.

## Rules

1. **Double-encode.** Style carries the state in color and border. The glyph and word carry it where color is lost: monochrome print, projectors, color-blind readers. Present has no glyph, because absence is the default.
2. **Declare all six classes in every diagram,** including the ones the diagram does not use. Identical blocks make drift visible by diff and let any diagram be pasted into any context.
3. **Class every node.** A node with no state class is an unstated claim. The audit script fails on it.
4. **Connectors follow state.** Solid when the relationship is live at both ends. Dotted (`-.->`) when either end is not present or the relationship is being retired.
5. **A glyph in a label annotates the node's state, unless the label names a sub-part.** "IAM / Credential (IRAw ⏸ parked)" is a present container with one parked capability. The label says so, and the class stays `present`.
6. **A slice entirely in one state** classes every node alike and carries one annotation node that states the state and its driver:
   ```
   NOTE["⏸ PARKED - pending resolution of <the open question>.<br/><Excluded scope> kept off the canvas by driver."]:::parked
   ```
7. **Superseded paths stay drawn** when readers would otherwise rediscover and rebuild them. Label the node with the governing record that replaced it.
8. **A state claim needs evidence.** The companion's References cite the ADR status, ticket state, or deployment fact behind each non-obvious state. An element with no evidence is `planned`.
9. **Exclusions are held off the canvas by driver, never by silence.** Name what is excluded and what drove the exclusion in the header comment and in the companion's Scope note. "Held off the canvas by design" names no driver and does not meet this rule.

## Shapes and labels

- People: stadium shape, `AT(["Application Teams"]):::present`.
- Systems and containers: rectangle with a `<br/>`-separated description, `GL["GitLab<br/>VCS + CI/CD"]:::present`.
- Boundaries: `subgraph` with a title naming the boundary and its owner or subscription. Subgraphs take no class.
- Relationships: label each with a verb phrase for its purpose, `-->|"remote apply, token rotation"|`.
- Titles in `%%` header comments use ASCII only. Write hyphens where a dash or middle dot would go.
