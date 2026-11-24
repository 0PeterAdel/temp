# Ask & Decide

> **Page ID:** `ASK` · **Type:** Component workspace · **Phase:** Design now  
> **Status:** Not Started — scaffold; proposed role assignment only.

| Responsibility | Role |
|---|---|
| Owner | UI/UX Designer & Mobile (Design Owner) |
| Contributors | AI Engineer & Research Lead, Frontend Engineer (Frontend Owner), Cybersecurity & Backend Engineer (Security Owner) |
| Reviewer | Technical Lead / Software Architect |
| Last reviewed / role confirmation | TBD — confirm during team assignment |

[Shared Components](SHARED) · [Architecture Overview](ARCH)

## Overview & current understanding

**Candidate vision:** Explore a shared capability for clarification, approval and decision context when uncertainty or authority requires it.

**Candidate boundary:** Callable across components; not a mandatory lifecycle stage or a replacement for technical decision authority.

**Design work:** Explain why this component exists, what goes wrong without it, and the authority it should or should not possess. Verify these candidate statements; do not treat them as approved contracts.

## Workflow & conceptual interfaces

Describe the normal input → behavior → output flow; include ambiguous, denied, failed or incomplete paths when relevant.

| Input / trigger | Source | Conceptual behavior | Output / next component | Unknowns |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

**Scenario to develop:** A material ambiguity blocks planning, while a harmless default can proceed with an explicit assumption.

## Elements & ownership

One page per substantial element. The component owner coordinates; element owners write their page and reviewers check it. Listed contributors are suggestions, and other disciplines may join research. Reviewers must not co-author the material they independently review. Split, merge or move elements when the design requires it.

| Element | Owner | Contributors | Reviewer | Expected design output |
|---|---|---|---|---|
| [Clarification](ASK-CLARIFY) | UI/UX Designer & Mobile (Design Owner) | Frontend Engineer (Frontend Owner), Backend Engineer (Data & Persistence Owner) | AI Engineer & Research Lead | Uncertainty / question / response / resulting context |
| [Approval & Authorization](ASK-APPROVAL) | Cybersecurity & Backend Engineer (Security Owner) | UI/UX Designer & Mobile (Design Owner), AI Engineer & Research Lead | Technical Lead / Software Architect | Request / authority / scope / decision / validity |
| [Decision Context](ASK-DECISION) | AI Engineer & Research Lead | UI/UX Designer & Mobile (Design Owner), Backend Engineer (Data & Persistence Owner), Cybersecurity & Backend Engineer (Security Owner) | Technical Lead / Software Architect | Decision request / options / evidence / outcome / affected component |

## Expected component outputs

- Coherent purpose, responsibilities and exclusions.
- Reviewed conceptual workflow and input/output model with normal and failure examples.
- Element deliverables integrated into a consistent model; unresolved cross-element conflicts visible.
- Material questions and their impact, linked research and decisions; no silent assumptions.

## Open questions / blockers

The following are starter prompts, not confirmed blockers. The owner must classify them after discussion. Detailed question records live in the element pages.

| Question | Impact / affected element | Classification | Source |
|---|---|---|---|
| When is a question worth interrupting the user? | Clarification | To triage | [Question & work](ASK-CLARIFY) |
| Can user approval override system policy? | Approval & Authorization | To triage | [Question & work](ASK-APPROVAL) |
| How do we preserve which decision a downstream action relied on? | Decision Context | To triage | [Question & work](ASK-DECISION) |

## Dependencies & shared responsibilities

[Task Analysis](ANALYSIS) · [Task Planning](PLAN) · [Repair & Recovery](RECOVERY) · [Completion Gate](GATE) · [User Experience](UXD) · [Security & Trust](TRUST)

For each material dependency, record exchanged information, authority, failure behavior and any unresolved assumptions.

## Research & decisions

Link investigation notes and material decisions; write their effect on this component here. No decisions have been marked Agreed by this scaffold.

[Open Questions](QUESTIONS) · [Research Library](LIBRARY) · [Decision Log](DECISIONS)

## Implementation & Jira (later)

Only fill this when a relevant design slice is agreed and the scope is clear. Use the [Work Package & Jira Template](T-JIRA); Jira owns delivery status.

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
