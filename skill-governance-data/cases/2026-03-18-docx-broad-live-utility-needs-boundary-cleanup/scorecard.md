# Scorecard

- Skill: docx
- Version: 0.2.0
- Auditor: Codex
- Date: 2026-03-18

| Dimension | Score | Notes |
|---|---:|---|
| Trigger Fit | 17 | DOCX as a Word-fidelity lane is now clearly stated |
| Scope Discipline | 18 | Redline default and format boundaries sharply reduce scope bleed |
| Progressive Disclosure | 16 | Deep detail now routes to `docx-js.md`, `ooxml.md`, and `document.py` |
| Structural Integrity | 18 | Versioned, mode-based workflow, output contract, and acceptance criteria now present |
| Empirical Gain | 11 | No trigger eval yet, but broken path references were removed from the entry-point layer |
| Maintenance Cost | 9 | Smaller body with bundled references lowers drift risk |
| Total | 89 | Strong keep-enabled result after boundary cleanup |

## Strongest keep evidence

- Tracked changes, comments, and OOXML-aware edits are distinct enough to justify a dedicated live skill.
- The skill directory already contains the right deeper materials; the main problem was how they were surfaced.

## Strongest disable evidence

- The old body was too large for an entry-point skill and contained broken local path references.
- Without explicit routing, it risked becoming a generic document-editing sink.

## Nearest competing skill

- `pdf`
- `pptx`

## Routing / content / scope diagnosis

- This was a routing and integrity cleanup, not a lane-removal case.
- The fix was to compress the entry point, remove bad references, and make `redline` the safety default for higher-risk documents.
