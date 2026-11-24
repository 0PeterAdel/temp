# Experience Management

> **Page ID:** `EXP` · **Type:** Component workspace · **Phase:** Design now  
> **Status:** Not Started — scaffold; proposed role assignment only.

| Responsibility | Role |
|---|---|
| Owner | AI Engineer & Research Lead |
| Contributors | Backend Engineer (Data & Persistence Owner), Cybersecurity & Backend Engineer (Security Owner) |
| Reviewer | Technical Lead / Software Architect |
| Last reviewed / role confirmation | TBD — confirm during team assignment |

[Runtime Layers](../index.md) · [Architecture Overview](../../architecture-overview.md)

## Overview & current understanding

**Candidate vision:** Explore how validated lessons can be captured, qualified and reused in later tasks.

**Candidate boundary:** Own experience promotion and lifecycle; coordinate retrieval with shared memory rather than duplicating its authority.

**Design work:** Explain why this component exists, what goes wrong without it, and the authority it should or should not possess. Verify these candidate statements; do not treat them as approved contracts.

## Workflow & conceptual interfaces

Describe the normal input → behavior → output flow; include ambiguous, denied, failed or incomplete paths when relevant.

| Input / trigger | Source | Conceptual behavior | Output / next component | Unknowns |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

**Scenario to develop:** A prior repair lesson is retrieved for a similar task but may be obsolete after a version change.

## Elements & ownership

One page per substantial element. The component owner coordinates; element owners write their page and reviewers check it. Listed contributors are suggestions, and other disciplines may join research. Reviewers must not co-author the material they independently review. Split, merge or move elements when the design requires it.

| Element | Owner | Contributors | Reviewer | Expected design output |
|---|---|---|---|---|
| [Experience Model](model.md) | AI Engineer & Research Lead | Backend Engineer (Data & Persistence Owner) | Technical Lead / Software Architect | Lesson / context / evidence / applicability / version |
| [Experience Trust](trust.md) | Cybersecurity & Backend Engineer (Security Owner) | Backend Engineer (Data & Persistence Owner), Backend Lead | AI Engineer & Research Lead | Trust signal / evidence / scope / invalidation |
| [Experience Promotion](promotion.md) | AI Engineer & Research Lead | Backend Engineer (Data & Persistence Owner), Cybersecurity & Backend Engineer (Security Owner) | Technical Lead / Software Architect | Candidate / qualifying evidence / decision / expiry |
| [Retrieval & Reuse](reuse.md) | AI Engineer & Research Lead | Backend Engineer (Data & Persistence Owner), Cybersecurity & Backend Engineer (Security Owner), Frontend Engineer (Frontend Owner) | Technical Lead / Software Architect | Query / candidate / applicability / decision / provenance |

## Expected component outputs

- Coherent purpose, responsibilities and exclusions.
- Reviewed conceptual workflow and input/output model with normal and failure examples.
- Element deliverables integrated into a consistent model; unresolved cross-element conflicts visible.
- Material questions and their impact, linked research and decisions; no silent assumptions.

## Open questions / blockers

The following are starter prompts, not confirmed blockers. The owner must classify them after discussion. Detailed question records live in the element pages.

| Question | Impact / affected element | Classification | Source |
|---|---|---|---|
| What makes an execution history a reusable experience? | Experience Model | To triage | [Question & work](model.md) |
| What evidence is sufficient to trust a lesson? | Experience Trust | To triage | [Question & work](trust.md) |
| Can failure lessons be promoted without successful completion? | Experience Promotion | To triage | [Question & work](promotion.md) |
| How do we avoid reusing obsolete advice? | Retrieval & Reuse | To triage | [Question & work](reuse.md) |

## Dependencies & shared responsibilities

[Completion Gate](../completion-gate/index.md) · [Policy, Knowledge & Memory](../../shared-components/policy-knowledge-memory/index.md) · [Data & Storage](../../cross-system/data-storage/index.md) · [Security & Trust](../../cross-system/security-trust/index.md)

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
