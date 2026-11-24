# Shift Core — Master Project Wiki

**Cognitive AI Runtime Platform | Knowledge & Design Workspace | v1.0**

This private temporary repository is a browsable copy of the Master Project Wiki package for the seven-person Shift Core graduation project team. It is a design and research workspace, not the product implementation repository. All design prompts, element breakdowns and role assignments are proposed scaffolds, not approved architecture or completed research.

**[Open the Wiki →](wiki/Home.md)** · **[Start Here](START-HERE.md)** · **[Full Structure](STRUCTURE.md)** · **[Ownership Matrix](wiki/06-team-records/team-ownership/ownership-matrix.md)**

## Wiki navigation

| Section | What you will find | Primary role |
| --- | --- | --- |
| [Project](wiki/01-project/index.md) | Product vision, problem, scope and use cases | Product Owner |
| [System Design](wiki/02-system-design/index.md) | Architecture, workflow, component and element workspaces | Technical Lead / Software Architect |
| [Research & Decisions](wiki/03-research-decisions/index.md) | Open questions, investigations, design decisions | AI Engineer & Research Lead |
| [Development](wiki/04-development/index.md) | Technical design, engineering guide, roadmap and future Jira breakdown | Technical Lead / Software Architect |
| [Testing & Evaluation](wiki/05-testing-evaluation/index.md) | Testing, research evaluation, results and evidence | Backend Engineer (Data & Persistence Owner) |
| [Team & Project Records](wiki/06-team-records/index.md) | Roles, ownership, meetings, feedback and academic deliverables | Scrum Master |

## System design workspaces

Each workspace includes its conceptual purpose, role-based ownership, element pages, required work, expected deliverables, review criteria, open questions and future implementation links. The component order below is a candidate map; stable IDs do not depend on the order.

| Runtime layer | Component workspace |
| --- | --- |
| 01 | [Task Creation](wiki/02-system-design/runtime-layers/task-creation/index.md) |
| 02 | [Task Analysis](wiki/02-system-design/runtime-layers/task-analysis/index.md) |
| 03 | [Task Planning](wiki/02-system-design/runtime-layers/task-planning/index.md) |
| 04 | [Task Preparation](wiki/02-system-design/runtime-layers/task-preparation/index.md) |
| 05 | [Task Execution](wiki/02-system-design/runtime-layers/task-execution/index.md) |
| 06 | [Verification & Evaluation](wiki/02-system-design/runtime-layers/verification-evaluation/index.md) |
| 07 | [Repair & Recovery](wiki/02-system-design/runtime-layers/repair-recovery/index.md) |
| 08 | [Completion Gate](wiki/02-system-design/runtime-layers/completion-gate/index.md) |
| 09 | [Experience Management](wiki/02-system-design/runtime-layers/experience-management/index.md) |

**Shared components:** [Ask & Decide](wiki/02-system-design/shared-components/ask-decide/index.md) · [Policy, Knowledge & Memory](wiki/02-system-design/shared-components/policy-knowledge-memory/index.md)

**Cross-system design:** [Data & Storage](wiki/02-system-design/cross-system/data-storage/index.md) · [Security & Trust](wiki/02-system-design/cross-system/security-trust/index.md) · [User Experience](wiki/02-system-design/cross-system/user-experience/index.md) · [Infrastructure & Deployment](wiki/02-system-design/cross-system/infrastructure-deployment/index.md)

## Repository structure (this repository)

```text
temp/
├── README.md                       # This entry point
├── START-HERE.md                   # Editing and import guide
├── STRUCTURE.md                    # Complete nested Wiki page tree
├── wiki/                           # Canonical editable Markdown
│   ├── Home.md
│   ├── _Sidebar.md
│   ├── _Footer.md
│   ├── 01-project/
│   ├── 02-system-design/
│   │   ├── runtime-layers/          # Nine candidate layers
│   │   ├── shared-components/       # Two shared components
│   │   └── cross-system/           # Four cross-system components
│   ├── 03-research-decisions/
│   ├── 04-development/
│   ├── 05-testing-evaluation/
│   ├── 06-team-records/
│   └── _templates/
├── github-wiki-ready/               # Generated flat import snapshot
└── tools/
    ├── wiki_tools.py
    └── page-map.json
```

<details>
<summary>Expand the complete canonical Wiki file tree</summary>

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

</details>

## Planned real product repository (separate)

The following is the previously discussed high-level monorepo layout for `Shift-Core/cognitive-ai-runtime`. It is a planning reference, not directories created in this temporary repository and not a claim of approved implementation details.

```text
cognitive-ai-runtime/
├── apps/
│   ├── web/
│   └── api/
├── services/
│   └── runtime/
├── packages/
│   ├── contracts/
│   └── shared/
├── domain-packs/                   # Domain-specific extensions; finance optional
├── database/
├── infra/
├── tests/
├── docs/
│   ├── architecture/
│   ├── adr/
│   ├── api/
│   ├── research/
│   └── diagrams/
├── academic/
│   ├── proposal/
│   ├── thesis/
│   ├── reports/
│   ├── presentations/
│   └── submissions/
├── scripts/
├── .github/
│   ├── workflows/
│   ├── CODEOWNERS
│   └── PULL_REQUEST_TEMPLATE.md
├── README.md
├── CONTRIBUTING.md
├── SECURITY.md
├── GOVERNANCE.md
├── .gitignore
├── .gitattributes
├── .editorconfig
└── .env.example
```

See [Repository & Engineering Guide](wiki/04-development/repository-engineering-guide.md) for the work to refine this layout. Create implementation folders only when they become useful.

## How the team works

1. Explore a component or element and document the current understanding.
2. Record questions where they arise; open a [research note](wiki/_templates/research-note.md) for deeper investigation.
3. Review the evidence, agree the design slice and record relevant decisions in the [Decision Log](wiki/03-research-decisions/decision-log.md).
4. Transfer approved engineering specifications and significant ADRs to the real repository; track implementation tasks in Jira.

**[Team & Ownership](wiki/06-team-records/team-ownership/index.md)** · **[Roles & Responsibilities](wiki/06-team-records/team-ownership/roles-responsibilities.md)** · **[Open Questions](wiki/03-research-decisions/open-questions.md)** · **[Writing Templates](wiki/_templates/index.md)**

## Editing and export

Edit `wiki/` only. The `github-wiki-ready/` folder is an import snapshot, not a second source of truth and not a published GitHub Wiki. Its wiki-style links are meant for the separate GitHub Wiki renderer; browse `wiki/` for regular repository Markdown links.

```bash
python3 tools/wiki_tools.py validate
python3 tools/wiki_tools.py export ./github-wiki-export-new
```

The export folder must be new or empty. Confirm role assignments and active pages before assigning work. No Jira tickets or actual appointments have been created.

## Package status

The original 242 files of the v1.0 ZIP are preserved; this README is the additional repository navigation page. This is a private review workspace. Do not publish or copy confidential project information to a public repository without the team's approval.
