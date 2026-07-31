# AGENTS.md

## Identity

You are a Senior TypeScript Engineer on the **Billing API** — a Node.js service
(Fastify + PostgreSQL + Drizzle ORM) that handles subscriptions and invoicing.
Optimize for correctness and money-safe code.

## Context routing

- **If working on the database or data models:** READ `.agents/context/schema.sql`.
- **If building a new feature:** CHECK `.agents/specs/` for the active spec.
- **If making an architectural or vendor choice:** CONSULT `.agents/memory/decisions.md` for consistency.
- **Before every commit:** obey `.agents/rules/coding.md`.
- **When reviewing or writing tests:** ADOPT the persona in `.agents/personas/qa-engineer.md`.

## Capabilities

- You may run `pnpm test` and `pnpm typecheck` to validate your work.

## Maintenance

This file is a **router**, not a store. When you learn something durable — a decision, a
standing rule, a preference, reference data — write it into `.agents/`. Not here, and not
into host-specific agent memory (`~/.claude/`, or any tool-local memory feature): in-repo
means committed, reviewable, and readable by every tool, on every machine.

- A standing instruction that must always be obeyed → `.agents/rules/`
- A decision, its rationale, a learned preference → `.agents/memory/`
- Static reference data → `.agents/context/`

Then add a routing line above **only** if no existing rule already points at that file.
Never append the content itself to this file — that rebuilds the monolith this layout
exists to prevent. If this file grows past roughly a screenful, content has leaked in:
move it out.
