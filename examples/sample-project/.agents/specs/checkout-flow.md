# Spec: self-serve plan upgrade

**Status:** Active
**Owner:** Billing squad

## Goal

Let a customer upgrade from `free` to `pro` without contacting support.

## Requirements

1. Show a prorated price for the remainder of the current billing period.
2. On confirm, create a Stripe payment intent for the prorated amount (in cents).
3. On payment success (webhook), set `subscriptions.plan = 'pro'` and issue an invoice.
4. The upgrade must be idempotent — a retried webhook must not double-charge or double-issue.

## Out of scope

- Downgrades and cancellations (tracked in a separate spec).
