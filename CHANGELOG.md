# Changelog

All notable changes to the `dotagents-standard` skill are documented here. The format is
based on [Keep a Changelog](https://keepachangelog.com/), and this project aims to follow
[Semantic Versioning](https://semver.org/).

## [0.2.0] - 2026-07-31

Guard the router against context leaking back into it.

### Added

- `SKILL.md`: a "Writing context back (the append trap)" section — the classify → write to
  `.agents/` → only-then-touch-the-router order, a self-check before any `AGENTS.md` write,
  and a worked trap-vs-correct example. Names both competing sinks: `AGENTS.md` itself and
  host-local agent memory (`~/.claude/` and similar tool-local memory features), which is
  machine-local, uncommitted, and invisible to other tools.
- A `## Maintenance` block in `assets/templates/AGENTS.md` and in the router example under
  the "AGENTS.md router pattern" section, stating that durable knowledge goes in `.agents/`
  and that only routing lines are ever added to the router.
- The same `## Maintenance` block in the worked example, `examples/sample-project/AGENTS.md`.

### Changed

- Implementing step 4 now includes the maintenance rule in the description of a tight router.
- Dropped the permissive `You may append durable decisions to .agents/memory/decisions.md`
  capability line from both routers — it read as an allowance rather than a constraint, and
  the `## Maintenance` block supersedes it.

## [0.1.0] - 2026-07-07

Initial release.

### Added

- `dotagents-standard` skill: mental model, the context decision-taxonomy, the utilize
  and implement workflows, and the `AGENTS.md` router pattern (`SKILL.md`).
- Reference docs: `references/directory-reference.md` (every `.agents/` subdirectory in
  depth) and `references/protocol-extensions.md` (the dotagentsprotocol.com superset).
- Copy-paste starter templates under `assets/templates/`.
- A worked example under `examples/sample-project/` — a filled-in `.agents/` layout for a
  hypothetical billing API.
- MIT license, README, and a CI workflow that validates skill frontmatter and Markdown links.

[0.2.0]: https://github.com/zaventh/dotagents-standard-skill/releases/tag/v0.2.0
[0.1.0]: https://github.com/zaventh/dotagents-standard-skill/releases/tag/v0.1.0
