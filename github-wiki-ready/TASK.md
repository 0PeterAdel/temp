# Task Creation

> **Page ID:** `TASK` · **Type:** Component workspace · **Phase:** Design now  
> **Status:** Not Started — scaffold; proposed role assignment only.

| Responsibility | Role |
|---|---|
| Owner | Backend Engineer (Data & Persistence Owner) |
| Contributors | UI/UX Designer & Mobile (Design Owner), Frontend Engineer (Frontend Owner), AI Engineer & Research Lead |
| Reviewer | Technical Lead / Software Architect |
| Last reviewed / role confirmation | TBD — confirm during team assignment |

[Runtime Layers](LAYERS) · [Architecture Overview](ARCH)

## Overview & current understanding

**Candidate vision:** Capture a task and its original request with sufficient identity and context to begin analysis.

**Candidate boundary:** Capture and acknowledge; do not infer requirements, approve a plan, or execute work.

**Design work:** Explain why this component exists, what goes wrong without it, and the authority it should or should not possess. Verify these candidate statements; do not treat them as approved contracts.

## Workflow & conceptual interfaces

Describe the normal input → behavior → output flow; include ambiguous, denied, failed or incomplete paths when relevant.

| Input / trigger | Source | Conceptual behavior | Output / next component | Unknowns |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

**Scenario to develop:** A user submits a bug report with a repository reference and an attachment.

## Elements & ownership

One page per substantial element. The component owner coordinates; element owners write their page and reviewers check it. Listed contributors are suggestions, and other disciplines may join research. Reviewers must not co-author the material they independently review. Split, merge or move elements when the design requires it.

| Element | Owner | Contributors | Reviewer | Expected design output |
|---|---|---|---|---|
| [Task Input](TASK-INPUT) | UI/UX Designer & Mobile (Design Owner) | Frontend Engineer (Frontend Owner), AI Engineer & Research Lead | Backend Engineer (Data & Persistence Owner) | Input type / source / validation / rejection reason |
| [Task Identity](TASK-IDENTITY) | Backend Engineer (Data & Persistence Owner) | Cybersecurity & Backend Engineer (Security Owner) | Technical Lead / Software Architect | Identity concept / uniqueness scope / duplicate behavior |
| [Initial Context](TASK-CONTEXT) | Backend Engineer (Data & Persistence Owner) | UI/UX Designer & Mobile (Design Owner), Cybersecurity & Backend Engineer (Security Owner) | AI Engineer & Research Lead | Context type / origin / trust / missing behavior |
| [User Interaction](TASK-INTERACTION) | Frontend Engineer (Frontend Owner) | AI Engineer & Research Lead | UI/UX Designer & Mobile (Design Owner) | State / user action / feedback / next state |

## Expected component outputs

- Coherent purpose, responsibilities and exclusions.
- Reviewed conceptual workflow and input/output model with normal and failure examples.
- Element deliverables integrated into a consistent model; unresolved cross-element conflicts visible.
- Material questions and their impact, linked research and decisions; no silent assumptions.

## Open questions / blockers

The following are starter prompts, not confirmed blockers. The owner must classify them after discussion. Detailed question records live in the element pages.

| Question | Impact / affected element | Classification | Source |
|---|---|---|---|
| Which input forms belong in the initial scope? | Task Input | To triage | [Question & work](TASK-INPUT) |
| What counts as the same submission? | Task Identity | To triage | [Question & work](TASK-IDENTITY) |
| When should context be captured versus retrieved later? | Initial Context | To triage | [Question & work](TASK-CONTEXT) |
| What does the user need to know before submission? | User Interaction | To triage | [Question & work](TASK-INTERACTION) |

## Dependencies & shared responsibilities

[Task Analysis](ANALYSIS) · [Ask & Decide](ASK) · [Data & Storage](DATA) · [User Experience](UXD)

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
