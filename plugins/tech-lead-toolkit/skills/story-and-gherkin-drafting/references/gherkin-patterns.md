# Gherkin patterns

Gherkin states a story's Definition of Done as observable system behavior. Its discipline is that it forbids intent: a scenario describes what the system does under stated conditions, which is testable, and never what the business wants, which is not.

## Form

`Scenario:` / `Given` / `When` / `Then` / `And`.

Write both poles.

- **Positive scenarios, Governance & Assurance Success.** The happy path: the control behaves, the guardrail permits, the pipeline passes.
- **Negative scenarios, Governance & Assurance Failures.** The edge and the violation: the guardrail blocks, the policy denies, the malformed input is rejected. A control that has never been shown to refuse has not been shown to work.

## Rules

- **Operational language only.** Describe observable behavior: a plan that fails, a status that transitions, a policy that returns `deny`. Do not restate business intent.
- **One behavior per scenario.** Compose with `And`; do not conflate.
- **`Given` sets a verifiable precondition.** `When` names the single triggering action. `Then` asserts the observable outcome.
- **Each scenario maps to something a reviewer or a pipeline can check.** If you cannot say what would check it, rewrite it.

## Worked pairs

A policy guardrail:

```gherkin
Scenario: Permission policy scoped to named resources is admitted
  Given an IAM permission policy that lists explicit resource ARNs
  And the guardrail policy set is attached to the workspace's policy evaluation
  When the developer runs a remote apply from the workspace
  Then the plan passes policy evaluation
  And the role is provisioned

Scenario: Permission policy with a wildcard resource is rejected
  Given an IAM permission policy whose Resource is "*"
  When the developer runs a remote apply from the workspace
  Then the guardrail returns deny
  And the plan fails before apply
  And the denial names the wildcard resource as the violated rule
```

An immutable evidence store with an integrity record:

```gherkin
Scenario: Evidence bundle is written to the immutable store with an integrity record
  Given a completed change with a generated evidence bundle
  When the bundle is published
  Then the bundle is written to the write-once container
  And the change record carries the bundle URL and its SHA-256 hash

Scenario: Tampered bundle fails integrity verification
  Given an evidence bundle whose contents differ from its recorded SHA-256 hash
  When integrity is verified against the change record
  Then verification fails
  And the bundle is treated as invalid
```

## Version scenario pairs

Add one pair when the story ships a versioned artifact (see SKILL.md step 5). Pick the pair that matches the classified increment.

**MINOR or PATCH story: existing consumers are unaffected, and an undeclared break is caught.**

```gherkin
Scenario: Additive release leaves existing consumers unchanged
  Given a module at version 1.4.0 with consumers pinned to "~> 1.4"
  And a release that adds an optional input with a default
  When a consumer upgrades to 1.5.0 without changing its configuration
  Then the consumer's plan shows no changes

Scenario: Breaking change tagged as a minor release is flagged
  Given a release that removes an input consumers rely on
  And the release is tagged as a MINOR increment
  When the release review compares the declared increment with the change
  Then the review reports the increment as under-declared
  And the release is blocked until it is tagged MAJOR
```

**MAJOR story: the break is declared and its adaptation path is documented.**

```gherkin
Scenario: Breaking release is declared as MAJOR with an adaptation path
  Given a release that removes an input consumers rely on
  When the release is tagged
  Then the tag is a MAJOR increment
  And the changelog names the removed input and the replacement

Scenario: Consumer on the previous major line is not upgraded implicitly
  Given a consumer pinned to "~> 1.4"
  When the new 2.0.0 release is published
  Then the consumer continues to resolve to the latest 1.x release
```

**First release of a new subject.**

```gherkin
Scenario: First tracked release is 0.1.0
  Given a subject with no previous version
  When its first release is tagged
  Then the tag is 0.1.0
```
