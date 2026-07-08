# Worked example: a dotagents layout in practice

This is a **filled-in** example of the dotagents standard for a hypothetical **billing API**
(Node.js + PostgreSQL + Drizzle ORM). It shows what the `dotagents-standard` skill helps you
produce — not blank templates, but a coherent, real-world `.agents/` library with a slim
[`AGENTS.md`](sample-project/AGENTS.md) router pointing into it.

```text
sample-project/
├── AGENTS.md                       # the router — identity + conditional context routing
└── .agents/
    ├── rules/coding.md             # invariants (strict TS, money as integer cents)
    ├── context/schema.sql          # read-only DB schema
    ├── memory/decisions.md         # ADRs (Postgres + Drizzle, cents, Stripe)
    ├── personas/qa-engineer.md     # the QA "hat"
    └── specs/checkout-flow.md      # the active feature spec
```

Read [`sample-project/AGENTS.md`](sample-project/AGENTS.md) first, then follow its routing
rules into `.agents/` — exactly how an agent practicing progressive disclosure would.
