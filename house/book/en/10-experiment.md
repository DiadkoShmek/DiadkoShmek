# 10. Experiments, not one attractive number

I want both the fact that training ran and the exact meaning of its metrics. They answer different questions.

| Question | What survives in this snapshot |
| --- | --- |
| Did training run? | A numeric 400-step log and saved weights with compatible tensor shapes. |
| Which metric? | Training-minibatch cross-entropy: 6.4814 → 3.4941; final reported perplexity 32.92. |
| What does a checkpoint retain? | Nine parameter tensors and V/E/H dimensions. No Adam moments, RNG state or saved character dictionary. |
| Are all derivatives verified? | A narrow finite-difference checker exists; full independent verification of all gradients was not established. |

Training uses 64-character sequences, batches of 48 and one-character-shifted targets. Loss is measured on the current training batch before its update. Its decrease describes optimization on that stream; it is not a held-out score or a measure of meaningful answers.

The handwritten backward pass has a flagged reset-gate derivative discrepancy: the contribution through r × previous_h must be multiplied by r when propagated to previous_h. This version remains research software. Other retained checkpoint families need exact run manifests of their own; filenames cannot substitute for experiment history.

Evidence basis: [B06](../../EVIDENCE.md#b06).

← [Previous](09-neural.md) | [Next](11-model-plane.md) →
