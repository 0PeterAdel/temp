# Shift Core — Master Project Wiki

**Cognitive AI Runtime Platform | Knowledge & Design Workspace | v1.0**

This temporary repository is the entry point to the Shift Core design and research workspace. The full documentation lives in the independent GitHub Wiki. The architecture, role assignments, and research prompts are proposed scaffolds, not approved implementation claims.

**[Open the Project Wiki →](https://github.com/0PeterAdel/temp/wiki)**

## Wiki navigation

| Section | Purpose |
| --- | --- |
| [Project](https://github.com/0PeterAdel/temp/wiki/PROJECT) | Vision, problem, scope and use cases |
| [System Design](https://github.com/0PeterAdel/temp/wiki/DESIGN) | Architecture, layers and shared components |
| [Research & Decisions](https://github.com/0PeterAdel/temp/wiki/RESEARCH) | Questions, research and decisions |
| [Development](https://github.com/0PeterAdel/temp/wiki/DEVELOP) | Technical design and Jira work breakdown |
| [Testing & Evaluation](https://github.com/0PeterAdel/temp/wiki/TEST) | Testing, evaluation and evidence |
| [Team & Project Records](https://github.com/0PeterAdel/temp/wiki/TEAM) | Roles, ownership, feedback and records |

[Ownership Matrix](https://github.com/0PeterAdel/temp/wiki/OWNERSHIP) · [Writing Templates](https://github.com/0PeterAdel/temp/wiki/TEMPLATES) · [Open Questions](https://github.com/0PeterAdel/temp/wiki/QUESTIONS)

## This repository

```text
temp/
└── README.md
```

The Wiki has its own Git repository (`temp.wiki.git`). Edit pages there, not in duplicated folders in this repository. The pre-migration documentation package remains recoverable from the existing Git history.

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

See [Repository & Engineering Guide](https://github.com/0PeterAdel/temp/wiki/REPO) for the work to refine this layout. Create implementation folders only when they become useful.
