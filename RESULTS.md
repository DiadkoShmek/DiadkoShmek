# Зовнішні результати

> **Поточний зріз 05.11.2026, 19:07 UTC: 10 власних merged, 4 внески у злиті fixes мейнтейнерів; 134 PR, 116 OPEN, 8 CLOSED без merge.** [Книга й чинний журнал](https://github.com/DiadkoShmek/engineering-results) · [Усі PR](https://github.com/DiadkoShmek/engineering-results/blob/main/PR_STATUS.md).
> **Нове:** [Instructor #2866 → merged #2899](https://github.com/DiadkoShmek/engineering-results/blob/main/reports/instructor-2026-11.md). Нижче - історичний зріз 02.11.2026; його стани не є поточними.

Внески у відкриті проєкти, технічні аудити й результати змагань. Кожен запис містить дату, внесок, зовнішнє джерело та фактичний статус. Реалізація й дослідження виконувалися з AI-інструментами.

[English](RESULTS.en.md) · [Інженерні кейси](ENGINEERING.md) · [Машиночитані записи](results.json)

## Внески та аудити

| Дата результату | Проєкт | Наш внесок | Зовнішній результат |
|---|---|---|---|
| 21.10.2026 | [FilesDrop](reports/filesdrop-2026-10.md) | Два виправлення API та регресійні перевірки | [PR #32 злитий](https://github.com/AndreyBegma/FilesDrop/pull/32) |
| 24.10.2026 | [Prime Intellect · Verifiers / prime-rl](reports/prime-intellect-2026-10.md) | Дослідження, відтворення помилки, запропонований patch | [Мейнтейнер підтвердив вплив на виправлення](https://github.com/PrimeIntellect-ai/verifiers/pull/2925#issuecomment-6385135636); його реалізація злита у двох репозиторіях |
| 29.10.2026 | [M7 MCP](reports/m7-2026-10.md) | Незалежний технічний аудит і перевірка першого пакета виправлень | [Реліз v3.18.1 публічно відзначає review/triage](https://github.com/DukeDeSouth/m7-mcp-oss/releases/tag/v3.18.1); реалізація — maintainers |
| 01.11.2026 | [TensorDict](reports/tensordict-2026-11.md) | Відтворення, запропонований fix і thorough tests | [Maintainer #3427 злитий із credit](https://github.com/pytorch/tensordict/pull/3427); наш #3426 superseded |
| 02.11.2026 | [Braintrust SDK JavaScript](reports/braintrust-2026-11.md) | Streaming UTF-8 decoder і регресії | [Наш PR #2701 злитий](https://github.com/braintrustdata/braintrust-sdk-javascript/pull/2701) |
| 02.11.2026 | [Kraft](reports/kraft-2026-11.md) | Refresh skills при вже зареєстрованому MCP server | [Наш PR #1227 злитий](https://github.com/itsOmidKarami/kraft/pull/1227) |
| 02.11.2026 | [BlackJAX](reports/blackjax-2026-11.md) | Стабільні proposal probabilities і acceptance ratio Barker MCMC | [Наш PR #1068 злитий](https://github.com/blackjax-devs/blackjax/pull/1068) |
| 02.11.2026 | [Apache TVM-FFI](reports/tvm-ffi-2026-11.md) | Виявлений дефект structural hashing, запропонований fix і регресії | [Мейнтейнер замінив #897 на #898](https://github.com/apache/tvm-ffi/pull/897#issuecomment-6588300834); наступний PR ще OPEN |

### Зріз 02.11.2026

**Чотири власні merged PR:** FilesDrop #32, Braintrust #2701, Kraft #1227 і BlackJAX #1068. **Два окремі credited contributions:** Prime Intellect і TensorDict — наші пропозиції superseded, реалізації мейнтейнерів злиті. Окремо: Apache TVM-FFI #897 superseded мейнтейнерським #898, який ще OPEN. M7 залишається окремим результатом аудиту.

### Apache TVM-FFI · finding продовжився в іншому шарі

Наш structural-hash finding і запропоноване виправлення у [#897](https://github.com/apache/tvm-ffi/pull/897) мейнтейнер пов’язав із власним [#898](https://github.com/apache/tvm-ffi/pull/898). Він змінив конструктор коротких moved strings замість нашого шару хешування. На зафіксованому зрізі наступний PR OPEN; наш superseded, не merged. [Хронологія, source paths і межі](reports/tvm-ffi-2026-11.md).

### BlackJAX · числова стабільність MCMC

Наш [PR #1068](https://github.com/blackjax-devs/blackjax/pull/1068) злитий 02.11.2026 через `junpenglao`. Стабільний `softplus` прибирає проміжне переповнення у ймовірностях пропозиції Barker sampler. NumPy density oracle: 142 розбіжності на базі → 0 після виправлення у 768 CPU-кроках; 384 звичайні контролі проходили й до зміни. [Кейс і межі перевірки](reports/blackjax-2026-11.md).

### Braintrust · Unicode збережено між chunks

Наш [PR #2701](https://github.com/braintrustdata/braintrust-sdk-javascript/pull/2701) злитий 02.11.2026 через `lforst`. Stateful `TextDecoder` зберігає UTF-8 символи, розділені між chunks потокового логування. Початкові focused tests: 6 failed / 13 passed; пов'язані suites після виправлення: 178 passed на двох Node versions. [Кейс і межі перевірки](reports/braintrust-2026-11.md).

### Kraft · повторна ініціалізація без втрати refresh

Наш [PR #1227](https://github.com/itsOmidKarami/kraft/pull/1227) злитий 02.11.2026 через `itsOmidKarami`. Повторний user-scope `kraft admin init` оновлює skills при вже наявній MCP-реєстрації; справжні помилки й далі зупиняють запис. Focused suite: 16 passed; `just ci-checks` і mutation checks пройшли. [Кейс і subprocess boundary](reports/kraft-2026-11.md).

### TensorDict · внесок відзначено у меншому maintainer fix

[PR #3427](https://github.com/pytorch/tensordict/pull/3427) злитий 01.11.2026 й прямо посилається на наш попередній fix. Мейнтейнер [подякував за report і thorough tests](https://github.com/pytorch/tensordict/pull/3426#issuecomment-6563347852) та обрав виклик власного loader PyTorch замість його копії. Наш [#3426](https://github.com/pytorch/tensordict/pull/3426) superseded, **не злитий**. [Внесок, перевірки та авторство реалізації](reports/tensordict-2026-11.md).

### FilesDrop · код прийнято

Очищення прострочених файлів зберігає невдалі видалення для повтору; deadline URL-upload діє також під час очікування DNS. **Наш PR #32 злитий 21 жовтня.** [Зміна й перевірки](reports/filesdrop-2026-10.md).

### Prime Intellect · дослідження використано у виправленні

Мейнтейнер прямо підтвердив, що наше дослідження й відтворення сформували виправлення. Його варіант злитий у [Verifiers #2973](https://github.com/PrimeIntellect-ai/verifiers/pull/2973) та [prime-rl #4243](https://github.com/PrimeIntellect-ai/prime-rl/pull/4243). Наш [PR #2925](https://github.com/PrimeIntellect-ai/verifiers/pull/2925) закритий як superseded, **не злитий**. Початкову задачу відкрив інший учасник. [Розбір внеску](reports/prime-intellect-2026-10.md).

### M7 · аудит дійшов до roadmap і релізу

Після зовнішнього review проєкт опублікував реєстр проблем, план виправлень і перший maintenance release. [План спринту на зафіксованому commit](https://github.com/DukeDeSouth/m7-mcp-oss/blob/6625fce7e07b4e5ba99fe0572b05a3d6c7b96ca0/docs/COMMUNITY_SPRINT.md) прямо посилається на DiadkoShmek. Наш внесок — аудит і review/triage; код виправлень написали maintainers. [Кейс, PDF та межі повторної перевірки](reports/m7-2026-10.md).

## Змагання й арени

| Дата результату | Змагання | Результат | Статус |
|---|---|---|---|
| 21.10.2026 | CodinGame · Mad Pod Racing | Legend League · 86/1657 у цій лізі | Зріз рухомого рейтингу |
| 27.10.2026, перевірено | Zoria 2026 · UA SKILLS | Призер першого сезону | Оголошено організатором; без точного фінального місця |
| 19.10.2026 | Zoria 2026 | 5/9 у попередньому загальному підсумку | Попередній, не фінальний |

## CodinGame · Mad Pod Racing

- **Акаунт:** [Architect.](https://www.codingame.com/profile/effff781bd270b96c3fddbba39a29b4a7099847).
- **Формат:** постійна арена bot programming.
- **Зафіксовано:** 21.10.2026, Europe/Helsinki.
- **Результат:** Legend League, місце **86 із 1657 учасників ліги**. Це не місце серед усіх зареєстрованих у грі.
- **Джерело:** [офіційна арена](https://www.codingame.com/multiplayer/bot-programming/mad-pod-racing) і [рейтинг](https://www.codingame.com/multiplayer/bot-programming/mad-pod-racing/leaderboard).
- **Робота:** C++-бот для двох машин; локальні перевірки фізики й політики перед зіставленням з реальною ареною. Розробка з AI-інструментами.

Рейтинг змінюється з новими матчами й учасниками. Цей запис не є заявою про поточне місце на будь-яку майбутню дату або про найкраще місце за весь час.

![CodinGame: Architect., Legend League, 86/1657 — зріз 21.10.2026](evidence/codingame-2026-10-21.jpg)

## Zoria 2026 · підсумок UA SKILLS

**`diadkoshmek` — призер першого сезону Zoria.** Організатор UA SKILLS публічно назвав акаунт серед п’яти призерів у повідомленні про завершення сезону.

- **Що це:** інженерний турнір із системної розробки; робота над ігровим ботом, штабом керування та стратегією за обмежених ресурсів.
- **Організатор:** [UA SKILLS](https://ua-skills.com/).
- **Джерело:** [оголошення UA SKILLS про завершення першого сезону](https://ua.linkedin.com/company/ua-skills).
- **Перевірено:** 27.10.2026, Europe/Helsinki. Дата перевірки не підміняє дату публікації оголошення.

Оголошення підтверджує статус призера; точне місце у фінальній таблиці цим записом не встановлюється. Таблиця на `zoria.net/news/` на момент перевірки була недоступна. Раніше зафіксовані **5/9** нижче стосуються попереднього підсумку другого етапу. Суму нагороди й виплату тут не фіксую.

## Zoria 2026 · попередній підсумок

- **Акаунт:** `diadkoshmek`.
- **Формат:** турнір системної розробки, бот та ігровий штаб.
- **Результат відкритої таблиці від 19.10.2026:** **5-те місце серед 9 учасників другого етапу**.
- **Джерело:** [офіційний попередній підсумок](https://zoria.net/news/#19102026-попередній-підсумок-другого-етапу).
- **Перевірено:** 21.10.2026, Europe/Helsinki; у відкритому джерелі ще попередня таблиця.
- **Статус:** остаточний підсумок запланований на 21.10.2026, 18:00 UTC / 21:00 Europe/Helsinki.

Опублікована таблиця від 19.10 не включає оцінку епізоду Р3. Це історичний запис попереднього етапу, а не остаточна таблиця. Подальше оголошення організатора про призерів наведене окремо вище.

Код турнірного репозиторію та службові матеріали залишаються приватними; ця сторінка не є їх публікацією.

## Як поповнюється журнал

- Новий результат — новий датований запис; старі зрізи не переписуються на нові.
- Для внеску розрізняю власний merged patch, дослідження, використане в чужій реалізації, та аудит із зовнішнім підтвердженням.
- Зберігаю першоджерело, роль і автора реалізації. Новий реліз або повторна перевірка додає датоване уточнення; історичні дані залишаються доступними в Git.
- Для місця зазначаю арену або турнір, лігу/етап, дату, джерело й доступний доказ.
- Локальні тести та спаринги не називаю офіційними результатами.
- Нагороду фіксую після офіційного оголошення; отримання коштів — лише після фактичної виплати.

[Машиночитані записи](results.json) · [Профіль](https://github.com/DiadkoShmek)
