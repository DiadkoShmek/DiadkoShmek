# Інженерні кейси

[Книга, першоджерела та актуальна статистика](https://github.com/DiadkoShmek/engineering-results/blob/main/ENGINEERING.md)

Проблема → рішення → перевірка → зовнішній результат.

## Прийнятий код

- **[Microsoft Semantic Kernel](https://github.com/DiadkoShmek/engineering-results/blob/main/reports/semantic-kernel-2026-11.md):** завершення native generators у streaming invocation; #14701 merged.
- **[Redis Python client](https://github.com/DiadkoShmek/engineering-results/blob/main/reports/redis-monitor-2026-11.md):** cleanup невдалого MONITOR context entry; #4550 merged.

- **[ONNX](https://github.com/DiadkoShmek/engineering-results/blob/main/reports/onnx-range-2026-11.md):** точна довжина integer Range без переповнення; #8734 merged.
- **[ONNX IR](https://github.com/DiadkoShmek/engineering-results/blob/main/reports/onnx-ir-2026-11.md):** публічні output names під час усунення Identity; #521 merged.
- **[TensorLy](https://github.com/DiadkoShmek/engineering-results/blob/main/reports/tensorly-2026-11.md):** weights і mask у single-factor Khatri-Rao; #695 merged.
- **[BlackJAX](reports/blackjax-2026-11.md):** стабільні proposal probabilities у Barker MCMC; #1068 merged.
- **SDK та інтеграції:** [Braintrust #2701](reports/braintrust-2026-11.md), [Kraft #1227](reports/kraft-2026-11.md), [FilesDrop #32](reports/filesdrop-2026-10.md) — merged.

## Відзначені дослідження

- **[Prime Intellect](https://github.com/DiadkoShmek/engineering-results/blob/main/reports/prime-intellect-2026-10.md):** ізоляція агентів; наш patch superseded.
- **[TensorDict](https://github.com/DiadkoShmek/engineering-results/blob/main/reports/tensordict-2026-11.md):** partial checkpoints; наш #3426 superseded, #3427 merged із credit.
- **[TVM-FFI](https://github.com/DiadkoShmek/engineering-results/blob/main/reports/tvm-ffi-2026-11.md):** structural hash; наш #897 superseded, #898 merged із reference.

## Аудит і змагання

- **[M7 MCP](reports/m7-2026-10.md):** release credit у v3.18.1; PDF і focused follow-up.
- **[CodinGame · Mad Pod Racing](reports/codingame-2026-10.md):** негативні та умовні локальні результати окремо від арени.
- **[Zoria / UA SKILLS](RESULTS.md#zoria-2026--підсумок-ua-skills):** призер сезону.

## Як читати

Ігровий бот діє в матчі. AI-агент розробки досліджує, пише й тестує. Людина визначає напрям, володіє поданням, погоджує зовнішні дії й відповідає за супровід.

Це не контрольований порівняльний бенчмарк AI-моделей: час, вартість і втручання не виміряні зіставно. Власний merged patch, відзначене дослідження й аудит обліковані окремо.

[Книга результатів](https://github.com/DiadkoShmek/engineering-results) · [Історичний журнал](RESULTS.md) · [English results](RESULTS.en.md)

## Подана серія · 04.11.2026 UTC

[Лезо: 20 нових PR у 18 репозиторіях](https://github.com/DiadkoShmek/engineering-results/blob/main/reports/lezo-2026-11.md). Локальні перевірки, source commits і зовнішні стани зібрано в окремому звіті; pending подання не додаються до прийнятих мерджів.
