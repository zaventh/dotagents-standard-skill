-- Billing API — core schema (PostgreSQL). Read-only reference for agents.

CREATE TABLE customers (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email       VARCHAR(255) UNIQUE NOT NULL,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE subscriptions (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id         UUID NOT NULL REFERENCES customers(id),
    plan                VARCHAR(50) NOT NULL,              -- 'free' | 'pro' | 'enterprise'
    status              VARCHAR(20) NOT NULL DEFAULT 'active',
    current_period_end  TIMESTAMPTZ NOT NULL,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE invoices (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    customer_id   UUID NOT NULL REFERENCES customers(id),
    amount_cents  INTEGER NOT NULL CHECK (amount_cents >= 0),  -- money is always integer cents
    currency      CHAR(3) NOT NULL DEFAULT 'USD',
    status        VARCHAR(20) NOT NULL DEFAULT 'open',         -- 'open' | 'paid' | 'void'
    issued_at     TIMESTAMPTZ NOT NULL DEFAULT now()
);
