# User Experience

> **Page ID:** `UXD` · **Type:** Component workspace · **Phase:** Design now  
> **Status:** Not Started — scaffold; proposed role assignment only.

| Responsibility | Role |
|---|---|
| Owner | UI/UX Designer & Mobile (Design Owner) |
| Contributors | AI Engineer & Research Lead, Product Owner, Backend Engineer (Data & Persistence Owner) |
| Reviewer | Frontend Engineer (Frontend Owner) |
| Last reviewed / role confirmation | TBD — confirm during team assignment |

[Cross-System Design](CROSS) · [Architecture Overview](ARCH)

## Overview & current understanding

**Candidate vision:** Describe how users create, understand, monitor and interact with tasks, uncertainty and outcomes.

**Candidate boundary:** Own interaction and usability concepts; do not define backend authority or imply capabilities not agreed.

**Design work:** Explain why this component exists, what goes wrong without it, and the authority it should or should not possess. Verify these candidate statements; do not treat them as approved contracts.

## Workflow & conceptual interfaces

Describe the normal input → behavior → output flow; include ambiguous, denied, failed or incomplete paths when relevant.

| Input / trigger | Source | Conceptual behavior | Output / next component | Unknowns |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

**Scenario to develop:** A user sees a clarification request, execution progress and a rejected completion result.

## Elements & ownership

One page per substantial element. The component owner coordinates; element owners write their page and reviewers check it. Listed contributors are suggestions, and other disciplines may join research. Reviewers must not co-author the material they independently review. Split, merge or move elements when the design requires it.

| Element | Owner | Contributors | Reviewer | Expected design output |
|---|---|---|---|---|
| [User Journeys & Information Architecture](UXD-JOURNEYS) | UI/UX Designer & Mobile (Design Owner) | Product Owner, AI Engineer & Research Lead | Frontend Engineer (Frontend Owner) | Journey / goal / screen or state / action / feedback |
| [Interaction & State Design](UXD-INTERACTIONS) | Frontend Engineer (Frontend Owner) | Backend Engineer (Data & Persistence Owner), AI Engineer & Research Lead | UI/UX Designer & Mobile (Design Owner) | UI state / trigger / content / action / accessibility |
| [Frontend Concept & Integration](UXD-FRONTEND) | Frontend Engineer (Frontend Owner) | UI/UX Designer & Mobile (Design Owner), Backend Engineer (Data & Persistence Owner) | Technical Lead / Software Architect | Screen / data need / interaction / service dependency |

## Expected component outputs

- Coherent purpose, responsibilities and exclusions.
- Reviewed conceptual workflow and input/output model with normal and failure examples.
- Element deliverables integrated into a consistent model; unresolved cross-element conflicts visible.
- Material questions and their impact, linked research and decisions; no silent assumptions.

## Open questions / blockers

The following are starter prompts, not confirmed blockers. The owner must classify them after discussion. Detailed question records live in the element pages.

| Question | Impact / affected element | Classification | Source |
|---|---|---|---|
| What details should be visible by default? | User Journeys & Information Architecture | To triage | [Question & work](UXD-JOURNEYS) |
| How do we distinguish execution success from task completion in the UI? | Interaction & State Design | To triage | [Question & work](UXD-INTERACTIONS) |
| What state should be server-authoritative? | Frontend Concept & Integration | To triage | [Question & work](UXD-FRONTEND) |

## Dependencies & shared responsibilities

[Task Creation](TASK) · [Ask & Decide](ASK) · [Task Execution](EXEC) · [Completion Gate](GATE)

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
