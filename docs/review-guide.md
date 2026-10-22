# A five-minute tour of my work

[Back to my profile](../README.md)

Start with the kind of work you want to inspect. Each route leads to a product, source code, and a concrete engineering decision.

| Time | Review path |
| --- | --- |
| 1 minute | Open the [WorkLink demo](https://worklink.id.vn) or the [Pageforce screenshot tour](https://github.com/MinhTT2/pageforce/blob/main/docs/showcase.md). |
| 2 minutes | Read the [WorkLink scheduling case study](./worklink-scheduling-story.md), including the distinction between start-based booking eligibility and end-based reference slots. |
| 2 minutes | Inspect a test or database rule below, then follow the corresponding commit history or CI run. |

## WorkLink — a team product, with attributable changes

**Problem:** candidates can open invitations after some interview slots have started. The UI needs a clear unavailable state, and the API needs to enforce the rule independently.

**My contribution:** past-slot UI and API validation, a Socket.io hook and typing indicator, backend test additions, and frontend CI/CD. The case study links exact authored changes rather than attributing the whole platform to me.

- [Backend repository and setup](https://github.com/minhtt22-26/sepbe_G31)
- [Frontend repository and setup](https://github.com/he170794kieudinhdoan-lang/sepfe_G31)
- [Backend test changes](https://github.com/minhtt22-26/sepbe_G31/commit/5f4b7b33d56f4e2c6830734c4ecf4a7945632802)
- Backend history: [earlier account](https://github.com/minhtt22-26/sepbe_G31/commits/main/?author=minhtt22-26) · [current account](https://github.com/minhtt22-26/sepbe_G31/commits/main/?author=MinhTT2)
- Frontend history: [earlier account](https://github.com/he170794kieudinhdoan-lang/sepfe_G31/commits/main/?author=minhtt22-26) · [current account](https://github.com/he170794kieudinhdoan-lang/sepfe_G31/commits/main/?author=MinhTT2)

**Discussion point:** the browser clock drives display, while server time drives acceptance. The [case study](./worklink-scheduling-story.md) describes review scenarios and further hardening; those scenarios are not reported as executed tests.

## Pageforce — one page schema across editing and publishing

**Problem:** a visual builder can drift from the page visitors actually see.

**Implementation to inspect:** typed JSON blocks, schema validation, and a shared renderer. Private APIs check ownership through the parent site; public pages render published content.

- [Live demo](https://pageforce.vercel.app) · [Product screenshots](https://github.com/MinhTT2/pageforce/blob/main/docs/showcase.md)
- [Shared renderer](https://github.com/MinhTT2/pageforce/blob/main/src/components/blocks/BlockRenderer.tsx) · [Renderer tests](https://github.com/MinhTT2/pageforce/blob/main/src/components/blocks/BlockRenderer.test.tsx)
- [Schema and lead validation tests](https://github.com/MinhTT2/pageforce/blob/main/src/lib/validators.test.ts)
- [API transaction tests](https://github.com/MinhTT2/pageforce/blob/main/src/app/api/pages/%5BpageId%5D/route.test.ts)
- [Unauthenticated browser smoke tests](https://github.com/MinhTT2/pageforce/blob/main/tests/e2e/smoke.spec.ts)
- [Commit history](https://github.com/MinhTT2/pageforce/commits/main/) · [CI runs](https://github.com/MinhTT2/pageforce/actions/workflows/ci.yml)

After following the repository's [local setup](https://github.com/MinhTT2/pageforce#local-setup) with a development Supabase project:

```bash
npm run test
npm run ci
npm run test:e2e
```

`test` runs Vitest. `ci` runs lint, type checking, unit tests, and a production build. Browser smoke tests run separately and are also configured in GitHub Actions. Consult the repository for current environment and browser prerequisites.

**Tradeoff:** saving a non-blank page updates its public content immediately. This keeps the MVP's publishing flow simple, with no separate review stage.

## Sân Ngon — reservation correctness at the database boundary

**Problem:** two requests can compete for the same court and time; a browser-provided price cannot be trusted.

**Implementation to inspect:** PostgreSQL overlap constraints and pricing functions, expiring holds, payment transaction checks, and access controls.

- [Live demo](https://san-ngon.vercel.app) · [Architecture and decisions](https://github.com/MinhTT2/san-ngon#những-quyết-định-kỹ-thuật-chính)
- [Versioned database migrations](https://github.com/MinhTT2/san-ngon/tree/main/supabase/migrations)
- [Hold, pricing, and expiry assertions](https://github.com/MinhTT2/san-ngon/blob/main/scripts/check-booking-holds.sql)
- [Concurrent booking check](https://github.com/MinhTT2/san-ngon/blob/main/scripts/check-booking-concurrency.mjs)
- [Isolated SQL runner](https://github.com/MinhTT2/san-ngon/blob/main/scripts/run-sql-ci.mjs) · [SQL workflow runs](https://github.com/MinhTT2/san-ngon/actions/workflows/sql-ci.yml)
- [Commit history](https://github.com/MinhTT2/san-ngon/commits/main/) · [App CI runs](https://github.com/MinhTT2/san-ngon/actions/workflows/ci.yml)

Follow the [development setup](https://github.com/MinhTT2/san-ngon/blob/main/docs/dev-setup.md), using Node.js 24 and a development Supabase project:

```bash
npm ci
npm run setup:check
npm run ci
```

App CI runs lint, type checking, and a production build. The separate SQL workflow builds a disposable database on Linux CI, applies tracked migrations, runs rollback checks, and exercises concurrent booking. It runs on relevant database/script changes or manual dispatch; it is not part of `npm run ci`.

**Product boundary:** live payments, email delivery, and manual refunds require environment-specific acceptance checks. See the [MVP acceptance checklist](https://github.com/MinhTT2/san-ngon/blob/main/docs/mvp-acceptance.md).

## Reading the evidence

The links and command descriptions above were reviewed against public source on **22 October 2026**. This portfolio edit does not claim a fresh application test run, a measured coverage percentage, or business impact. Workflow pages show the current run status.
