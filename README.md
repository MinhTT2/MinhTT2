<p align="center">
  <img src="./assets/profile-banner-vivid.svg?v=portfolio-4" alt="Minh Tien Tran — full-stack developer. Interfaces, APIs, and business rules. Basketball illustration." width="100%" />
</p>

I’m **Minh**, a full-stack developer working across **React, TypeScript, NestJS, and PostgreSQL**. I build web products where the interface, API, and data rules work together: interview scheduling, visual page editing, and sports venue reservations.

<p align="center">
  <a href="https://worklink.id.vn"><img src="./assets/link-worklink.svg" alt="Try WorkLink" width="183" /></a>
  <a href="./docs/review-guide.md"><img src="./assets/link-story.svg?v=review-2" alt="Review my work in five minutes" width="183" /></a>
  <a href="https://github.com/MinhTT2?tab=repositories"><img src="./assets/link-code.svg" alt="Explore my code" width="183" /></a>
</p>

## Selected projects

### WorkLink · Job matching & interview scheduling

**G31 team project** · React · NestJS · PostgreSQL / pgvector

A platform connecting job seekers and employers through applications, interviews, chat, and payments. **My contributions:** past-slot validation in the UI and API, a Socket.io hook and typing indicator, backend tests, and frontend CI/CD.

**A change to review:** a 09:00 interview slot should become unavailable after its start, even if the candidate left the page open. I disabled past choices in the UI and added a server-side check for slot changes.

[Live product ↗](https://worklink.id.vn) · [My case study](./docs/worklink-scheduling-story.md) · [API diff](https://github.com/minhtt22-26/sepbe_G31/commit/6633809ebe5b796e57cad1176b079bf7099449dc) · [UI diff](https://github.com/he170794kieudinhdoan-lang/sepfe_G31/commit/ef767e28c864400e0bc177c9fcb636f97ee78a24)

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Pageforce · Visual website builder</h3>
      <a href="https://github.com/MinhTT2/pageforce/blob/main/docs/showcase.md"><img src="https://raw.githubusercontent.com/MinhTT2/pageforce/main/docs/assets/screenshots/builder-overview.png" alt="Actual Pageforce builder: block palette, page canvas, and content inspector" width="100%" /></a>
      <p>Compose a multi-page website from typed JSON blocks, preview it, and publish the saved content.</p>
      <p><strong>Engineering focus:</strong> one renderer shared by the editor and public pages; schema validation; ownership checks on private APIs.</p>
      <p><sub>Next.js · TypeScript · Prisma · Supabase</sub></p>
      <p><a href="https://pageforce.vercel.app"><strong>Demo ↗</strong></a> · <a href="https://github.com/MinhTT2/pageforce">Code &amp; setup</a> · <a href="https://github.com/MinhTT2/pageforce/blob/main/docs/showcase.md">Screenshots</a></p>
    </td>
    <td width="50%" valign="top">
      <h3>Sân Ngon · Sports venue booking</h3>
      <a href="https://github.com/MinhTT2/san-ngon"><img src="./assets/san-ngon-card.svg?v=two-color-1" alt="Sân Ngon — conceptual reservation calendar illustration" width="100%" /></a>
      <p>Find an available court, hold a time slot, and follow payment confirmation.</p>
      <p><strong>Engineering focus:</strong> PostgreSQL overlap constraints, server-side pricing, expiring holds, and payment webhook checks.</p>
      <p><sub>Next.js · TypeScript · PostgreSQL · Supabase · SePay</sub></p>
      <p><a href="https://san-ngon.vercel.app"><strong>Demo ↗</strong></a> · <a href="https://github.com/MinhTT2/san-ngon">Code &amp; setup</a> · <a href="https://github.com/MinhTT2/san-ngon#những-quyết-định-kỹ-thuật-chính">Design decisions</a></p>
    </td>
  </tr>
</table>

## Code, tests & decisions

| Question | Start here |
| --- | --- |
| How do I explain a full-stack change? | [WorkLink: the problem, implementation, and tradeoffs](./docs/worklink-scheduling-story.md) |
| How are invalid page schemas rejected? | [Pageforce validator tests](https://github.com/MinhTT2/pageforce/blob/main/src/lib/validators.test.ts): missing props, invalid colors, and bounded lead submissions |
| How does a page update interact with the database? | [Pageforce API tests](https://github.com/MinhTT2/pageforce/blob/main/src/app/api/pages/%5BpageId%5D/route.test.ts): transactional update and homepage reassignment |
| Where are reservation rules exercised? | [Sân Ngon hold checks](https://github.com/MinhTT2/san-ngon/blob/main/scripts/check-booking-holds.sql), [concurrent booking checks](https://github.com/MinhTT2/san-ngon/blob/main/scripts/check-booking-concurrency.mjs), and the [isolated SQL workflow](https://github.com/MinhTT2/san-ngon/actions/workflows/sql-ci.yml) |

**Want to run the projects?** The [review guide](./docs/review-guide.md) links setup instructions, runnable quality checks, CI, and commit history for each project.

<details>
  <summary><strong>WorkLink — more of my authored changes</strong></summary>

| Area | Contribution | Evidence |
| --- | --- | --- |
| Real-time chat | Socket.io hook and typing indicator | [Commit](https://github.com/he170794kieudinhdoan-lang/sepfe_G31/commit/118863374b62e5c59fa3ef9f0a3bfebafac790a8) |
| Backend quality | Tests for services, DTOs, and infrastructure | [Test changes](https://github.com/minhtt22-26/sepbe_G31/commit/5f4b7b33d56f4e2c6830734c4ecf4a7945632802) |
| Delivery & resilience | Frontend CI/CD and a render error boundary | [Workflow](https://github.com/he170794kieudinhdoan-lang/sepfe_G31/commit/37c7d5d557651701d0e884b47cc31362bfb7d6ae) · [Error boundary](https://github.com/he170794kieudinhdoan-lang/sepfe_G31/commit/df882f9dac90df6eff1952b388bac86cf7af59c0) |

My WorkLink contributions span **[MinhTT2](https://github.com/MinhTT2)** and my earlier account **[minhtt22-26](https://github.com/minhtt22-26)**. The wider platform is team work.

</details>

## Tools I work with

| Frontend | Backend & data | Quality & delivery |
| --- | --- | --- |
| React · Next.js · TypeScript | NestJS · REST · Socket.io | Jest · Vitest · Playwright |
| Tailwind CSS · TanStack Query | PostgreSQL · Prisma · Supabase · Redis | GitHub Actions · Docker · Vercel |

Some professional work lives in private repositories. My profile includes anonymized private contributions; the public projects above provide code and decisions you can inspect.

<p align="center"><img src="./assets/basketball-avatar.png" alt="Basketball" width="180" /></p>
