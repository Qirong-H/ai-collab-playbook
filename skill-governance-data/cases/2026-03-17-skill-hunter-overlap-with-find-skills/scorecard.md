# Scorecard

- Skill: skill-hunter
- Version: unknown
- Auditor: Codex
- Date: 2026-03-17

| Dimension | Score | Notes |
|---|---:|---|
| Trigger Fit | 6 | It names a real fallback use case, but that use case is already claimed by `find-skills` |
| Scope Discipline | 5 | Too much implementation detail for a secondary fallback skill |
| Progressive Disclosure | 1 | Giant body with no `references/` split |
| Structural Integrity | 10 | File exists and parses, but environment assumptions are brittle |
| Empirical Gain | 4 | Some ideas are useful, but they do not justify a separate active skill |
| Maintenance Cost | 2 | Large body plus GitHub CLI assumptions create high upkeep cost |
| Total | 28 | Strong merge-and-disable candidate |

## Strongest keep evidence

- GitHub mining is still a useful fallback once registry search fails.

## Strongest disable evidence

- The same fallback lane is already better owned by [find-skills/SKILL.md](/home/cnfjlhj/.codex/skills/find-skills/SKILL.md).

## Nearest competing skill

- [find-skills/SKILL.md](/home/cnfjlhj/.codex/skills/find-skills/SKILL.md)

## Routing / content / scope diagnosis

- Primary diagnosis: routing duplication
- Secondary diagnosis: content bloat
- Tertiary diagnosis: stale environment assumptions
