# Case

- Date: 2026-03-18
- Skill: pdf
- Current version: unknown
- Request class: inventory-wide skill governance, one-skill-at-a-time cleanup
- Why this case exists: broad-live-utility-needs-boundary-cleanup

## Expected behavior

- `pdf` should remain a live lane because PDF work is common and materially different from other document formats.
- The live body should classify the task, define boundaries, and route to bundled references and scripts instead of acting like a full tutorial.

## Observed behavior

- The prior body was a large inline cookbook with many examples but little routing guidance.
- It had no `version`, no explicit `When to Use` section, no skip guidance, and no output contract.
- The skill already had supporting files like `forms.md`, `reference.md`, and `chinese-pdf-guide.md`, but the live body did not use them as progressive-disclosure anchors.

## Evidence

- Original user phrasing:
  - “我需要对我的整个skill的库做一次彻彻底底的review”
  - “我很想知道我是否有一些skill是重复的，或者说职权不清的”
  - “继续吧。但是我希望你逐个继续，一个一个来，就是不要我确认了”
- Files / paths:
  - `/home/cnfjlhj/.codex/skills/pdf/SKILL.md`
  - `/home/cnfjlhj/.codex/skills/pdf/forms.md`
  - `/home/cnfjlhj/.codex/skills/pdf/chinese-pdf-guide.md`
  - `/home/cnfjlhj/.codex/skills/pdf/reference.md`
  - `/home/cnfjlhj/.codex/skills/docx/SKILL.md`
  - `/home/cnfjlhj/.codex/skills/pptx/SKILL.md`
- Triggered skill(s):
  - `skill-governance-loop`
  - `skills-governance`
- Missing skill(s):
  - none
- Output problem:
  - too broad for a live skill
  - overlap risk with adjacent document-format skills
  - progressive disclosure existed on disk but not in the main routing body

## Failure mode

- triggered but low quality
- overlap / duplication

## Working hypothesis

- Keep `pdf` enabled, but reduce the live body to a routing layer around `extract / edit / form / create`.
- Re-anchor advanced detail in existing references and bundled scripts.
- Add explicit skill boundaries against `docx`, `pptx`, and `xlsx`.

## Next check

- Re-run static audit after rewrite.
- Confirm the inventory scanner still reports `pdf` as enabled.
- Verify the rewritten body links to the existing references and form scripts.
