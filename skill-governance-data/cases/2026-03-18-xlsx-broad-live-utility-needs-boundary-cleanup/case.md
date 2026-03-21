# Case

- Date: 2026-03-18
- Skill: xlsx
- Current version: unknown
- Request class: single-skill review
- Why this case exists: broad-live-utility-needs-boundary-cleanup

## Expected behavior

- `xlsx` should remain a live skill because spreadsheet tasks are real and frequent.
- The live skill should be narrow enough that the model knows when to route into it and when not to.
- Spreadsheet-specific rules should stay compact in the main skill body, with domain-heavy detail moved into references.

## Observed behavior

- [xlsx/SKILL.md](/home/cnfjlhj/.codex/skills/xlsx/SKILL.md) was the broadest live utility skill in the library and read like a spreadsheet handbook.
- The main body mixed core routing rules, financial modeling conventions, pandas/openpyxl usage, and long examples without a clear boundary.
- The skill had only one real asset, [recalc.py](/home/cnfjlhj/.codex/skills/xlsx/recalc.py), but no `references/` structure.
- Baseline static audit was **32/100**.

## Evidence

- Original user phrasing: the user asked for the skill library to be reviewed and then cleaned up one by one without repeated confirmation.
- Files / paths:
  - [xlsx/SKILL.md](/home/cnfjlhj/.codex/skills/xlsx/SKILL.md)
  - [recalc.py](/home/cnfjlhj/.codex/skills/xlsx/recalc.py)
  - [docx/SKILL.md](/home/cnfjlhj/.codex/skills/docx/SKILL.md)
  - [pptx/SKILL.md](/home/cnfjlhj/.codex/skills/pptx/SKILL.md)
  - [pdf/SKILL.md](/home/cnfjlhj/.codex/skills/pdf/SKILL.md)
- Triggered skill(s): `skill-governance-loop`, `skills-governance`
- Missing skill(s): none
- Output problem: the live skill was too broad and under-structured for reliable routing

## Failure mode

- should trigger but did not
- should not trigger but did
- triggered but low quality
- overlap / duplication
- belongs in AGENTS.md instead

## Working hypothesis

- `xlsx` should stay enabled, but its body should be rewritten around a small routing workflow.
- Finance-specific detail should move into a reference file instead of bloating the live body.

## Next check

- Rewrite the live skill, add a reference file, and verify that static quality rises while the skill remains enabled.
