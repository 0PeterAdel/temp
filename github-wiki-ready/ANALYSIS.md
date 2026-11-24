# Task Analysis

> **Page ID:** `ANALYSIS` · **Type:** Component workspace · **Phase:** Design now  
> **Status:** Not Started — scaffold; proposed role assignment only.

| Responsibility | Role |
|---|---|
| Owner | AI Engineer & Research Lead |
| Contributors | Backend Engineer (Data & Persistence Owner), UI/UX Designer & Mobile (Design Owner), Frontend Engineer (Frontend Owner) |
| Reviewer | Technical Lead / Software Architect |
| Last reviewed / role confirmation | TBD — confirm during team assignment |

[Runtime Layers](LAYERS) · [Architecture Overview](ARCH)

## Overview & current understanding

**Candidate vision:** Develop a shared understanding of intent, requirements, constraints, and uncertainty before planning.

**Candidate boundary:** Describe and clarify the problem; do not choose an execution plan or treat assumptions as facts.

**Design work:** Explain why this component exists, what goes wrong without it, and the authority it should or should not possess. Verify these candidate statements; do not treat them as approved contracts.

## Workflow & conceptual interfaces

Describe the normal input → behavior → output flow; include ambiguous, denied, failed or incomplete paths when relevant.

| Input / trigger | Source | Conceptual behavior | Output / next component | Unknowns |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

**Scenario to develop:** A request to fix login is ambiguous about the affected environment and expected behavior.

## Elements & ownership

One page per substantial element. The component owner coordinates; element owners write their page and reviewers check it. Listed contributors are suggestions, and other disciplines may join research. Reviewers must not co-author the material they independently review. Split, merge or move elements when the design requires it.

| Element | Owner | Contributors | Reviewer | Expected design output |
|---|---|---|---|---|
| [Intent Understanding](ANALYSIS-INTENT) | AI Engineer & Research Lead | UI/UX Designer & Mobile (Design Owner), Backend Engineer (Data & Persistence Owner), Frontend Engineer (Frontend Owner) | Technical Lead / Software Architect | Raw request / interpretation / evidence / uncertainty |
| [Requirements & Constraints](ANALYSIS-REQUIREMENTS) | AI Engineer & Research Lead | UI/UX Designer & Mobile (Design Owner), Backend Engineer (Data & Persistence Owner) | Technical Lead / Software Architect | Requirement / source / constraint / proposed success measure |
| [Context Discovery](ANALYSIS-CONTEXT) | Backend Engineer (Data & Persistence Owner) | Cybersecurity & Backend Engineer (Security Owner) | AI Engineer & Research Lead | Context / source / freshness / authorization / relevance |
| [Uncertainty & Clarification](ANALYSIS-UNCERTAINTY) | UI/UX Designer & Mobile (Design Owner) | AI Engineer & Research Lead, Frontend Engineer (Frontend Owner), Cybersecurity & Backend Engineer (Security Owner) | Technical Lead / Software Architect | Question / impact / default / confirmation requirement |

## Expected component outputs

- Coherent purpose, responsibilities and exclusions.
- Reviewed conceptual workflow and input/output model with normal and failure examples.
- Element deliverables integrated into a consistent model; unresolved cross-element conflicts visible.
- Material questions and their impact, linked research and decisions; no silent assumptions.

## Open questions / blockers

The following are starter prompts, not confirmed blockers. The owner must classify them after discussion. Detailed question records live in the element pages.

| Question | Impact / affected element | Classification | Source |
|---|---|---|---|
| How should intent be inferred without silently changing the request? | Intent Understanding | To triage | [Question & work](ANALYSIS-INTENT) |
| Who confirms inferred success criteria? | Requirements & Constraints | To triage | [Question & work](ANALYSIS-REQUIREMENTS) |
| Which sources may be read before clarification? | Context Discovery | To triage | [Question & work](ANALYSIS-CONTEXT) |
| What uncertainty blocks a safe plan? | Uncertainty & Clarification | To triage | [Question & work](ANALYSIS-UNCERTAINTY) |

## Dependencies & shared responsibilities

[Task Creation](TASK) · [Ask & Decide](ASK) · [Policy, Knowledge & Memory](PKM) · [Task Planning](PLAN)

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
