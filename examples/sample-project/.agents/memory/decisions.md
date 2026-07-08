# Architecture decision records

## 001. PostgreSQL + Drizzle ORM

Status: Accepted
Date: 2026-01-14

Chose PostgreSQL for transactional integrity and Drizzle for type-safe, migration-friendly
access. Rejected a NoSQL store — billing needs relational guarantees and joins across
customers, subscriptions, and invoices.

## 002. Store money as integer cents

Status: Accepted
Date: 2026-02-03

All monetary values are integers in the currency's minor unit. A prototype using floats
accumulated rounding drift on prorated charges; integers eliminate it.

## 003. Stripe as the payment processor

Status: Accepted
Date: 2026-02-20

Use Stripe for card processing and webhooks. We reconcile Stripe events against our own
`invoices` table rather than treating Stripe as the source of truth.
