# Артур Онисько — AI systems & reliability builder

Я проєктую AI/agent workflows, які можна **прочитати, зламати тестом, відновити після збою і передати іншому власнику без магії**.

Мій фокус — не кількість промптів і не титул. Мій фокус — системна форма:

`ingress → provenance → state → decision boundary → effect → receipt → recovery`

Працюю з Python і TypeScript, API/webhook automation, agent/tool runtimes, RAG/evaluation, durable state, idempotency, hostile tests та operator handoff. AI coding agents використовую як керовану інженерну силу; остаточні твердження приймаю лише після відтворюваного proof.

## Що можна перевірити публічно

### [Evidence-gated Agent Workflows](https://github.com/DiadkoShmek/evidence-gated-agent-workflows/releases/tag/public-proof-v1.8.0)

Immutable release `public-proof-v1.8.0` містить сім локальних reference-контурів для систем, які не мають права перетворювати stale/missing/conflicting evidence, crash, unknown job id, неповний artifact handoff, неперевірений action commitment або непідтверджений local context на успіх.

- evidence admission, bounded polling і durable workflow state;
- receipt-last immutable artifact handoff із historical held-FD readback без current-path claim після повернення;
- typed action/pre-state commitment перед локальною симуляцією;
- dependency-free lexical retrieval із точним source digest і лише `local-context-review-ready` межею;
- replay/conflict refusal та review-required handoff;
- `network_access_performed=false`;
- `external_action_performed=false`.

Відтворення: `python3 run_proof.py`. Очікуваний terminal readback: `ALL PUBLIC PROOFS PASSED`.

[Переглянути AI Systems Proof Sprint](https://diadkoshmek.github.io/evidence-gated-agent-workflows/ai-systems-sprint.html) · [відкрити review-only inquiry](https://github.com/DiadkoShmek/evidence-gated-agent-workflows/issues/new?template=client-inquiry.yml)

Публічний issue не повинен містити credentials, customer/personal data, private code або production access details.

## Інженерні кейси під контрольованим показом

Це локальні private proof artifacts. Публікую лише redacted technical summaries, щоб не змішувати synthetic proof із deployment claim і не віддавати відтворювану внутрішню реалізацію. Для релевантної команди проведу scoped live walkthrough та покажу тестовий readback без передачі приватного репозиторію, промптів, повної архітектури чи reusable implementation assets.

| Кейс | Що доведено | Локальний proof | Що не заявляється |
|---|---|---:|---|
| Webhook reliability controller | HMAC-before-persist, pseudonymization, durable lease, idempotency, bounded retry/dead-letter, crash recovery | `24 passed` | production GHL/n8n, real customer data, universal exactly-once |
| Bounded RAG review flow | source re-attestation, deterministic retrieval, LangGraph state, Chroma wiring, `review_only` effect boundary | `6 passed` | LLM provider quality, production RAG, deployment |
| Typed agent workflow contract | canonical fingerprint, exact approval binding, bounded retries, malformed-outcome rejection, deterministic receipts | `10 passed` + TypeScript typecheck | real transport/auth, external mutation, multi-writer persistence |
| Agent/runtime continuity architecture | explicit ownership, receipts, recovery state, fail-closed promotion and hostile review discipline | scoped technical review only; not public evidence | client deployment, certification, autonomous business authority |

Детальні карти доказів і timestamped private readbacks залишаються локальними матеріалами для scoped walkthrough; вони не є частиною публічного proof.

### Межа розкриття

- **Публічно:** проблема, клас рішення, перевірені метрики, межі доказу та навмисно вузький reproducible reference.
- **Технічний відбір:** керована демонстрація і відповіді на питання без копії приватного коду або повної карти системи.
- **Оплачуваний контур / окрема письмова домовленість:** адаптація, інтеграція, передача узгоджених deliverables і прав використання.

Внутрішні алгоритми, оркестрація, prompts, datasets, threat models, операційні playbooks та reusable blueprints не є безкоштовним screening material.

## Де я даю найбільшу цінність

- агент або automation prototype працює лише «коли все добре»;
- дублікати, retries і partial failure створюють неконтрольовані effects;
- RAG/tool workflow не має вимірюваної межі якості;
- складний код неможливо чесно передати або відновити після crash;
- команді потрібен не ще один demo, а один reviewable vertical slice.

## Формат першої роботи

Один workflow, один named owner, один вимірюваний критерій, один bounded slice:

1. карта failure modes і authority;
2. typed input/output contract;
3. runnable implementation seam;
4. hostile acceptance tests;
5. proof receipt, known limits і handoff.

Найкращий старт — **AI Systems Proof Sprint: $1,500 fixed, 3–5 working days**, один sanitized source-to-target handoff, hostile tests, decision trace, known limits і engineering handoff. Production deployment, SLA, certification, client-system access та automatic activation не входять у перший Sprint. Remote, async-first; українська вільно, англійська — письмово з AI-assisted translation, spoken/listening обмежені.

## Контакт

[LinkedIn](https://www.linkedin.com/in/%D0%B0%D1%80%D1%82%D1%83%D1%80-%D0%BE%D0%BD%D0%B8%D1%81%D1%8C%D0%BA%D0%BE-842296411/) · [Public proof v1.8](https://github.com/DiadkoShmek/evidence-gated-agent-workflows/releases/tag/public-proof-v1.8.0) · [Sprint](https://diadkoshmek.github.io/evidence-gated-agent-workflows/ai-systems-sprint.html)

---

**English summary:** I build inspectable AI/agent workflows around provenance, explicit authority, durable state, bounded retries, hostile tests, and recovery. Written English is supported; async technical screening or a code task is preferred.
