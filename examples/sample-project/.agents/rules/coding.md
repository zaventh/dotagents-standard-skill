# Coding standards

- TypeScript strict mode. Never use `any` — model unknowns with generics or `unknown` + narrowing.
- All money is stored and computed in integer minor units (cents). Never use floats for currency.
- Every database write goes through a Drizzle transaction; no raw string-concatenated SQL.
- Public functions declare explicit return types.
- Run `pnpm test` and `pnpm typecheck` before committing.
