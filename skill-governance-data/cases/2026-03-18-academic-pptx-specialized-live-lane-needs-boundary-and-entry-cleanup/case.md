# Case

- Date: 2026-03-18
- Skill: academic-pptx
- Current version: unknown
- Request class: inventory-wide skill governance, one-skill-at-a-time cleanup
- Why this case exists: specialized-live-lane-needs-boundary-and-entry-cleanup

## Expected behavior

- `academic-pptx` should remain a specialized live lane for academic slide creation, not be collapsed into a generic presentation skill.
- The entry point should clearly state when to use it, when not to use it, and what output and verification it requires.

## Observed behavior

- The skill already had a strong domain-specific body, but lacked `version`, an explicit `When to Use` section, and an output contract.
- After adjacent cleanup of generic `pptx`, this specialized lane needed a sharper entry boundary.
- User feedback on `pptx` indicated that live utility skills can be over-compressed; this skill should therefore be governance-framed without hollowing out its content.

## Evidence

- Original user phrasing:
  - “我需要对我的整个skill的库做一次彻彻底底的review”
  - “我很想知道我是否有一些skill是重复的，或者说职权不清的”
  - “是不是删太多了”
- Files / paths:
  - `/home/cnfjlhj/.codex/skills/academic-pptx/SKILL.md`
  - `/home/cnfjlhj/.codex/skills/pptx/SKILL.md`
  - `/home/cnfjlhj/.codex/skills/academic-pptx/formula-rendering.md`
  - `/home/cnfjlhj/.codex/skills/academic-pptx/diagram-rendering.md`
  - `/home/cnfjlhj/.codex/skills/academic-pptx/pptxgenjs-reference.md`
  - `/home/cnfjlhj/.codex/skills/academic-pptx/references/themes.md`
- Triggered skill(s):
  - `skill-governance-loop`
  - `skills-governance`
- Missing skill(s):
  - none
- Output problem:
  - entry boundary not explicit enough
  - governance metadata incomplete
  - risk of over-compression if treated like a generic live utility skill

## Failure mode

- triggered but low quality
- overlap / duplication

## Working hypothesis

- Keep `academic-pptx` enabled and preserve its detailed specialized body.
- Add governance framing at the top: version, use boundary, entry rule, and output contract.
- Avoid aggressive shrinkage; this is a heavy expert lane, not a thin router skill.

## Next check

- Re-run static audit after entry cleanup.
- Verify that the specialized body remains intact while the top-level boundary is clearer.
- Confirm `pptx` and `academic-pptx` now form a coherent generic-vs-academic pair.
