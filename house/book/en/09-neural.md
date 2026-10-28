# 09. My neural workshop

This direction already includes training, weights and an in-house neural implementation. It is a distinct technical layer that older corpus documentation can easily obscure.

I want to see learning from the inside, at a scale where each transformation can still be followed. A small character network offers that opportunity: it receives preceding characters and tries to predict the next, gradually changing its weights.

The hidden state is not a complete record of what was read. It is a limited representation carried between steps; gates govern how the previous state and a new candidate combine. After the beginning of a word, for example, the network can use that state to distribute probability over the next character.

This is a workshop for examining a mechanism, not a shortcut to a claim of general understanding. Its dimensions, formula and update procedure matter because they let me ask a concrete question about a concrete implementation.

![Conceptual GRU forward pass. Backpropagation and derivative verification are a separate implementation concern.](../../assets/diagrams/gru-en.svg)

*Conceptual GRU forward pass. Backpropagation and derivative verification are a separate implementation concern.*

This scale has its own value: I can compare what the formula promises with what the code actually does. If they diverge, that discrepancy needs investigation; the name of an architecture cannot transfer its guarantees to every implementation.

The character-level GRU is implemented in NumPy. A character maps to a 64-dimensional embedding; the hidden state has 192 coordinates. Reset and update gates control how the previous state enters the candidate and mixes with it. A linear projection and softmax produce the next-character distribution.

$$
h_t=(1-z_t)\odot h_{t-1}+z_t\odot\widetilde h_t
$$

The implementation includes manual backpropagation through time, embedding-gradient accumulation, bias-corrected Adam and gradient-norm clipping. The base checkpoint has 315,339 parameters; inspected variants with a different vocabulary have 326,904. This is a small trainable character language model, not a completed large conversational LLM.

Evidence basis: [B06](../../EVIDENCE.md#b06).

← [Previous](08-data.md) | [Next](10-experiment.md) →
