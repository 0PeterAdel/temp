# Completion Gate

> **Page ID:** `GATE` · **Type:** Component workspace · **Phase:** Design now  
> **Status:** Not Started — scaffold; proposed role assignment only.

| Responsibility | Role |
|---|---|
| Owner | Backend Engineer (Data & Persistence Owner) |
| Contributors | AI Engineer & Research Lead, Cybersecurity & Backend Engineer (Security Owner) |
| Reviewer | Technical Lead / Software Architect |
| Last reviewed / role confirmation | TBD — confirm during team assignment |

[Runtime Layers](../index.md) · [Architecture Overview](../../architecture-overview.md)

## Overview & current understanding

**Candidate vision:** Define how an authoritative completion outcome follows from agreed criteria and trustworthy verification.

**Candidate boundary:** Decide task completion; do not equate an execution claim with acceptance or invent evidence.

**Design work:** Explain why this component exists, what goes wrong without it, and the authority it should or should not possess. Verify these candidate statements; do not treat them as approved contracts.

## Workflow & conceptual interfaces

Describe the normal input → behavior → output flow; include ambiguous, denied, failed or incomplete paths when relevant.

| Input / trigger | Source | Conceptual behavior | Output / next component | Unknowns |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

**Scenario to develop:** A candidate has passing visible checks but missing evidence for a mandatory requirement.

## Elements & ownership

One page per substantial element. The component owner coordinates; element owners write their page and reviewers check it. Listed contributors are suggestions, and other disciplines may join research. Reviewers must not co-author the material they independently review. Split, merge or move elements when the design requires it.

| Element | Owner | Contributors | Reviewer | Expected design output |
|---|---|---|---|---|
| [Completion Criteria](criteria.md) | AI Engineer & Research Lead | Backend Engineer (Data & Persistence Owner), Cybersecurity & Backend Engineer (Security Owner) | Technical Lead / Software Architect | Criterion / source / mandatory flag / proof / failure behavior |
| [Decision Authority](authority.md) | Backend Engineer (Data & Persistence Owner) | AI Engineer & Research Lead, Cybersecurity & Backend Engineer (Security Owner) | Technical Lead / Software Architect | Authority / allowed decision / inputs / constraints |
| [Completion Outcomes](outcomes.md) | Backend Engineer (Data & Persistence Owner) | UI/UX Designer & Mobile (Design Owner), Frontend Engineer (Frontend Owner) | AI Engineer & Research Lead | Outcome / precondition / next state / user explanation |

## Expected component outputs

- Coherent purpose, responsibilities and exclusions.
- Reviewed conceptual workflow and input/output model with normal and failure examples.
- Element deliverables integrated into a consistent model; unresolved cross-element conflicts visible.
- Material questions and their impact, linked research and decisions; no silent assumptions.

## Open questions / blockers

The following are starter prompts, not confirmed blockers. The owner must classify them after discussion. Detailed question records live in the element pages.

| Question | Impact / affected element | Classification | Source |
|---|---|---|---|
| Can a task be accepted with an inconclusive optional check? | Completion Criteria | To triage | [Question & work](criteria.md) |
| What decisions can be automated and what requires explicit authorization? | Decision Authority | To triage | [Question & work](authority.md) |
| What state should represent insufficient evidence? | Completion Outcomes | To triage | [Question & work](outcomes.md) |

## Dependencies & shared responsibilities

[Verification & Evaluation](../verification-evaluation/index.md) · [Repair & Recovery](../repair-recovery/index.md) · [Ask & Decide](../../shared-components/ask-decide/index.md) · [Experience Management](../experience-management/index.md)

For each material dependency, record exchanged information, authority, failure behavior and any unresolved assumptions.

## Research & decisions

Link investigation notes and material decisions; write their effect on this component here. No decisions have been marked Agreed by this scaffold.

[Open Questions](../../../03-research-decisions/open-questions.md) · [Research Library](../../../03-research-decisions/research-library.md) · [Decision Log](../../../03-research-decisions/decision-log.md)

## Implementation & Jira (later)

Only fill this when a relevant design slice is agreed and the scope is clear. Use the [Work Package & Jira Template](../../../_templates/work-package.md); Jira owns delivery status.

| Work package | Design reference | Expected outcome | Dependencies | Jira link |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | Not created |

## Review criteria

- [ ] Element outputs reconcile with one another and the conceptual architecture.
- [ ] Authority and boundaries are clear; scenarios include failures and uncertainty.
- [ ] Blocking questions affecting the proposed agreed scope are resolved or scope is narrowed.
- [ ] A distinct reviewer checks technical consistency; affected roles are consulted.

## Design changes

| Date / version | Change | Reason / decision link | Impact |
|---|---|---|---|
| Initial scaffold | Candidate elements and questions | Source discussion; not approved design | Review with team |
