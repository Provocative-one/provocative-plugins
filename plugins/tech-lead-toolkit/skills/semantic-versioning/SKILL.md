---
name: semantic-versioning
description: "Classify a change to any versioned subject — software, an Enterprise Architecture deliverable, an essay, a knowledge-repository unit, a governance document, or anything else someone has decided to track through discrete states — as a PATCH, MINOR, or MAJOR increment, or assign the correct first version. Use this skill any time the user asks how to version something, what the next version number should be, whether a change is breaking, or wants a version bumped — even when the subject is not software. This is a pure classifier — it does not itself define file-naming conventions, branching strategy, or release process — and other skills may depend on or embed it whenever they need a versioning decision."
---

# Semantic Versioning (generalized classifier)

This skill classifies a change to a versioned subject according to Semantic Versioning (semver.org), generalized to any subject with a consumer and an interface — not only software with an API. It answers one question at a time: "is this PATCH, MINOR, or MAJOR, or is this the first version?" It does not prescribe file names, repositories, or workflows; a caller that needs those should consult its own conventions and use this skill only for the classification step.

## Core generalization

Standard semver defines a breaking change against an API: a contract point a consumer coded against. That is one instance of a broader category. An **interface**, in the sense this skill uses it, is any point of coupling where one party offers something and another party forms an expectation of continuity around it — a technical API, a document's declared scope, an engagement's terms, or a reader's grasp of an argument are all interfaces in this sense. Backward compatibility is a property someone chooses to engineer into a release; it is not a guarantee the version number itself confers. This means a MAJOR release can legitimately disrupt that expectation even where no literal API was ever exposed — see `references/generalized-semver.md` for the full grounding and worked examples across subject types.

## Procedure

### Step 1 — Identify the subject, its consumer, and its interface

Before classifying anything, establish three things:

1. **The subject**: what is being versioned (a codebase, a document, an essay, a knowledge unit).
2. **The consumer**: who relies on continuity across versions (calling code, a client engagement, a reader, a downstream unit that cites this one). A subject can have more than one consumer class; classify against the consumer whose expectation is most affected.
3. **The interface**: what specific expectation of continuity that consumer holds — the thing a MAJOR change would break. Name it concretely (e.g. "the public method signatures," "the scope the client signed off on," "the thesis and the distinctions it depends on").

If this cannot be answered, ask the user rather than guessing — the rest of the procedure depends on it.

### Step 2 — Check whether a version already exists

- **No prior version exists** → the subject is receiving its first tracked state. Assign **0.1.0** and stop. Do not assign 0.0.1 (a PATCH presupposes prior scope to correct, which a first version lacks by definition) and do not assign 1.0.0 (reserved for the later MAJOR threshold — see Step 3 and the note below). The act of a subject amalgamating into something worth tracking is itself an additive event: MINOR, applied for the first time.
- **A prior version exists** → proceed to Step 3.

### Step 3 — Classify the change, MAJOR first

Apply these three questions in order. Stop at the first "yes." If a single change is both breaking and additive, standard semver practice governs: **MAJOR pre-empts MINOR** — classify by the most disruptive effect present, not the most generous one.

| # | Question | Yes → | No → |
|---|---|---|---|
| 1 | Does the change alter the interface identified in Step 1 such that the consumer must re-engage to preserve their understanding or usage — i.e. does it break the contract boundary? | **MAJOR** | go to 2 |
| 2 | Does the change add to what the subject offers, without invalidating anything the consumer already relies on? | **MINOR** | go to 3 |
| 3 | Does the change correct or refine existing content without altering scope, functionality, or consumer-facing meaning? | **PATCH** | no increment warranted |

If none of the three applies, nothing changed that a consumer would need reflected in a version number — say so rather than forcing a bump.

### Step 4 — Record the classification with rationale

State the assigned increment (or the assigned first version) together with one sentence naming which interface expectation was preserved or broken. This sentence is what makes the classification auditable later — a bare "MINOR" or "MAJOR" with no reference to the interface is not a complete answer under this skill.

## What this skill does not decide

- File-naming or repository conventions for encoding the version (a caller's own convention, e.g. a GitOps unit-chain filename scheme, sits on top of this skill's output).
- Pre-release or build-metadata suffixes (`-alpha`, `+build.123`) — these are out of scope for a general-purpose classifier and should be handled by a caller that needs them, if at all.
- Branching or release-process mechanics.

## Reference

`references/generalized-semver.md` — the interface-in-general argument in full, the subject-type mapping table (software, Enterprise Architecture deliverable, essay, knowledge-repository unit), and worked examples. Load it when the consumer/interface identification in Step 1 is not obvious from the subject type alone, or when the user asks for the reasoning behind a classification rather than just the answer.
