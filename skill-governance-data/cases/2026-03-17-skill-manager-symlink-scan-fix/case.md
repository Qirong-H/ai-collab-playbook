# Case

- Date: 2026-03-17
- Skill: skill-manager
- Current version: unversioned
- Request class: version update
- Why this case exists: `skill-manager` failed to discover a newly added symlinked Codex skill, which made the governance catalog incomplete right after a real skill installation.

## Expected behavior

Running `node ~/.codex/skills/skill-manager/scan.js` should discover both normal skill directories and symlinked skill directories under `~/.codex/skills/`, because symlink-based skill sharing is part of the actual workflow.

## Observed behavior

The scanner only accepted `entry.isDirectory()`. A symlinked skill folder existed and contained a valid `SKILL.md`, but it was omitted from scan output and therefore invisible to catalog-based governance.

## Evidence

- Original user phrasing: the new governance skill was linked into `~/.codex/skills`, but `skill-manager` refresh did not show it.
- Files / paths:
  - `/home/cnfjlhj/.codex/skills/skill-manager/scan.js`
  - `/home/cnfjlhj/.codex/skills/skill-governance-loop -> /home/cnfjlhj/projects/ai-collab-playbook/skills/full/skill-governance-loop`
- Triggered skill(s): `skill-manager`
- Missing skill(s): `skill-governance-loop`
- Output problem: scan output did not contain `skill-governance-loop` until the scanner was patched to follow symlinked directories.

## Failure mode

- should trigger but did not
- triggered but low quality

## Working hypothesis

`skill-manager` is useful, but it is under-specified and under-versioned. The immediate bug was scanner logic, but the broader problem is that the skill lacked explicit boundaries, versioning, and governance-oriented output expectations.

## Next check

1. Add versioning and tighter trigger/boundary language to `skill-manager`.
2. Re-run static audit and scan verification.
3. Use the next real skill-management request to verify that the updated workflow is easier to iterate.
