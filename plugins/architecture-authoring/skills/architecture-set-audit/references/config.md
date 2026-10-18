# Audit configuration

`tools/audit-config.json` at the repository root. Every key below is read by `audit.py`.

| Key | Type | Meaning |
|---|---|---|
| `project_prefix` | string | Prefix of diagram asset IDs, such as `HHB` for `[HHB-CTX-01]` |
| `living_dir` | string | Directory of the living documents; every `*.md` in it must appear under `documents` |
| `documents` | object | Role to path. The roles `architecture` and `estimate` drive the direction and pin checks |
| `also_read` | list | Further files read for references, pointers and residue: usually `README.md`, `CLAUDE.md`, `CHANGELOG.md` |
| `series` | object | Series letter to the role of the document that owns its register |
| `cited_required` | list | Series whose rows must each be cited at least once outside their own row, unless the row's status is terminal (Closed, Withdrawn, Superseded, Retired) |
| `retired_prefixes` | list | Prefixes that must no longer appear, such as `CA` after asserted assumptions moved to `EA` |
| `residue_allow` | list | Tokens that look like series references and are not: `C4`, quarter labels. Default `["C4", "Q1", "Q2", "Q3", "Q4"]` |
| `other_roles` | list | Words that qualify a `§` reference as belonging to a document outside the set, such as `technology report` or `RFP` |
| `rogue_terms` | list | Regular expressions for identifiers of other engagements |
| `vocabulary` | list | Objects `{"term": ..., "forbidden": [...]}`: the client's names and the synonyms that must not appear |
| `client_forbidden_terms` | list | Terms a client-facing dump must not contain, typically effort units, staffing and rates |
| `diagram_palette` | list | House palette as hex colors; `diagram_tools.py check` fails on any other color. Empty or absent skips the check |
| `pointers` | list | Objects `{"file", "pattern", "document"}`: where a file records a document's version, as a regular expression with one capture group |

Adding a series means three edits in one commit: the notation key row (prefix, meaning, home register, who may close a row), the `series` entry here, and, for a plan-side series, `cited_required`.
