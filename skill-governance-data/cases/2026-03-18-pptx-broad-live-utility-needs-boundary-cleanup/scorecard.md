# Scorecard

- Skill: pptx
- Version: 0.2.1
- Auditor: Codex
- Date: 2026-03-18

| Dimension | Score | Notes |
|---|---:|---|
| Trigger Fit | 17 | Generic PPTX ownership is now clearly described |
| Scope Discipline | 18 | Academic deck creation is explicitly delegated to `academic-pptx` |
| Progressive Disclosure | 17 | Bundled scripts and references now own the deeper workflows |
| Structural Integrity | 18 | Versioned, mode-based workflow, output contract, and acceptance criteria now present |
| Empirical Gain | 11 | No live trigger eval yet, but dead helper references were removed and real assets are now foregrounded |
| Maintenance Cost | 9 | Much smaller entry point and better asset routing reduce drift |
| Total | 90 | Strong keep-enabled result after boundary cleanup |

## Strongest keep evidence

- Existing-deck PowerPoint operations are common and distinct enough to justify a generic lane.
- This skill directory already contains a credible tool bundle for inventory, replacement, reordering, and thumbnails.

## Strongest disable evidence

- The old file had become an oversized handbook and mixed in specialized creation guidance.
- Without an explicit boundary, users could easily route academic slide creation into the wrong lane.

## Nearest competing skill

- `academic-pptx`

## Routing / content / scope diagnosis

- This was a keep-and-narrow case with overlap control.
- The main repair was to convert the entry point into a generic router, make the academic lane boundary explicit, and then restore a medium-depth generic workflow reference after user feedback showed the first rewrite was too thin.
