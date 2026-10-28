# 12. Mathematics of sufficient state

One central question in the House is how much history must survive for the next decision to be possible at all.

Compression is necessary: no one can carry the entire history every time. But every compression discards something. Before asking a system to answer, I want to know whether its representation still contains the information on which the right answer depends.

Imagine two streams with identical aggregate counts but different event orders. If the next decision depends on what happened first, equal totals are insufficient. Compression has lost precisely the distinction needed to choose an action. Sufficiency starts with the decision we want to preserve.

The formula below states the condition precisely: the target must be constant over each set of histories compressed to the same representation. It does not say how to find a good representation; it lets me rule out one that has already erased a necessary distinction.

![Two histories have the same counts but different order. Counts alone cannot recover which event happened first.](../../assets/diagrams/fibers-en.svg)

*Two histories have the same counts but different order. Counts alone cannot recover which event happened first.*

Let P compress a history x into a representation, and let T(x) be the required answer. Exact recovery through that representation is possible only when every pair of histories with the same P also shares the same T. Otherwise one input demands two different answers. Model confidence cannot recover information removed by the representation.

$$
T=g\circ P\quad\Longleftrightarrow\quad P(x)=P(y)\Rightarrow T(x)=T(y)
$$

I use this as a design instrument for memory and evaluation. In finite CreditWorld, a history-aware reference distinguished 16 of 16 development cases; the memoryless projection had an 8-of-16 ceiling. Missing feedback and incorrect links were checked separately. This is a controlled demonstration of state sufficiency, not an evaluation of a trained LLM.

Evidence basis: [B08](../../EVIDENCE.md#b08).

← [Previous](11-model-plane.md) | [Next](13-order.md) →
