# Generalized Semantic Versioning — grounding and worked examples

## Why the generalization is not an extrapolation

Standard SemVer (semver.org) defines a breaking change against an API: a contract point at which one party exposes something and another party builds an expectation of continuity around it. An API is already, by definition, a special case of a more general thing — an *interface*, in the broad sense of any point of coupling where one party offers something and another forms an expectation around it. Reading SemVer at the level of interface-in-general rather than API-in-particular is not stretching the concept beyond its domain of validity; it is applying the concept at the level it was already defined to operate on. An engagement's scope, an essay's argument, and a software API are all interfaces in this sense: each is a point of coupling where one party offers something and another party forms an expectation of continuity around it.

Backward compatibility is a property someone chooses to engineer into a release, not a guarantee the version number itself confers — so a MAJOR release can legitimately break that expectation even where no literal API was ever exposed.

The practitioner-facing version of the same idea (from the Semantic Versioning and Parallel Development deck):

- **MAJOR** — the product's contract boundary changes and existing consumers may need to adapt.
- **MINOR** — the product's value expands while preserving all existing consumer assumptions.
- **PATCH** — the product's quality improves without changing scope or expected behavior.

## Why the first version is always 0.1.0

A PATCH corrects existing scope; a subject with no prior version has no scope yet to correct, so 0.0.1 is not reachable. 1.0.0 marks the MAJOR threshold — the moment a subject crosses from cumulative draft into something the domain recognizes as delivered — and a subject cannot cross that threshold before it exists in any tracked form. The event that brings a subject into tracked existence at all — enough coalescing of material to be worth versioning — is itself additive: something now exists to consult where nothing did before, and nothing prior is broken because there was no prior consumer expectation to break. That is exactly the MINOR condition, applied for the first time. Hence 0.1.0, unconditionally, for every subject's first tracked state.

## Subject-type mapping

| Subject | Consumer | Interface (what continuity is expected) | MAJOR example | MINOR example | PATCH example |
|---|---|---|---|---|---|
| Software module | Calling code | The API signature and behavioral contract | Removing or renaming a public method | Adding a new optional parameter | Fixing a bug with no behavior change to the documented contract |
| Enterprise Architecture deliverable (e.g. a client blueprint) | The client engagement | The scope and decisions the engagement was signed off against | Revisiting a foundational architectural decision the client already acted on | Adding a new section covering a previously unaddressed domain | Correcting a factual error in an already-approved section |
| Essay or thesis | The reader | The argument's thesis and the distinctions it depends on | Reversing or replacing the thesis itself | Adding a new supporting section or example that extends the argument without changing the thesis | Fixing a citation, a typo, or an infelicitous phrase |
| Knowledge-repository unit | Whoever cites or builds on the unit | The unit's declared scope | The unit crosses from cumulative draft into a recognized deliverable | An additive increment within a scope still incomplete | A correction with no change to scope |

## Precedence rule

When a single change is simultaneously breaking and additive — it both invalidates an existing consumer expectation and adds new value — standard SemVer practice governs: classify by MAJOR. The version number communicates the most disruptive effect present, not the most generous one. A caller should not average or split the difference between MAJOR and MINOR signals; the higher classification always wins.

## Deliberately out of scope

This reference, like the skill itself, does not cover:

- Pre-release or build-metadata suffixes (`-alpha`, `+build.123`).
- File-naming, namespace, or repository conventions for encoding a version once assigned.
- Branching strategy or release process.

A caller with its own conventions for any of these (for instance, a GitOps-style unit-chain filename scheme) should apply this skill only for the classification decision and handle encoding separately.
