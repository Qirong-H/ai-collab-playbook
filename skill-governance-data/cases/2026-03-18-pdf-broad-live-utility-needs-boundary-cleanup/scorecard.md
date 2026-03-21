# Scorecard

- Skill: pdf
- Version: 0.2.0
- Auditor: Codex
- Date: 2026-03-18

| Dimension | Score | Notes |
|---|---:|---|
| Trigger Fit | 17 | PDF as a file-format lane is clear and common |
| Scope Discipline | 17 | Boundaries against `docx`, `pptx`, and `xlsx` are now explicit |
| Progressive Disclosure | 16 | Advanced detail moved behind `forms.md`, `reference.md`, and the CJK guide |
| Structural Integrity | 18 | Versioned, stepwise workflow, output contract, and acceptance criteria now present |
| Empirical Gain | 12 | No trigger eval yet, but local directory structure now aligns with the live skill body |
| Maintenance Cost | 9 | Smaller main body and existing references reduce drift risk |
| Total | 89 | Strong keep-enabled candidate after boundary cleanup |

## Strongest keep evidence

- PDF extraction, page operations, and form workflows are distinct enough to justify a dedicated live lane.
- The skill directory already contains reusable references and scripts, so shrinking the live body improves reuse instead of deleting capability.

## Strongest disable evidence

- The old live body was too broad and overlapped with general document-processing instincts.
- Without explicit routing, the skill could encourage ad hoc PDF tool use instead of bounded execution.

## Nearest competing skill

- `docx`
- `pptx`

## Routing / content / scope diagnosis

- This was primarily a scope-discipline failure, not a false-positive lane.
- The fix was to keep the skill enabled while converting the main file into a compact router over the already-present deeper references.
