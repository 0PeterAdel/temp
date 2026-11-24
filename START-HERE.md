# Shift Core — Master Project Wiki v1.0

**A ready-to-edit, role-based Markdown knowledge workspace for a seven-person graduation project team.**

## Open the Wiki

Start with [wiki/Home.md](wiki/Home.md) and [the sidebar](wiki/_Sidebar.md). The complete nested hierarchy is in [STRUCTURE.md](STRUCTURE.md). Use any Markdown editor with local-link support (e.g., VS Code preview or Obsidian). No extra dependencies are needed to edit the Markdown.

| Directory / file | Purpose |
|---|---|
| `wiki/` | **Canonical editable source.** Six project sections, component workspaces, element workspaces, role pages, research starters and reusable templates. |
| `github-wiki-ready/` | Generated flat GitHub Wiki import snapshot. Stable IDs are page slugs. Do not edit both copies. |
| `tools/wiki_tools.py` | Standard-library Python helper to validate links and regenerate a flat export from `wiki/`. |
| `tools/page-map.json` | Initial role and page-path snapshot for reference; it is not a second editable source of truth. |

## Use with the team

1. Read [Team & Ownership](wiki/06-team-records/team-ownership/index.md). Confirm actual seat mapping and whether the proposed Scrum Master overlay is appropriate; roles are **not** appointments.
2. Open [Architecture Overview](wiki/02-system-design/architecture-overview.md). Treat the nine-layer list as the current candidate map, not as approved architecture.
3. Pilot one component: [Task Execution](wiki/02-system-design/runtime-layers/task-execution/index.md). Assign an owner, contributors and a different-person reviewer for only the elements you can realistically explore. The page breakdown can be revised.
4. Use each element's **Required work**, **Expected deliverables**, output table and **Review criteria** as instructions. Replace prompts with actual understanding; leave unresolved questions visible.
5. Use the question index, research library and decision log to connect research to design. The provided agent/runtime research and decision records are **examples**, not completed work or approved decisions.
6. Complete Development and Jira sections progressively when design slices become clear. Jira owns actual work status; the real repository owns approved engineering specifications, ADRs, code and reproducible evidence.

**Do not activate all pages at once.** This package includes tailored scaffolds so you can select the next component and begin work immediately. It is not a claim that every element requires its own workstream or that all listed pages must be completed before implementation.

## GitHub Wiki import (optional)

The `github-wiki-ready/` folder contains a flat import snapshot, including `Home.md`, `_Sidebar.md` and `_Footer.md`. If you choose GitHub Wiki, enable it on the selected project repository and create its first page if necessary. Clone that repository's **wiki** Git repository (the URL ends in `.wiki.git`), review existing content, and copy the exported Markdown into the cloned Wiki checkout. Commit and push only after team review. Back up existing pages first; do not overwrite an existing Wiki without checking for filename conflicts. No remote repository or Wiki has been changed by this package.

To rebuild an export after editing the canonical source:

```bash
python3 tools/wiki_tools.py validate
python3 tools/wiki_tools.py export ./github-wiki-export-new
```

The export directory must be new or empty. The exporter converts relative local Markdown links into stable Wiki page slugs. It validates page IDs and local Markdown links; no live GitHub Wiki publishing or renderer test has been performed. In a plain local editor, use the nested `wiki/` source rather than the flat import's Wiki-style links.

## Changes and maintenance

- Keep stable page IDs. Numbering is only navigation; changing layer order does not change identities.
- When moving a page, update parent links and the architecture map. Keep an explanation or redirect when superseding a component. Validate links after moving.
- Update ownership and question indexes when introducing or moving pages. They are initial index snapshots, not a live status dashboard. Keep question classification at its originating element and ticket status in Jira.
- Maintain official content in English. Reviewers must be different actual people even if two roles are held by one person.
- Use diagrams and examples to clarify the concept; do not create empty documentation for appearance.

## Source and scope

This package is grounded in the two supplied November 24 discussion exports: the six-section Master Project Wiki proposal and the seven-seat Scrum/engineering role proposal. The later role discussion replaces the generic Team Lead title. Page-level owners, element prompts, output formats, sample research and the additional execution monitoring element are **proposed elaborations for team review**, not established technical decisions. The real repository layout is a later engineering topic; no prototype repository is used as authority. Actual findings, code, Jira IDs, supervisor statements, dates, assignments and approvals have not been invented.
