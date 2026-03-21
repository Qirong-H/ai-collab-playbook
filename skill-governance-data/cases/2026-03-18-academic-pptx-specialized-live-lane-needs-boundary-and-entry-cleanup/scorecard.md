# Scorecard

- Skill: academic-pptx
- Version: 0.2.0
- Auditor: Codex
- Date: 2026-03-18

| Dimension | Score | Notes |
|---|---:|---|
| Trigger Fit | 18 | Academic slide creation scope is highly specific and already well described |
| Scope Discipline | 18 | Boundary against generic `pptx` is now explicit |
| Progressive Disclosure | 14 | Heavy live body remains, but specialized references and scripts already exist |
| Structural Integrity | 16 | Version and top-level governance sections were added without flattening the main body |
| Empirical Gain | 12 | No trigger eval yet, but user feedback directly informed the “do not over-compress” decision |
| Maintenance Cost | 8 | Still a large live skill, which carries some upkeep cost |
| Total | 86 | Strong specialized keep-enabled case |

## Strongest keep evidence

- The skill contains genuinely specialized academic presentation logic that generic deck tooling does not cover well.
- It has real supporting assets for themes, formulas, diagrams, OMML injection, and verification.

## Strongest disable evidence

- The body is still very large for an always-loaded skill.
- Some future detail could likely move into references without harming the lane.

## Nearest competing skill

- `pptx`

## Routing / content / scope diagnosis

- This is not a “thin router” skill. It is a specialized heavy lane.
- The governance fix was to sharpen the entry boundary and metadata, not to remove the detailed academic workflow body.
