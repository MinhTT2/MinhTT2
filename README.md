<p align="center">
  <picture><source media="(prefers-reduced-motion: reduce)" srcset="./assets/profile-banner.png" /><img src="./assets/profile-banner.gif" alt="Minh Tien Tran — full-stack developer. From a user flow to a working product. WorkLink, Pageforce, Sân Ngon." width="100%" /></picture>
</p>
<p align="center">
  <a href="https://worklink.id.vn"><img src="./assets/link-worklink.svg" alt="Visit WorkLink" width="165" /></a>
  <a href="https://github.com/MinhTT2?tab=repositories"><img src="./assets/link-code.svg" alt="Explore my code" width="183" /></a>
  <a href="https://github.com/minhtt22-26"><img src="./assets/link-history.svg" alt="Earlier GitHub account" width="178" /></a>
</p>

<p>I’m Minh, a <strong>full-stack developer</strong> building practical products with React, TypeScript, NestJS, and PostgreSQL. I like the details that make a product work: a clear interface, explicit business rules, and a backend that backs them up.</p>

<p><strong>A quick look at my work:</strong> <a href="https://worklink.id.vn">Try WorkLink ↗</a> · <a href="./docs/worklink-scheduling-story.md">Read an authored engineering story ↗</a> · <a href="https://github.com/MinhTT2?tab=repositories">Explore the code ↗</a></p>

<h2>01 / WorkLink — flagship team project</h2>
<p><strong>AI-powered job matching for the Vietnamese labor market.</strong><br /><sub>Software Engineering Project · Group 31 · React + NestJS</sub></p>
<p>Job discovery, applications, interview scheduling, chat, and payment workflows in one platform. Semantic embeddings and vector search connect candidates with relevant opportunities.</p>

<p>
  <a href="https://github.com/minhtt22-26/sepbe_G31/actions/workflows/ci.yml">Backend <img src="https://github.com/minhtt22-26/sepbe_G31/actions/workflows/ci.yml/badge.svg?branch=main" alt="WorkLink backend CI status" /></a> ·
  <a href="https://github.com/he170794kieudinhdoan-lang/sepfe_G31/actions/workflows/ci.yml">Frontend <img src="https://github.com/he170794kieudinhdoan-lang/sepfe_G31/actions/workflows/ci.yml/badge.svg?branch=main" alt="WorkLink frontend CI status" /></a>
</p>
<h3>One detail I cared about</h3>
<p>A candidate opens an interview invitation after a slot has already started. The UI should explain why it is unavailable, and the API should enforce the same rule.</p>
<p><picture><source media="(prefers-reduced-motion: reduce)" srcset="./assets/worklink-scheduling.png" /><img src="./assets/worklink-scheduling.gif" alt="Conceptual scheduling illustration: past slot unavailable, upcoming slot selectable, server rejects past starts" width="100%" /></picture></p>
<p><strong>My change:</strong> visible past-slot states, disabled selection, and a backend check on slot changes. I also refined invitation queries to consider upcoming slots and active deadlines.</p>
<p><a href="./docs/worklink-scheduling-story.md"><strong>Read the engineering story →</strong></a> <sub>Problem · decision · code evidence · tradeoffs</sub></p>

<h3>What I contributed</h3>
<ul>
  <li><strong>Scheduling reliability:</strong> disabled past interview slots in the UI, rejected past-slot changes in the API, and refined pending invitation counts. <a href="https://github.com/minhtt22-26/sepbe_G31/commit/6633809ebe5b796e57cad1176b079bf7099449dc">API change ↗</a> · <a href="https://github.com/he170794kieudinhdoan-lang/sepfe_G31/commit/ef767e28c864400e0bc177c9fcb636f97ee78a24">UI change ↗</a></li>
  <li><strong>Responsive conversations:</strong> added a Socket.io hook and typing indicator. <a href="https://github.com/he170794kieudinhdoan-lang/sepfe_G31/commit/118863374b62e5c59fa3ef9f0a3bfebafac790a8">Chat change ↗</a></li>
  <li><strong>Quality and delivery:</strong> expanded backend tests, added frontend CI/CD, and handled render failures with an error boundary. Evidence below.</li>
</ul>
<p><a href="https://worklink.id.vn">Live website ↗</a> · <a href="https://github.com/minhtt22-26/sepbe_G31">Backend ↗</a> · <a href="https://github.com/he170794kieudinhdoan-lang/sepfe_G31">Frontend ↗</a></p>
<p><sub>Built with the G31 team. My contributions span <a href="https://github.com/MinhTT2">MinhTT2</a> and my earlier account <a href="https://github.com/minhtt22-26">minhtt22-26</a>.</sub></p>
<details>
  <summary><strong>Engineering details &amp; verified contribution links</strong></summary>
<p><picture><source media="(prefers-reduced-motion: reduce)" srcset="./assets/worklink-flow.png" /><img src="./assets/worklink-flow.gif" alt="Conceptual WorkLink flow: profile, Gemini embeddings, pgvector and scoring, ranked suggestions" width="100%" /></picture></p>
<table>
  <tr><th align="left">Product capability</th><th align="left">Engineering behind it</th></tr>
  <tr><td>Semantic recommendations</td><td>Gemini embeddings, PostgreSQL/pgvector, and configurable scoring</td></tr>
  <tr><td>Application &amp; interview flows</td><td>React, TanStack Query, validated forms, and calendar interfaces</td></tr>
  <tr><td>Background processing</td><td>NestJS, Bull/Redis queues, retry handling, and scheduled tasks</td></tr>
  <tr><td>Chat &amp; payment workflows</td><td>Socket.io messaging, SePay checkout, and asynchronous webhook processing</td></tr>
</table>
<h3>My WorkLink contribution highlights</h3>
<p>Selected changes I authored across my two accounts:</p>
<table>
  <tr><th align="left">Area</th><th align="left">My contribution</th><th align="left">See the change</th></tr>
  <tr><td>Interview scheduling</td><td>Aligned past-slot handling across the UI and API; refined upcoming-slot and pending-invitation rules.</td><td><a href="https://github.com/minhtt22-26/sepbe_G31/commit/6633809ebe5b796e57cad1176b079bf7099449dc">API</a> · <a href="https://github.com/he170794kieudinhdoan-lang/sepfe_G31/commit/ef767e28c864400e0bc177c9fcb636f97ee78a24">UI</a></td></tr>
  <tr><td>Real-time chat</td><td>Added a Socket.io hook and typing indicator to make conversations feel responsive.</td><td><a href="https://github.com/he170794kieudinhdoan-lang/sepfe_G31/commit/118863374b62e5c59fa3ef9f0a3bfebafac790a8">Commit</a></td></tr>
  <tr><td>Backend quality</td><td>Expanded tests for services, DTOs, and infrastructure, including the Redis provider.</td><td><a href="https://github.com/minhtt22-26/sepbe_G31/commit/5f4b7b33d56f4e2c6830734c4ecf4a7945632802">Tests</a></td></tr>
  <tr><td>Delivery &amp; resilience</td><td>Added frontend CI/CD workflows and a top-level error boundary for render failures.</td><td><a href="https://github.com/he170794kieudinhdoan-lang/sepfe_G31/commit/37c7d5d557651701d0e884b47cc31362bfb7d6ae">CI/CD</a> · <a href="https://github.com/he170794kieudinhdoan-lang/sepfe_G31/commit/df882f9dac90df6eff1952b388bac86cf7af59c0">Error boundary</a></td></tr>
</table>
</details>
<details>
  <summary><strong>View my WorkLink contribution history</strong></summary>
  <ul>
    <li>Backend: <a href="https://github.com/minhtt22-26/sepbe_G31/commits/main/?author=minhtt22-26">earlier account</a> · <a href="https://github.com/minhtt22-26/sepbe_G31/commits/main/?author=MinhTT2">current account</a></li>
    <li>Frontend: <a href="https://github.com/he170794kieudinhdoan-lang/sepfe_G31/commits/main/?author=minhtt22-26">earlier account</a> · <a href="https://github.com/he170794kieudinhdoan-lang/sepfe_G31/commits/main/?author=MinhTT2">current account</a></li>
  </ul>
</details>

<h2>02 / More products I’m building</h2>
<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/MinhTT2/pageforce"><img src="./assets/pageforce-card.svg" alt="Pageforce — visual website builder; conceptual editor illustration" width="100%" /></a>
      <p>Drag-and-drop editing with typed JSON blocks and a renderer shared by previews and public pages.</p>
      <p><sub>Ownership checks · Lead capture · Migrations · Tests</sub></p>
      <p><a href="https://pageforce.vercel.app">Demo ↗</a> · <a href="https://github.com/MinhTT2/pageforce">Code ↗</a> · <a href="https://github.com/MinhTT2/pageforce/blob/main/docs/showcase.md">Tour ↗</a></p>
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/MinhTT2/san-ngon"><img src="./assets/san-ngon-card.svg" alt="Sân Ngon — sports venue booking; conceptual reservation calendar" width="100%" /></a>
      <p>Court discovery and booking with database-backed reservation rules and payment status updates.</p>
      <p><sub>Overlap protection · Expiring holds · Payment webhooks</sub></p>
      <p><a href="https://san-ngon.vercel.app">Demo ↗</a> · <a href="https://github.com/MinhTT2/san-ngon">Code ↗</a> · <a href="https://github.com/MinhTT2/san-ngon#những-quyết-định-kỹ-thuật-chính">Decisions ↗</a></p>
    </td>
  </tr>
</table>
<details>
  <summary><strong>Inside Pageforce — the builder workflow</strong></summary>
  <br />
  <a href="https://github.com/MinhTT2/pageforce/blob/main/docs/showcase.md">
    <img src="https://raw.githubusercontent.com/MinhTT2/pageforce/main/docs/assets/screenshots/builder-overview.png" alt="Pageforce visual builder with block palette, editing canvas, and inspector" width="100%" />
  </a>
  <p>The editor and public pages share a renderer, keeping what you edit aligned with what visitors see.</p>
</details>
<details>
  <summary><strong>Five-minute technical tour — where to start in the code</strong></summary>
  <ul>
    <li><strong>WorkLink:</strong> inspect <a href="https://github.com/minhtt22-26/sepbe_G31/blob/main/src/modules/ai-matching/service/ai-matching.service.ts">matching orchestration</a>, <a href="https://github.com/minhtt22-26/sepbe_G31/blob/main/src/modules/ai-matching/repositories/ai-matching.repository.ts">vector queries</a>, and the <a href="https://github.com/minhtt22-26/sepbe_G31/commit/6633809ebe5b796e57cad1176b079bf7099449dc">interview scheduling fix</a>.</li>
    <li><strong>Pageforce:</strong> inspect the <a href="https://github.com/MinhTT2/pageforce/blob/main/src/components/blocks/BlockRenderer.tsx">shared block renderer</a> used by editing previews and public pages, then follow the <a href="https://github.com/MinhTT2/pageforce/blob/main/docs/showcase.md">product walkthrough</a>.</li>
    <li><strong>Sân Ngon:</strong> inspect <a href="https://github.com/MinhTT2/san-ngon/blob/main/supabase/migrations/20260925000000_booking_holds.sql">booking hold logic</a>, then read the <a href="https://github.com/MinhTT2/san-ngon#những-quyết-định-kỹ-thuật-chính">engineering decisions</a> behind reservations and payments.</li>
  </ul>
</details>

<h2>03 / How I build</h2>
<p><img src="./assets/engineering-focus.svg" alt="Build interfaces and APIs; model data and rules; verify with tests and CI; ship and iterate" width="100%" /></p>
<p><strong>Start with the user flow.</strong> Model the data and edge cases, validate changes at the right boundary, and make decisions easy to review.</p>
<details>
  <summary><strong>Technology toolbox</strong></summary>
<table>
  <tr><th align="left">Area</th><th align="left">Tools</th></tr>
  <tr><td>Frontend</td><td>React, Next.js, TypeScript, Vite, Tailwind CSS, TanStack Query</td></tr>
  <tr><td>Backend &amp; async work</td><td>NestJS, REST APIs, Redis, Bull, Socket.io</td></tr>
  <tr><td>Data &amp; AI integration</td><td>PostgreSQL, pgvector, Prisma, Supabase, Gemini embeddings</td></tr>
  <tr><td>Quality &amp; delivery</td><td>Jest, Vitest, Playwright, ESLint, GitHub Actions, Docker, Vercel</td></tr>
  <tr><td>Also exploring</td><td><a href="https://github.com/MinhTT2/learning-vuejs">Vue 3, Vue Router, and Vite</a></td></tr>
</table>
</details>
<p><sub>Some professional contributions live in private repositories. My public work shows the product flows and engineering decisions I can share.</sub></p>

