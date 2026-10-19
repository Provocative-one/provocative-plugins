# Working-log mode, digest

Digest of Sections 6, 10.9 and 10.10 of the Corponomia specification. The specification governs; this file orients the agent.

## Unit

A unit has five fields: Implements, Succeeds, Supersedes / Obsoletes, Presupposes, Leaves open. It is created once and never edited. Implements and Leaves open are always filled. Succeeds is filled when the chain is not linear.

## Composite Identifier

An open item is an entry of a unit's Leaves open field. Its identifier is the unit version, a hash sign, the family and the ordinal within the unit: `0.4.1#A-2`. Across corpora it is qualified: `one.provocative.architecture@0.4.1#A-2`. The only family is A. An entry is closed when a later unit cites its identifier in Implements. The unit that opened it is never edited.

The need to record an architectural decision calls for an item on creating an architecture document with a decision register, for example `0.4.1#A-3`. No decision identifier exists in the working-log.

## Central register

When a central register is instantiated, it indexes every item the working-log has ever opened, closed ones included. Each receives a Proxy Row with its own register identifier (`[A-1]`), the origin it stands for (`0.1.2#A-1`) and its status, naming the closing unit when closed. Register identifiers follow the order of origin: unit version first, ordinal second. The instantiation is a unit and lists the Proxy Rows. After it, new items are rows of the register, a later unit closes a row by citing its identifier in Implements, and units stop opening Composite Identifiers. The audit requires that the identifiers found in the working-log and the origins of the Proxy Rows coincide.

## Surfaces and pointers

Any surface may create a unit. The surface that runs the audit certifies and commits it, and a unit written elsewhere stays provisional until then. Each surface keeps one pointer, the last unit it has read. The pointer holds a position and no content, may be mutable and kept outside the history, and is written only by its own surface. Unit versions are assigned at authoring, from the tip of the chain the author last read, and the audit verifies that no two units share a version. A Succeeds field naming a unit that is no longer the tip reveals concurrent work.

## Awareness unit

Instantiating the mode produces a unit that states the mechanism in force: surfaces, pointers and the identifier scheme. It cites the specification version in Presupposes and leaves the definition to the specification. Its version is 0.1.0 when the chain is empty and the next version otherwise. The pointers start by pointing at it.

## Declaration

One line of `CLAUDE.md` declares the mode. An untracked `HANDOFF.md` is not a declaration. Without one, fallback mode applies.
