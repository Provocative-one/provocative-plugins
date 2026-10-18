# C4 method checklist

The C4 model (Simon Brown) describes a software system at four zoom levels. This package uses the first three. The checklist drives step 2 (choosing the set) and step 6 (the blunt pass).

## Level discipline

| Level | Shows | Leaves out | Test |
|---|---|---|---|
| L1 System Context | The system in focus as one box, the people who use it, and the external systems it depends on or feeds | Technology, internal structure | A reader who knows nothing of the estate can say who uses the system and what it talks to |
| L2 Container View | The separately runnable or deployable units inside the system boundary (applications, services, data stores, pipelines) and the technology of each | Internal structure of any one container | Each box can be deployed, started, or stopped on its own |
| L3 Component slice | The components inside one container, or one cross-cutting concern across a few | Anything outside the slice's concern | The slice answers one question a reader would otherwise have to ask |
| L4 Code | Not drawn in this package | | If the user wants it, generate it from the code |

"Container" here means a separately runnable unit. It has no relation to Docker.

## Choosing L3 slices

Draw a slice where decisions concentrate: a pipeline under an open ADR, a recovery path, an integration with an external platform, a module estate under a disposition program. One slice per concern. A container that nobody is deciding anything about gets no slice.

A slice may be drawn wholly parked or wholly draft. Include it when the record needs to show the work was considered and deferred. Say so in the README's set listing and in the companion's Executive Summary.

## Universal diagram rules

- Every element has a name and a one-line description. Add technology at L2 and L3.
- Every relationship is labeled with its purpose, and its direction is unambiguous.
- Every diagram has a title, its level, and a visible or referenced legend. The state grammar is the legend, stated in the companion header.
- One level per diagram. A component inside an L2 diagram, or a person inside an L3 slice, is a level error.
- Keep a diagram under about twenty nodes. Past that, split by concern.

## The blunt pass

Apply the blunt-critique moves to the package. The audit script covers the mechanical half. The table covers the judgment half.

| blunt-critique move | What it finds in a C4 package |
|---|---|
| Internal contradiction | The `.mmd` and its companion disagree. An element is `present` in L2 and `planned` in an L3 slice. The README's count or set differs from the folder |
| Unfalsifiable claim | A state asserted with no evidence: a `present` element nobody can point to, a `planned` one with no ticket or ADR |
| Definition by example list | A walkthrough line that enumerates technologies and never states the element's responsibility |
| Category error | Two levels in one diagram. Infrastructure drawn as a logical container without saying so. A person drawn as a system |
| Excisability | A node that no relationship touches and no walkthrough line explains. A walkthrough line about something that is not drawn |
| Missing prior art | The governing ADR absent from References. A superseded diagram with no `Supersedes:` line |
| Silent reconciliation | A state changed between versions with no currency note, or a superseded path deleted from the drawing |
| Audience drift | An Executive Summary about the drawing method where the system belongs. A diagram past twenty nodes |

Rank findings by damage. A wrong state on a withdrawn element outranks a label typo. When a full pass finds nothing real, say the package has converged and name what was checked: the audit run, each companion against its source, each state against its evidence.
