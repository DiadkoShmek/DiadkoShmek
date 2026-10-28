# 08. From experience to training data

I develop the in-house model direction through separate layers: material, transformation, evaluation and training. Each produces a different kind of result.

| Layer | Concrete form |
| --- | --- |
| Structured turns | Question, sources, reasoning, counterexample, outcome and next question. |
| Export | Separate formats for reasoning, instruction/response, completion and mistake→fix pairs. |
| Mixture and split | File groups remain wholly in train or test; records lacking file IDs are split separately by source. |
| Checks | Deduplication, provenance checks, lexical baselines and separate contamination reports. |

The retained mixture contains 3,010 records. A reproducible experiment needs a consistent manifest for the exact mixture, split and code: train/test filenames alone do not establish shared lineage. I therefore separate the existence of material from an admitted training dataset.

A correction label also has a method behind it. Some labels come from regular expressions; repeated lessons are screened with word-set Jaccard similarity. These are useful sorting tools. Semantic correctness and transfer to another task are separate questions.

Evidence basis: [B05](../../EVIDENCE.md#b05).

← [Previous](07-pole-memory.md) | [Next](09-neural.md) →
