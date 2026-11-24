# Policy, Knowledge & Memory

> **Page ID:** `PKM` · **Type:** Component workspace · **Phase:** Design now  
> **Status:** Not Started — scaffold; proposed role assignment only.

| Responsibility | Role |
|---|---|
| Owner | AI Engineer & Research Lead |
| Contributors | Backend Engineer (Data & Persistence Owner), Backend Lead |
| Reviewer | Cybersecurity & Backend Engineer (Security Owner) |
| Last reviewed / role confirmation | TBD — confirm during team assignment |

[Shared Components](../index.md) · [Architecture Overview](../../architecture-overview.md)

## Overview & current understanding

**Candidate vision:** Explore how policies, trusted knowledge and memory are supplied to authorized components with clear provenance.

**Candidate boundary:** Shared capability, not a mandatory stage; distinguish memory access from experience promotion and policy enforcement.

**Design work:** Explain why this component exists, what goes wrong without it, and the authority it should or should not possess. Verify these candidate statements; do not treat them as approved contracts.

## Workflow & conceptual interfaces

Describe the normal input → behavior → output flow; include ambiguous, denied, failed or incomplete paths when relevant.

| Input / trigger | Source | Conceptual behavior | Output / next component | Unknowns |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

**Scenario to develop:** Retrieve a versioned policy and relevant lesson; detect conflicting or stale context before use.

## Elements & ownership

One page per substantial element. The component owner coordinates; element owners write their page and reviewers check it. Listed contributors are suggestions, and other disciplines may join research. Reviewers must not co-author the material they independently review. Split, merge or move elements when the design requires it.

| Element | Owner | Contributors | Reviewer | Expected design output |
|---|---|---|---|---|
| [Policies & Constraints](policy.md) | Cybersecurity & Backend Engineer (Security Owner) | AI Engineer & Research Lead, DevOps Engineer (Infrastructure Owner) | Technical Lead / Software Architect | Policy / owner / scope / precedence / enforcement |
| [Knowledge Sources](knowledge.md) | AI Engineer & Research Lead | Backend Engineer (Data & Persistence Owner), Cybersecurity & Backend Engineer (Security Owner), Frontend Engineer (Frontend Owner) | Technical Lead / Software Architect | Source / scope / trust / freshness / citation |
| [Memory Model](memory.md) | Backend Engineer (Data & Persistence Owner) | Cybersecurity & Backend Engineer (Security Owner), Backend Lead | AI Engineer & Research Lead | Memory type / scope / lifetime / provenance / access |
| [Retrieval & Context Assembly](retrieval.md) | AI Engineer & Research Lead | Backend Engineer (Data & Persistence Owner), Cybersecurity & Backend Engineer (Security Owner) | Technical Lead / Software Architect | Query / filter / result / trust / downstream use |

## Expected component outputs

- Coherent purpose, responsibilities and exclusions.
- Reviewed conceptual workflow and input/output model with normal and failure examples.
- Element deliverables integrated into a consistent model; unresolved cross-element conflicts visible.
- Material questions and their impact, linked research and decisions; no silent assumptions.

## Open questions / blockers

The following are starter prompts, not confirmed blockers. The owner must classify them after discussion. Detailed question records live in the element pages.

| Question | Impact / affected element | Classification | Source |
|---|---|---|---|
| How should conflicting policies be resolved? | Policies & Constraints | To triage | [Question & work](policy.md) |
| How should retrieved external knowledge be distinguished from facts supplied by the user? | Knowledge Sources | To triage | [Question & work](knowledge.md) |
| What should persist after a task ends? | Memory Model | To triage | [Question & work](memory.md) |
| When should retrieved material be excluded despite high relevance? | Retrieval & Context Assembly | To triage | [Question & work](retrieval.md) |

## Dependencies & shared responsibilities

[Experience Management](../../runtime-layers/experience-management/index.md) · [Security & Trust](../../cross-system/security-trust/index.md) · [Data & Storage](../../cross-system/data-storage/index.md) · [Task Analysis](../../runtime-layers/task-analysis/index.md) · [Task Planning](../../runtime-layers/task-planning/index.md)

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
