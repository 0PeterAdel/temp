# Open Questions

> **Page ID:** `QUESTIONS` · **Type:** Guide / working page · **Phase:** Design now  
> **Status:** Not Started — scaffold; proposed role assignment only.

| Responsibility | Role |
|---|---|
| Owner | AI Engineer & Research Lead |
| Contributors | Backend Engineer (Data & Persistence Owner), Cybersecurity & Backend Engineer (Security Owner), DevOps Engineer (Infrastructure Owner), Frontend Engineer (Frontend Owner), UI/UX Designer & Mobile (Design Owner) |
| Reviewer | Technical Lead / Software Architect |
| Last reviewed / role confirmation | TBD — confirm during team assignment |

> **Objective:** Index material questions at their discovery page; do not maintain duplicate question details.

## How to complete this page

Write in English. Replace prompts with actual findings; keep unresolved questions visible. Use short paragraphs, tables and diagrams only when they improve understanding. Label evidence, assumptions and proposals separately.

## Question index

**Required work:** Link the canonical question row inside an element or component. Identify blocking scope, owner role and research link when assigned.

**Expected output / writing format:** ID / question / affected element / impact / source link.

**Working content:** _To be developed by the owner and contributors._

## Triage

**Required work:** Use Blocking, Non-blocking or Deferred; explain what work is affected and keep unrelated work moving.

**Expected output / writing format:** Impact / rationale / next action.

**Working content:** _To be developed by the owner and contributors._

## Closure

**Required work:** When a question is answered, update the origin and link findings and decision; retain unresolved uncertainty.

**Expected output / writing format:** Answer / supporting evidence / remaining uncertainty / source link.

**Working content:** _To be developed by the owner and contributors._

## Review checklist

- [ ] All required outputs above are present or explicitly marked not applicable with a reason.
- [ ] Claims are supported; proposed material and unknowns are marked.
- [ ] A different person reviews the page, including relevant domain specialists if needed.
- [ ] Links to impacted design, research and decisions are current.

## Related pages

[Research & Decisions](index.md) · [Shift Core — Home](../Home.md)

## Starter question index (all untriaged prompts)

Open the element for current wording, classification, ownership and research link. These are suggestions for exploration, not confirmed blockers.

| Originating question ID | Element | Owner |
|---|---|---|
| `TASK-INPUT-Q01` | [Task Input](../02-system-design/runtime-layers/task-creation/input.md) | UI/UX Designer & Mobile (Design Owner) |
| `TASK-IDENTITY-Q01` | [Task Identity](../02-system-design/runtime-layers/task-creation/identity.md) | Backend Engineer (Data & Persistence Owner) |
| `TASK-CONTEXT-Q01` | [Initial Context](../02-system-design/runtime-layers/task-creation/context.md) | Backend Engineer (Data & Persistence Owner) |
| `TASK-INTERACTION-Q01` | [User Interaction](../02-system-design/runtime-layers/task-creation/interaction.md) | Frontend Engineer (Frontend Owner) |
| `ANALYSIS-INTENT-Q01` | [Intent Understanding](../02-system-design/runtime-layers/task-analysis/intent.md) | AI Engineer & Research Lead |
| `ANALYSIS-REQUIREMENTS-Q01` | [Requirements & Constraints](../02-system-design/runtime-layers/task-analysis/requirements.md) | AI Engineer & Research Lead |
| `ANALYSIS-CONTEXT-Q01` | [Context Discovery](../02-system-design/runtime-layers/task-analysis/context.md) | Backend Engineer (Data & Persistence Owner) |
| `ANALYSIS-UNCERTAINTY-Q01` | [Uncertainty & Clarification](../02-system-design/runtime-layers/task-analysis/uncertainty.md) | UI/UX Designer & Mobile (Design Owner) |
| `PLAN-DECOMPOSITION-Q01` | [Dynamic Task Decomposition](../02-system-design/runtime-layers/task-planning/decomposition.md) | AI Engineer & Research Lead |
| `PLAN-DEPENDENCIES-Q01` | [Dependencies & Ordering](../02-system-design/runtime-layers/task-planning/dependencies.md) | Backend Lead |
| `PLAN-RESOURCES-Q01` | [Agent, Skill & Resource Selection](../02-system-design/runtime-layers/task-planning/resources.md) | AI Engineer & Research Lead |
| `PLAN-VALIDATION-Q01` | [Plan Validation & Acceptance](../02-system-design/runtime-layers/task-planning/validation.md) | Backend Lead |
| `PREP-READINESS-Q01` | [Environment Readiness](../02-system-design/runtime-layers/task-preparation/readiness.md) | DevOps Engineer (Infrastructure Owner) |
| `PREP-RESOURCES-Q01` | [Resource Preparation](../02-system-design/runtime-layers/task-preparation/resources.md) | Backend Lead |
| `PREP-PERMISSIONS-Q01` | [Permissions & Isolation Preconditions](../02-system-design/runtime-layers/task-preparation/permissions.md) | Cybersecurity & Backend Engineer (Security Owner) |
| `PREP-PRECONDITIONS-Q01` | [Preconditions & Handoff](../02-system-design/runtime-layers/task-preparation/preconditions.md) | Backend Engineer (Data & Persistence Owner) |
| `EXEC-MODEL-Q01` | [Execution Model & Boundaries](../02-system-design/runtime-layers/task-execution/model.md) | AI Engineer & Research Lead |
| `EXEC-ADAPTERS-Q01` | [Agents & Runtime Adapters](../02-system-design/runtime-layers/task-execution/adapters.md) | Backend Lead |
| `EXEC-TOOLS-Q01` | [Tools & Permissions](../02-system-design/runtime-layers/task-execution/tools.md) | Cybersecurity & Backend Engineer (Security Owner) |
| `EXEC-ENV-Q01` | [Execution Environment](../02-system-design/runtime-layers/task-execution/env.md) | DevOps Engineer (Infrastructure Owner) |
| `EXEC-STATE-Q01` | [Execution State & Control](../02-system-design/runtime-layers/task-execution/state.md) | Backend Engineer (Data & Persistence Owner) |
| `EXEC-OUTPUT-Q01` | [Outputs & Evidence](../02-system-design/runtime-layers/task-execution/output.md) | Backend Engineer (Data & Persistence Owner) |
| `EXEC-MONITOR-Q01` | [Execution Monitoring & User Interaction](../02-system-design/runtime-layers/task-execution/monitor.md) | Frontend Engineer (Frontend Owner) |
| `VERIFY-EVIDENCE-Q01` | [Evidence Model & Provenance](../02-system-design/runtime-layers/verification-evaluation/evidence.md) | Backend Engineer (Data & Persistence Owner) |
| `VERIFY-CHECKS-Q01` | [Independent Checks](../02-system-design/runtime-layers/verification-evaluation/checks.md) | Cybersecurity & Backend Engineer (Security Owner) |
| `VERIFY-CRITERIA-Q01` | [Evaluation Criteria](../02-system-design/runtime-layers/verification-evaluation/criteria.md) | AI Engineer & Research Lead |
| `VERIFY-RESULTS-Q01` | [Verification Results](../02-system-design/runtime-layers/verification-evaluation/results.md) | AI Engineer & Research Lead |
| `RECOVERY-DIAGNOSIS-Q01` | [Failure Diagnosis](../02-system-design/runtime-layers/repair-recovery/diagnosis.md) | AI Engineer & Research Lead |
| `RECOVERY-STRATEGY-Q01` | [Repair Strategies](../02-system-design/runtime-layers/repair-recovery/strategy.md) | Backend Lead |
| `RECOVERY-LIMITS-Q01` | [Recovery Limits](../02-system-design/runtime-layers/repair-recovery/limits.md) | Cybersecurity & Backend Engineer (Security Owner) |
| `RECOVERY-ESCALATION-Q01` | [Escalation & Human Decisions](../02-system-design/runtime-layers/repair-recovery/escalation.md) | UI/UX Designer & Mobile (Design Owner) |
| `GATE-CRITERIA-Q01` | [Completion Criteria](../02-system-design/runtime-layers/completion-gate/criteria.md) | AI Engineer & Research Lead |
| `GATE-AUTHORITY-Q01` | [Decision Authority](../02-system-design/runtime-layers/completion-gate/authority.md) | Backend Engineer (Data & Persistence Owner) |
| `GATE-OUTCOMES-Q01` | [Completion Outcomes](../02-system-design/runtime-layers/completion-gate/outcomes.md) | Backend Engineer (Data & Persistence Owner) |
| `EXP-MODEL-Q01` | [Experience Model](../02-system-design/runtime-layers/experience-management/model.md) | AI Engineer & Research Lead |
| `EXP-TRUST-Q01` | [Experience Trust](../02-system-design/runtime-layers/experience-management/trust.md) | Cybersecurity & Backend Engineer (Security Owner) |
| `EXP-PROMOTION-Q01` | [Experience Promotion](../02-system-design/runtime-layers/experience-management/promotion.md) | AI Engineer & Research Lead |
| `EXP-REUSE-Q01` | [Retrieval & Reuse](../02-system-design/runtime-layers/experience-management/reuse.md) | AI Engineer & Research Lead |
| `ASK-CLARIFY-Q01` | [Clarification](../02-system-design/shared-components/ask-decide/clarify.md) | UI/UX Designer & Mobile (Design Owner) |
| `ASK-APPROVAL-Q01` | [Approval & Authorization](../02-system-design/shared-components/ask-decide/approval.md) | Cybersecurity & Backend Engineer (Security Owner) |
| `ASK-DECISION-Q01` | [Decision Context](../02-system-design/shared-components/ask-decide/decision.md) | AI Engineer & Research Lead |
| `PKM-POLICY-Q01` | [Policies & Constraints](../02-system-design/shared-components/policy-knowledge-memory/policy.md) | Cybersecurity & Backend Engineer (Security Owner) |
| `PKM-KNOWLEDGE-Q01` | [Knowledge Sources](../02-system-design/shared-components/policy-knowledge-memory/knowledge.md) | AI Engineer & Research Lead |
| `PKM-MEMORY-Q01` | [Memory Model](../02-system-design/shared-components/policy-knowledge-memory/memory.md) | Backend Engineer (Data & Persistence Owner) |
| `PKM-RETRIEVAL-Q01` | [Retrieval & Context Assembly](../02-system-design/shared-components/policy-knowledge-memory/retrieval.md) | AI Engineer & Research Lead |
| `DATA-MODEL-Q01` | [Conceptual Data Model](../02-system-design/cross-system/data-storage/model.md) | Backend Engineer (Data & Persistence Owner) |
| `DATA-LIFECYCLE-Q01` | [Data Lifecycle & Retention](../02-system-design/cross-system/data-storage/lifecycle.md) | Backend Engineer (Data & Persistence Owner) |
| `DATA-CONSISTENCY-Q01` | [Consistency & Storage Boundaries](../02-system-design/cross-system/data-storage/consistency.md) | Backend Lead |
| `TRUST-THREATS-Q01` | [Threat Model & Trust Boundaries](../02-system-design/cross-system/security-trust/threats.md) | Cybersecurity & Backend Engineer (Security Owner) |
| `TRUST-IDENTITY-Q01` | [Identity & Authorization](../02-system-design/cross-system/security-trust/identity.md) | Cybersecurity & Backend Engineer (Security Owner) |
| `TRUST-ISOLATION-Q01` | [Isolation & Safety Controls](../02-system-design/cross-system/security-trust/isolation.md) | Cybersecurity & Backend Engineer (Security Owner) |
| `UXD-JOURNEYS-Q01` | [User Journeys & Information Architecture](../02-system-design/cross-system/user-experience/journeys.md) | UI/UX Designer & Mobile (Design Owner) |
| `UXD-INTERACTIONS-Q01` | [Interaction & State Design](../02-system-design/cross-system/user-experience/interactions.md) | Frontend Engineer (Frontend Owner) |
| `UXD-FRONTEND-Q01` | [Frontend Concept & Integration](../02-system-design/cross-system/user-experience/frontend.md) | Frontend Engineer (Frontend Owner) |
| `INFRA-TOPOLOGY-Q01` | [Environment & Deployment Topology](../02-system-design/cross-system/infrastructure-deployment/topology.md) | DevOps Engineer (Infrastructure Owner) |
| `INFRA-OPERATIONS-Q01` | [Observability & Operations](../02-system-design/cross-system/infrastructure-deployment/operations.md) | DevOps Engineer (Infrastructure Owner) |
| `INFRA-DELIVERY-Q01` | [Delivery & Environment Reproducibility](../02-system-design/cross-system/infrastructure-deployment/delivery.md) | DevOps Engineer (Infrastructure Owner) |
