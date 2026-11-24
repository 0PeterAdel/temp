# Repair Strategies

> **Page ID:** `RECOVERY-STRATEGY` · **Type:** Element workspace · **Phase:** Design now  
> **Status:** Not Started — scaffold; proposed role assignment only.

| Responsibility | Role |
|---|---|
| Owner | Backend Lead |
| Contributors | Backend Engineer (Data & Persistence Owner) |
| Reviewer | AI Engineer & Research Lead |
| Last reviewed / role confirmation | TBD — confirm during team assignment |

[Parent component](RECOVERY) · [Architecture map](ARCH)

## Objective

Compare targeted repair, retry and replanning.

## Required work & writing guidance

### 1. Define repair scope and affected requirements

Explain the current understanding, provide a concrete example or diagram if useful, distinguish evidence from assumptions, and identify what remains unresolved.

_Working content: TBD._

### 2. Compare local versus full retry

Explain the current understanding, provide a concrete example or diagram if useful, distinguish evidence from assumptions, and identify what remains unresolved.

_Working content: TBD._

### 3. Preserve candidate and attempt history

Explain the current understanding, provide a concrete example or diagram if useful, distinguish evidence from assumptions, and identify what remains unresolved.

_Working content: TBD._

## Current understanding & proposed design

Write a concise conceptual model in your own words. Include purpose, inputs, outputs, responsibilities, boundaries and what happens when the expected input is missing or invalid. Compare alternatives when the choice matters.

## Example scenario

**Starter case:** A dependency change invalidates a downstream result.

Describe input, expected behavior, result and what happens in a failure or ambiguous variant. This is a design exercise, not an implemented test result.

## Expected deliverables — output format

Complete the following tailored table as part of this page. Add a diagram or short scenario when it makes the explanation clearer.

| Failure class | repair option | impact | recheck |
| --- | --- | --- | --- |
| TBD | TBD | TBD | TBD |

- A clear answer to the objective and a coherent proposed model.
- The completed table with at least one meaningful scenario; no invented implementation details.
- An explicit list of assumptions, uncertainties and material decisions.

## Open questions

| ID | Question | Impact / what it blocks | Classification | Research |
|---|---|---|---|---|
| `RECOVERY-STRATEGY-Q01` | When is replanning necessary instead of repairing a step? | Assess during exploration | To triage | Create only if deeper investigation is needed |

## Research & decisions

Link evidence, alternatives and rationale; indicate whether a recommendation is proposed or agreed. See [Research Library](LIBRARY) and [Decision Log](DECISIONS).

## Review criteria

- [ ] Each required-work section has a clear answer or an explicit unresolved question.
- [ ] The output table addresses all named fields and the example is understandable.
- [ ] Boundaries match the parent component, and affected specialists are consulted.
- [ ] Claims are evidence-backed; unknowns and design choices are marked.
- [ ] The reviewer is a different person from the owner, and review scope is recorded.

## Implementation & Jira (later)

Use [Work Package & Jira Template](T-JIRA) only when the relevant design is agreed, or track a clearly scoped research spike. No Jira tickets created.

## Design changes

Record meaningful revisions here with date, reason and affected decisions; preserve superseded rationale.
