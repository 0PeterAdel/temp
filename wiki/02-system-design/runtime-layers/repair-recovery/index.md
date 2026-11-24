# Repair & Recovery

> **Page ID:** `RECOVERY` · **Type:** Component workspace · **Phase:** Design now  
> **Status:** Not Started — scaffold; proposed role assignment only.

| Responsibility | Role |
|---|---|
| Owner | Backend Lead |
| Contributors | Backend Engineer (Data & Persistence Owner), Cybersecurity & Backend Engineer (Security Owner), DevOps Engineer (Infrastructure Owner) |
| Reviewer | AI Engineer & Research Lead |
| Last reviewed / role confirmation | TBD — confirm during team assignment |

[Runtime Layers](../index.md) · [Architecture Overview](../../architecture-overview.md)

## Overview & current understanding

**Candidate vision:** Explore bounded diagnosis and correction after execution or verification failure.

**Candidate boundary:** Recommend or coordinate repair within policy; do not retry indefinitely or erase prior attempts.

**Design work:** Explain why this component exists, what goes wrong without it, and the authority it should or should not possess. Verify these candidate statements; do not treat them as approved contracts.

## Workflow & conceptual interfaces

Describe the normal input → behavior → output flow; include ambiguous, denied, failed or incomplete paths when relevant.

| Input / trigger | Source | Conceptual behavior | Output / next component | Unknowns |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

**Scenario to develop:** A failed verification check triggers a targeted repair instead of rerunning every step.

## Elements & ownership

One page per substantial element. The component owner coordinates; element owners write their page and reviewers check it. Listed contributors are suggestions, and other disciplines may join research. Reviewers must not co-author the material they independently review. Split, merge or move elements when the design requires it.

| Element | Owner | Contributors | Reviewer | Expected design output |
|---|---|---|---|---|
| [Failure Diagnosis](diagnosis.md) | AI Engineer & Research Lead | Backend Engineer (Data & Persistence Owner), Cybersecurity & Backend Engineer (Security Owner) | Technical Lead / Software Architect | Failure / evidence / suspected cause / confidence / next action |
| [Repair Strategies](strategy.md) | Backend Lead | Backend Engineer (Data & Persistence Owner) | AI Engineer & Research Lead | Failure class / repair option / impact / recheck |
| [Recovery Limits](limits.md) | Cybersecurity & Backend Engineer (Security Owner) | AI Engineer & Research Lead, DevOps Engineer (Infrastructure Owner) | Technical Lead / Software Architect | Limit / trigger / stop behavior / authority |
| [Escalation & Human Decisions](escalation.md) | UI/UX Designer & Mobile (Design Owner) | AI Engineer & Research Lead, Frontend Engineer (Frontend Owner), Cybersecurity & Backend Engineer (Security Owner) | Technical Lead / Software Architect | Trigger / recipient / evidence / options / resulting state |

## Expected component outputs

- Coherent purpose, responsibilities and exclusions.
- Reviewed conceptual workflow and input/output model with normal and failure examples.
- Element deliverables integrated into a consistent model; unresolved cross-element conflicts visible.
- Material questions and their impact, linked research and decisions; no silent assumptions.

## Open questions / blockers

The following are starter prompts, not confirmed blockers. The owner must classify them after discussion. Detailed question records live in the element pages.

| Question | Impact / affected element | Classification | Source |
|---|---|---|---|
| How do we distinguish a faulty result from a faulty verifier? | Failure Diagnosis | To triage | [Question & work](diagnosis.md) |
| When is replanning necessary instead of repairing a step? | Repair Strategies | To triage | [Question & work](strategy.md) |
| Which events require immediate stop rather than retry? | Recovery Limits | To triage | [Question & work](limits.md) |
| When must a human authorize a new recovery scope? | Escalation & Human Decisions | To triage | [Question & work](escalation.md) |

## Dependencies & shared responsibilities

[Task Execution](../task-execution/index.md) · [Verification & Evaluation](../verification-evaluation/index.md) · [Completion Gate](../completion-gate/index.md) · [Ask & Decide](../../shared-components/ask-decide/index.md) · [Policy, Knowledge & Memory](../../shared-components/policy-knowledge-memory/index.md)

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
