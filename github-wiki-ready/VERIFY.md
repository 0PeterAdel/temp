# Verification & Evaluation

> **Page ID:** `VERIFY` · **Type:** Component workspace · **Phase:** Design now  
> **Status:** Not Started — scaffold; proposed role assignment only.

| Responsibility | Role |
|---|---|
| Owner | AI Engineer & Research Lead |
| Contributors | Backend Engineer (Data & Persistence Owner), Backend Lead, Frontend Engineer (Frontend Owner) |
| Reviewer | Cybersecurity & Backend Engineer (Security Owner) |
| Last reviewed / role confirmation | TBD — confirm during team assignment |

[Runtime Layers](LAYERS) · [Architecture Overview](ARCH)

## Overview & current understanding

**Candidate vision:** Assess task outputs against agreed criteria using evidence with meaningful independence.

**Candidate boundary:** Evaluate the candidate and evidence; do not silently redefine the criteria or own the final completion decision.

**Design work:** Explain why this component exists, what goes wrong without it, and the authority it should or should not possess. Verify these candidate statements; do not treat them as approved contracts.

## Workflow & conceptual interfaces

Describe the normal input → behavior → output flow; include ambiguous, denied, failed or incomplete paths when relevant.

| Input / trigger | Source | Conceptual behavior | Output / next component | Unknowns |
|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD |

**Scenario to develop:** An executor reports success, but an independent check discovers an unmet requirement.

## Elements & ownership

One page per substantial element. The component owner coordinates; element owners write their page and reviewers check it. Listed contributors are suggestions, and other disciplines may join research. Reviewers must not co-author the material they independently review. Split, merge or move elements when the design requires it.

| Element | Owner | Contributors | Reviewer | Expected design output |
|---|---|---|---|---|
| [Evidence Model & Provenance](VERIFY-EVIDENCE) | Backend Engineer (Data & Persistence Owner) | AI Engineer & Research Lead, Backend Lead | Cybersecurity & Backend Engineer (Security Owner) | Evidence type / source / binding / trust / validation |
| [Independent Checks](VERIFY-CHECKS) | Cybersecurity & Backend Engineer (Security Owner) | AI Engineer & Research Lead, Backend Engineer (Data & Persistence Owner), Frontend Engineer (Frontend Owner) | Technical Lead / Software Architect | Check / author / runner / isolation / independence claim |
| [Evaluation Criteria](VERIFY-CRITERIA) | AI Engineer & Research Lead | UI/UX Designer & Mobile (Design Owner), Backend Engineer (Data & Persistence Owner) | Technical Lead / Software Architect | Requirement / criterion / evidence / method / ambiguity |
| [Verification Results](VERIFY-RESULTS) | AI Engineer & Research Lead | Backend Engineer (Data & Persistence Owner), Backend Lead | Cybersecurity & Backend Engineer (Security Owner) | Criterion / result / evidence / confidence limitation / next action |

## Expected component outputs

- Coherent purpose, responsibilities and exclusions.
- Reviewed conceptual workflow and input/output model with normal and failure examples.
- Element deliverables integrated into a consistent model; unresolved cross-element conflicts visible.
- Material questions and their impact, linked research and decisions; no silent assumptions.

## Open questions / blockers

The following are starter prompts, not confirmed blockers. The owner must classify them after discussion. Detailed question records live in the element pages.

| Question | Impact / affected element | Classification | Source |
|---|---|---|---|
| What evidence is sufficient for each kind of claim? | Evidence Model & Provenance | To triage | [Question & work](VERIFY-EVIDENCE) |
| Is independently rerunning executor-authored tests sufficient? | Independent Checks | To triage | [Question & work](VERIFY-CHECKS) |
| How can criteria be defined before seeing candidate outputs? | Evaluation Criteria | To triage | [Question & work](VERIFY-CRITERIA) |
| How should conflicting check results be handled? | Verification Results | To triage | [Question & work](VERIFY-RESULTS) |

## Dependencies & shared responsibilities

[Task Planning](PLAN) · [Task Execution](EXEC) · [Completion Gate](GATE) · [Repair & Recovery](RECOVERY) · [Security & Trust](TRUST)

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
