# External results

> **Current snapshot 05.11.2026, 19:07 UTC: 10 direct merges, 4 contributions incorporated into merged maintainer fixes; 134 PRs, 116 OPEN, 8 CLOSED without merge.** [Casebook and current ledger](https://github.com/DiadkoShmek/engineering-results) · [All PRs](https://github.com/DiadkoShmek/engineering-results/blob/main/PR_STATUS.en.md).
> **New:** [Instructor #2866 → merged #2899](https://github.com/DiadkoShmek/engineering-results/blob/main/reports/instructor-2026-11.md). The material below is the historical 2 November 2026 snapshot; its states are not current.

Open-source contributions, technical audits and competition results. Each entry names the date, contribution, external evidence and disposition. Engineering and investigation used AI tools.

[Українська](RESULTS.md) · [Case reports](reports/README.md) · [Machine-readable records](results.json)

## Contributions and audits

| Date | Project | Contribution | External outcome |
|---|---|---|---|
| 21 Oct 2026 | [FilesDrop](reports/filesdrop-2026-10.md#english-summary) | Two API reliability fixes and regression coverage | [PR #32 merged](https://github.com/AndreyBegma/FilesDrop/pull/32) |
| 24 Oct 2026 | [Prime Intellect · Verifiers / prime-rl](reports/prime-intellect-2026-10.md#english-summary) | Investigation, reproduction and a proposed patch | [Maintainer acknowledgement](https://github.com/PrimeIntellect-ai/verifiers/pull/2925#issuecomment-6385135636); maintainer implementation merged in both projects |
| 29 Oct 2026 | [M7 MCP](reports/m7-2026-10.md#english-summary) | Independent technical audit and focused follow-up | [Public review/triage credit in v3.18.1](https://github.com/DukeDeSouth/m7-mcp-oss/releases/tag/v3.18.1); fixes implemented by maintainers |
| 1 Nov 2026 | [TensorDict](reports/tensordict-2026-11.md#english-summary) | Reproduction, proposed fix and thorough tests | [Maintainer #3427 merged with credit](https://github.com/pytorch/tensordict/pull/3427); our #3426 superseded |
| 2 Nov 2026 | [Braintrust SDK JavaScript](reports/braintrust-2026-11.md#english-summary) | Streaming UTF-8 decoding and regressions | [Our PR #2701 merged](https://github.com/braintrustdata/braintrust-sdk-javascript/pull/2701) |
| 2 Nov 2026 | [Kraft](reports/kraft-2026-11.md#english-summary) | Skill refresh with an existing MCP registration | [Our PR #1227 merged](https://github.com/itsOmidKarami/kraft/pull/1227) |
| 2 Nov 2026 | [BlackJAX](reports/blackjax-2026-11.md#english-summary) | Stable Barker MCMC proposal probabilities and acceptance ratio | [Our PR #1068 merged](https://github.com/blackjax-devs/blackjax/pull/1068) |
| 2 Nov 2026 | [Apache TVM-FFI](reports/tvm-ffi-2026-11.md#english-summary) | Structural-hash finding, proposed fix and regressions | [Maintainer superseded #897 with #898](https://github.com/apache/tvm-ffi/pull/897#issuecomment-6588300834); successor still OPEN |

### Snapshot · 2 November 2026

**Four directly merged PRs:** FilesDrop #32, Braintrust #2701, Kraft #1227 and BlackJAX #1068. **Two separate credited contributions:** Prime Intellect and TensorDict — our proposals were superseded and the maintainers' implementations merged. M7 remains a separate audit outcome.

### Apache TVM-FFI · a finding continued at another layer

Our structural-hash finding and proposed repair in [#897](https://github.com/apache/tvm-ffi/pull/897) were explicitly linked to the maintainer’s [#898](https://github.com/apache/tvm-ffi/pull/898). The successor changes short moved-string construction rather than our hashing layer. It was OPEN at the recorded observation; our PR was superseded, not merged. [Timeline, source paths and limits](reports/tvm-ffi-2026-11.md#english-summary).

### BlackJAX

Our [PR #1068](https://github.com/blackjax-devs/blackjax/pull/1068) merged on 2 November through `junpenglao`. Stable `softplus` prevents intermediate overflow in Barker proposal probabilities and the acceptance ratio. A NumPy density oracle found 142 base mismatches and zero after the fix across 768 CPU steps; all 384 ordinary controls already passed on the base. [Case and validation scope](reports/blackjax-2026-11.md#english-summary).

### Braintrust

Our [PR #2701](https://github.com/braintrustdata/braintrust-sdk-javascript/pull/2701) merged on 2 November through `lforst`. A stateful `TextDecoder` preserves UTF-8 characters split across logging byte-stream chunks. The original focused run had 6 failures / 13 passing controls; related suites passed 178 tests on both tested Node versions. [Case and test scope](reports/braintrust-2026-11.md#english-summary).

### Kraft

Our [PR #1227](https://github.com/itsOmidKarami/kraft/pull/1227) merged on 2 November through `itsOmidKarami`. Repeated user-scope `kraft admin init` refreshes skills when its MCP server already exists; genuine errors still stop before writes. The focused suite passed 16 tests; `just ci-checks` and mutation checks passed. [Case and subprocess boundary](reports/kraft-2026-11.md#english-summary).

### TensorDict

Merged maintainer [PR #3427](https://github.com/pytorch/tensordict/pull/3427) explicitly credits our earlier fix. The [closing acknowledgement](https://github.com/pytorch/tensordict/pull/3426#issuecomment-6563347852) thanks the report and thorough tests, and explains the smaller solution: delegate to PyTorch's loader rather than copy it. Our [#3426](https://github.com/pytorch/tensordict/pull/3426) was superseded, **not merged**. [Contribution, validation and implementation authorship](reports/tensordict-2026-11.md#english-summary).

### FilesDrop

Expired-file cleanup retains failed removals for retry; URL-upload cancellation covers waiting for DNS. Our code was merged on 21 October. [Details and test scope](reports/filesdrop-2026-10.md#english-summary).

### Prime Intellect

The maintainer explicitly acknowledged that our reproduction and investigation shaped the fix. Their implementation was merged in [Verifiers #2973](https://github.com/PrimeIntellect-ai/verifiers/pull/2973) and [prime-rl #4243](https://github.com/PrimeIntellect-ai/prime-rl/pull/4243). Our [PR #2925](https://github.com/PrimeIntellect-ai/verifiers/pull/2925) was superseded and was not merged. Another contributor filed the original issue. [Contribution and design trade-off](reports/prime-intellect-2026-10.md#english-summary).

### M7

The project published a known-issues roadmap and its first maintenance release after an external review. The [source-pinned sprint document](https://github.com/DukeDeSouth/m7-mcp-oss/blob/6625fce7e07b4e5ba99fe0572b05a3d6c7b96ca0/docs/COMMUNITY_SPRINT.md) credits DiadkoShmek for review context. Our contribution is audit and triage; the maintainers implemented the fixes. [Audit, original PDF and follow-up boundaries](reports/m7-2026-10.md#english-summary).

## Competitions and arenas

| Observation date | Event | Result | Scope |
|---|---|---|---|
| 21 Oct 2026 | CodinGame · Mad Pod Racing | Legend League · 86/1657 | Dated league-ranking snapshot |
| Checked 27 Oct 2026 | Zoria 2026 · UA SKILLS | Season prize winner | Organizer announcement; exact final placement not established here |
| 19 Oct 2026 | Zoria 2026 | 5/9 | Historical preliminary second-stage table |

### CodinGame · Mad Pod Racing

Account: [Architect.](https://www.codingame.com/profile/effff781bd270b96c3fddbba39a29b4a7099847). The result is **86 of 1657 within Legend League**, observed on 21 October 2026, Europe/Helsinki. It is a moving ranking, not a final tournament result, an all-player rank or a current-rank promise. Sources: [official arena](https://www.codingame.com/multiplayer/bot-programming/mad-pod-racing) and [leaderboard](https://www.codingame.com/multiplayer/bot-programming/mad-pod-racing/leaderboard).

![Dated CodinGame league-ranking evidence](evidence/codingame-2026-10-21.jpg)

### Zoria 2026 · UA SKILLS

UA SKILLS named `diadkoshmek` among five season prize winners in its [public organizer announcement](https://ua.linkedin.com/company/ua-skills), checked on 27 October. That check date is not asserted to be the publication date. This entry establishes prize-winner status without claiming an exact final rank or payment.

The separate [19 October preliminary table](https://zoria.net/news/#19102026-попередній-підсумок-другого-етапу) placed the account fifth among nine second-stage participants and excluded episode R3. It remains a preliminary record. Tournament code and operational material remain private.

## How this record grows

Each result retains a date, role, primary source and evidence boundary. Merged code, an investigation informing a maintainer's fix, and an acknowledged audit are distinct outcomes. Later releases and rechecks receive dated updates; Git retains earlier records. Local tests are not official competition results, and prize announcements are separate from payment.

[Profile](https://github.com/DiadkoShmek) · [Engineering cases](ENGINEERING.md)
