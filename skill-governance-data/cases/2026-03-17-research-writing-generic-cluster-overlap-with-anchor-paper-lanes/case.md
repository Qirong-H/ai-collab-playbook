# Case

- Date: 2026-03-17
- Skill: research-writing-generic-cluster
- Current version: unknown
- Request class: inventory cleanup
- Why this case exists: overlap-with-anchor-paper-lanes

## Expected behavior

- Generic paper-writing requests should route to one of a few specific live lanes.
- Broad legacy writers should not compete with anchor skills that already own the main paper workflows.
- Disabled legacy skills may remain as archival routing notes, but not as live fallbacks.

## Observed behavior

- [academic-paper-helper](/home/cnfjlhj/.codex/skills/academic-paper-helper/SKILL.md), [academic-research-writer](/home/cnfjlhj/.codex/skills/academic-research-writer/SKILL.md), and [research-paper-writer](/home/cnfjlhj/.codex/skills/research-paper-writer/SKILL.md) all present themselves as broad paper-writing helpers.
- The active anchors already exist:
  - [ml-paper-writing](/home/cnfjlhj/.codex/skills/ml-paper-writing/SKILL.md)
  - [arxiv-paper-writer](/home/cnfjlhj/.codex/skills/arxiv-paper-writer/SKILL.md)
  - [paper-review-pipeline](/home/cnfjlhj/.codex/skills/paper-review-pipeline/SKILL.md)
  - [citation-validator](/home/cnfjlhj/.codex/skills/citation-validator/SKILL.md)
- Baseline static audits for the generic trio were **42**, **63**, and **72**, substantially below the anchor lanes.
- Although the generic trio was already disabled, their content still described themselves as broad end-to-end entry points.

## Evidence

- Original user phrasing: the user asked for a thorough review of the skill library, especially duplicate skills and unclear ownership.
- Files / paths:
  - [academic-paper-helper](/home/cnfjlhj/.codex/skills/academic-paper-helper/SKILL.md)
  - [academic-research-writer](/home/cnfjlhj/.codex/skills/academic-research-writer/SKILL.md)
  - [research-paper-writer](/home/cnfjlhj/.codex/skills/research-paper-writer/SKILL.md)
  - [ml-paper-writing](/home/cnfjlhj/.codex/skills/ml-paper-writing/SKILL.md)
  - [arxiv-paper-writer](/home/cnfjlhj/.codex/skills/arxiv-paper-writer/SKILL.md)
  - [paper-review-pipeline](/home/cnfjlhj/.codex/skills/paper-review-pipeline/SKILL.md)
- Triggered skill(s): `skill-governance-loop`, `skills-governance`
- Missing skill(s): none
- Output problem: the generic trio still acts like overlapping front doors instead of clearly yielding to anchor lanes

## Failure mode

- should trigger but did not
- should not trigger but did
- triggered but low quality
- overlap / duplication
- belongs in AGENTS.md instead

## Working hypothesis

- The generic trio should remain disabled and be rewritten into compact archival routing notes.
- The live front door should be the anchor lanes, not the generic trio.

## Next check

- Rewrite the three generic writers as disabled routing notes, then re-audit and confirm their disabled status remains stable.
