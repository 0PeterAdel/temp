# Complete editable Wiki structure

Start at [Home](wiki/Home.md). Each page includes role-based ownership. Each component links its own elements; the sidebar shows only the major navigation.

```text
wiki/
├── _Footer.md
├── _Sidebar.md
├── Home.md
├── 01-project/
│   ├── index.md
│   ├── problem-vision.md
│   ├── project-overview.md
│   ├── requirements-scope.md
│   └── use-cases.md
├── 02-system-design/
│   ├── index.md
│   ├── architecture-overview.md
│   ├── cross-system/
│   │   ├── index.md
│   │   ├── data-storage/
│   │   │   ├── index.md
│   │   │   ├── consistency.md
│   │   │   ├── lifecycle.md
│   │   │   └── model.md
│   │   ├── infrastructure-deployment/
│   │   │   ├── index.md
│   │   │   ├── delivery.md
│   │   │   ├── operations.md
│   │   │   └── topology.md
│   │   ├── security-trust/
│   │   │   ├── index.md
│   │   │   ├── identity.md
│   │   │   ├── isolation.md
│   │   │   └── threats.md
│   │   └── user-experience/
│   │       ├── index.md
│   │       ├── frontend.md
│   │       ├── interactions.md
│   │       └── journeys.md
│   ├── runtime-layers/
│   │   ├── index.md
│   │   ├── completion-gate/
│   │   │   ├── index.md
│   │   │   ├── authority.md
│   │   │   ├── criteria.md
│   │   │   └── outcomes.md
│   │   ├── experience-management/
│   │   │   ├── index.md
│   │   │   ├── model.md
│   │   │   ├── promotion.md
│   │   │   ├── reuse.md
│   │   │   └── trust.md
│   │   ├── repair-recovery/
│   │   │   ├── index.md
│   │   │   ├── diagnosis.md
│   │   │   ├── escalation.md
│   │   │   ├── limits.md
│   │   │   └── strategy.md
│   │   ├── task-analysis/
│   │   │   ├── index.md
│   │   │   ├── context.md
│   │   │   ├── intent.md
│   │   │   ├── requirements.md
│   │   │   └── uncertainty.md
│   │   ├── task-creation/
│   │   │   ├── index.md
│   │   │   ├── context.md
│   │   │   ├── identity.md
│   │   │   ├── input.md
│   │   │   └── interaction.md
│   │   ├── task-execution/
│   │   │   ├── index.md
│   │   │   ├── adapters.md
│   │   │   ├── env.md
│   │   │   ├── model.md
│   │   │   ├── monitor.md
│   │   │   ├── output.md
│   │   │   ├── state.md
│   │   │   └── tools.md
│   │   ├── task-planning/
│   │   │   ├── index.md
│   │   │   ├── decomposition.md
│   │   │   ├── dependencies.md
│   │   │   ├── resources.md
│   │   │   └── validation.md
│   │   ├── task-preparation/
│   │   │   ├── index.md
│   │   │   ├── permissions.md
│   │   │   ├── preconditions.md
│   │   │   ├── readiness.md
│   │   │   └── resources.md
│   │   └── verification-evaluation/
│   │       ├── index.md
│   │       ├── checks.md
│   │       ├── criteria.md
│   │       ├── evidence.md
│   │       └── results.md
│   ├── shared-components/
│   │   ├── index.md
│   │   ├── ask-decide/
│   │   │   ├── index.md
│   │   │   ├── approval.md
│   │   │   ├── clarify.md
│   │   │   └── decision.md
│   │   └── policy-knowledge-memory/
│   │       ├── index.md
│   │       ├── knowledge.md
│   │       ├── memory.md
│   │       ├── policy.md
│   │       └── retrieval.md
│   └── system-workflow.md
├── 03-research-decisions/
│   ├── index.md
│   ├── decision-log.md
│   ├── decision-records/
│   │   └── DEC-EXAMPLE.md
│   ├── open-questions.md
│   ├── research-library.md
│   └── research-notes/
│       └── RQ-EXEC-001.md
├── 04-development/
│   ├── index.md
│   ├── development-roadmap.md
│   ├── repository-engineering-guide.md
│   ├── technical-architecture.md
│   ├── technology-stack.md
│   └── work-breakdown-jira.md
├── 05-testing-evaluation/
│   ├── index.md
│   ├── research-evaluation.md
│   ├── results-evidence.md
│   └── testing-strategy.md
├── 06-team-records/
│   ├── index.md
│   ├── academic-deliverables.md
│   ├── meeting-notes.md
│   ├── supervisor-feedback.md
│   └── team-ownership/
│       ├── index.md
│       ├── ownership-matrix.md
│       ├── roles-responsibilities.md
│       ├── team-members.md
│       ├── team-structure.md
│       └── ways-of-working.md
└── _templates/
    ├── index.md
    ├── component.md
    ├── decision-record.md
    ├── element.md
    ├── meeting-note.md
    ├── research-note.md
    └── work-package.md
```

See [Ownership Matrix](wiki/06-team-records/team-ownership/ownership-matrix.md) for role assignments.
