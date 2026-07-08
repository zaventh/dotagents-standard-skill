# dotagents-standard — an agent skill

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Format: Agent Skill](https://img.shields.io/badge/format-agentskills.io-blue.svg)](https://agentskills.io)

An [agent skill](https://agentskills.io) that teaches an AI coding agent how to **implement and utilize the [dotagents](https://github.com/bgreenwell/dotagents) standard** — a slim `AGENTS.md` "router" at the repository root plus a `.agents/` directory that organizes agent context for *progressive disclosure*.

> Install this skill and your agent knows how to set up, migrate to, and work inside a `.agents/` layout — instead of stuffing everything into one monolithic `AGENTS.md` / `CLAUDE.md`.

## What is the dotagents standard?

As agents take on more work, a single context file (`AGENTS.md`, `CLAUDE.md`, `.cursorrules`) tends to bloat: the agent reads a database schema while editing CSS, behavioral rules blur into static facts, and vendor folders (`.claude/`, `.cursor/`, `.gemini/`) litter the repository root.

**dotagents** solves this by splitting context into a *router* and a *library*:

- **`AGENTS.md`** — a slim router at the repo root, always read. It states the agent's identity and points to deeper context *conditionally*.
- **`.agents/`** — the library of "heavy" context, split by kind: `rules/`, `context/`, `memory/`, `personas/`, `skills/`, `specs/`, `logs/`.

The agent loads only what the current task matches. This skill packages the know-how to do that well — the decision taxonomy, the router pattern, and ready-to-use templates — and also covers the broader [.agents Protocol](https://dotagentsprotocol.com/) superset.

## What this skill does

Once installed, it triggers whenever you:

- ask to **set up** dotagents / an `.agents/` layout in a repository,
- want to **split or migrate** a monolithic `AGENTS.md` / `CLAUDE.md` / `.cursorrules`,
- need to **work inside** a repository that already has an `AGENTS.md` router or a `.agents/` directory,
- or want the broader **.agents Protocol** (global `~/.agents/` layer, `mcp.json`, sub-agents, tasks, memories, shareable bundles).

It then walks the agent through classifying each piece of context, writing a tight router, and authoring each `.agents/` subdirectory — with copy-paste templates.

## Install

### With the Skills CLI (recommended)

```bash
npx skills add zaventh/dotagents-standard-skill
```

This installs the `dotagents-standard` skill for any [agentskills.io](https://agentskills.io)-compatible agent and keeps it current via `npx skills check` / `npx skills update`.

### Manual (symlink)

```bash
git clone https://github.com/zaventh/dotagents-standard-skill.git
cd dotagents-standard-skill
ln -s "$(pwd)/skills/dotagents-standard" ~/.claude/skills/dotagents-standard
```

Claude Code discovers skills under `~/.claude/skills/` (symlinks included), so it is picked up automatically. If you keep a canonical skills store at `~/.agents/skills/`, symlink it there too. For other agents, copy or symlink `skills/dotagents-standard/` into wherever your tool loads skills.

## Repository layout

```text
.
├── skills/
│   └── dotagents-standard/           # the skill (installed via `npx skills add`)
│       ├── SKILL.md                  # mental model, decision taxonomy, workflows, router pattern
│       ├── references/
│       │   ├── directory-reference.md    # every .agents/ subdirectory in depth
│       │   └── protocol-extensions.md    # the dotagentsprotocol.com superset
│       ├── assets/
│       │   └── templates/            # copy-paste starters: AGENTS.md, rules, memory, persona, skill
│       └── LICENSE
├── README.md
└── LICENSE
```

## How it works

Skills use **progressive disclosure**: the agent always sees the skill's name and description, reads `SKILL.md` when a task matches, and only opens `references/` or `assets/` when it needs the depth. That mirrors the dotagents philosophy itself — load the router first, the library on demand.

## Relationship to the standards

This skill is an independent **guide**, not the standard itself. It builds on:

| Standard | What it defines |
| :--- | :--- |
| [dotagents](https://github.com/bgreenwell/dotagents) (Brandon Greenwell) | The core directory-as-context architecture: `AGENTS.md` router + `.agents/`. |
| [.agents Protocol](https://dotagentsprotocol.com/) | A superset — global layer, machine config, structured sub-agents / tasks / memories, a sharing Hub. |
| [Agent Skills](https://agentskills.io) | The `SKILL.md` format this skill (and `.agents/skills/`) follow. |
| [AGENTS.md](https://agents.md) | The cross-vendor entry-point file the router rides on. |

## Acknowledgements

Thanks to **Brandon Greenwell** for the [dotagents](https://github.com/bgreenwell/dotagents) proposal, and to the authors of the [.agents Protocol](https://dotagentsprotocol.com/) for extending it. This skill exists to make those ideas easy for any agent to apply.

## License

[MIT](LICENSE) &copy; 2026 Jeffrey Walter Mixon
