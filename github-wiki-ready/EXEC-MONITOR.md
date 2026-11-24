# Execution Monitoring & User Interaction

> **Page ID:** `EXEC-MONITOR` · **Type:** Element workspace · **Phase:** Design now  
> **Status:** Not Started — scaffold; proposed role assignment only.

| Responsibility | Role |
|---|---|
| Owner | Frontend Engineer (Frontend Owner) |
| Contributors | Backend Engineer (Data & Persistence Owner), AI Engineer & Research Lead, Cybersecurity & Backend Engineer (Security Owner) |
| Reviewer | UI/UX Designer & Mobile (Design Owner) |
| Last reviewed / role confirmation | TBD — confirm during team assignment |

[Parent component](EXEC) · [Architecture map](ARCH)

## Objective

Define user-visible execution observations and controls without transferring runtime authority to the client.

## Required work & writing guidance

### 1. Identify observations users need during an attempt

Explain the current understanding, provide a concrete example or diagram if useful, distinguish evidence from assumptions, and identify what remains unresolved.

_Working content: TBD._

### 2. Sketch running, disconnected and stopped states

Explain the current understanding, provide a concrete example or diagram if useful, distinguish evidence from assumptions, and identify what remains unresolved.

_Working content: TBD._

### 3. Clarify control permissions with execution state and security owners

Explain the current understanding, provide a concrete example or diagram if useful, distinguish evidence from assumptions, and identify what remains unresolved.

_Working content: TBD._

## Current understanding & proposed design

Write a concise conceptual model in your own words. Include purpose, inputs, outputs, responsibilities, boundaries and what happens when the expected input is missing or invalid. Compare alternatives when the choice matters.

## Example scenario

**Starter case:** A user requests cancellation while an external runtime is disconnected.

Describe input, expected behavior, result and what happens in a failure or ambiguous variant. This is a design exercise, not an implemented test result.

## Expected deliverables — output format

Complete the following tailored table as part of this page. Add a diagram or short scenario when it makes the explanation clearer.

| User-visible state | source | action | authorization | feedback |
| --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | TBD |

- A clear answer to the objective and a coherent proposed model.
- The completed table with at least one meaningful scenario; no invented implementation details.
- An explicit list of assumptions, uncertainties and material decisions.

## Open questions

| ID | Question | Impact / what it blocks | Classification | Research |
|---|---|---|---|---|
| `EXEC-MONITOR-Q01` | How should the interface distinguish a requested stop from a confirmed stop? | Assess during exploration | To triage | Create only if deeper investigation is needed |

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
