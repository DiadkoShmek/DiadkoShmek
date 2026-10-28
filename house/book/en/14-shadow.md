# 14. Shadow: mathematics as an instrument

A mathematical workshop matters when a formula becomes a computation, an example and a counterexample.

| Family | What is implemented |
| --- | --- |
| Information and statistics | Character and n-gram entropy, conditional entropy, index of coincidence and chi-square. |
| Search | N-gram log-likelihood, coordinate improvement, restarts and simulated annealing. |
| Algebra | Modular inverses, matrices over rings and elliptic-curve arithmetic. |
| Finite fields and codes | GF(2^8), GF(2^128), block transformations, Hamming and cyclic-code syndromes. |

For example, a bigram language model sums neighboring-character log probabilities. Search changes a candidate and compares its score. Simulated annealing sometimes accepts a worse move with a temperature-dependent probability to escape a local optimum. This is a concrete algorithmic mechanism that can be checked on controlled texts.

$$
H(X)=-\sum_x p(x)\log_2 p(x)
$$

A specific snapshot has a retained independent isolated run of 55 tests. I present the workbench as a mathematical and educational laboratory, combining theory, numerical transformations and edge-case checks. Implementing a cryptographic primitive does not make it a hardened library or demonstrate a break of modern cryptography.

Evidence basis: [B09](../../EVIDENCE.md#b09).

← [Previous](13-order.md) | [Next](15-continuity.md) →
