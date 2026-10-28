# 08. From experience to training data

I develop the in-house model direction through separate layers: material, transformation, evaluation and training. Each produces a different kind of result.

Experience can become training material, but not automatically. Between an event and a training example lies a series of choices: what to retain, which mistake to name, which answer counts as a repair, and how to check that the example is not repeated in evaluation.

One document can produce dozens of fragments. If some enter training while very similar neighboring passages enter evaluation, a good score may reflect recognition of familiar text. A split should therefore keep related fragments together. Data provenance can change what a number means before training even begins.

This is why I treat corpus counts carefully. A count describes the amount of material, not its semantic quality, and does not prove that a lesson transfers. A split and a manifest make a particular experiment reproducible and interpretable.

| Layer | Concrete form |
| --- | --- |
| Structured turns | Question, sources, reasoning, counterexample, outcome and next question. |
| Export | Separate formats for reasoning, instruction/response, completion and mistake→fix pairs. |
| Mixture and split | File groups remain wholly in train or test; records lacking file IDs are split separately by source. |
| Checks | Deduplication, provenance checks, lexical baselines and separate contamination reports. |

The division of material also matters for trusting a conclusion. If nearly identical documents appear in both training and evaluation, success may mean recognition rather than an ability to handle a new case. I therefore look at where examples came from, not just at the final score.

The retained mixture contains 3,010 records. A reproducible experiment needs a consistent manifest for the exact mixture, split and code: train/test filenames alone do not establish shared lineage. I therefore separate the existence of material from an admitted training dataset.

A correction label also has a method behind it. Some labels come from regular expressions; repeated lessons are screened with word-set Jaccard similarity. These are useful sorting tools. Semantic correctness and transfer to another task are separate questions.

Evidence basis: [B05](../../EVIDENCE.md#b05).

← [Previous](07-pole-memory.md) | [Next](09-neural.md) →
