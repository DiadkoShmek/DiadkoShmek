# 14. Shadow: mathematics as an instrument

A mathematical workshop matters when a formula becomes a computation, an example and a counterexample.

A formula becomes a working instrument when I can give it data, compute a result and construct a case where intuition fails. Such a workshop lets me do more than name an idea: it lets me test its boundary on a small example.

For text search I can score neighboring characters and compare candidates. An algorithm can temporarily accept a worse candidate to escape a local trap. That does not guarantee the best answer; it describes one concrete way to explore a space of possibilities.

Entropy in the formula below measures uncertainty in a distribution, while the acceptance rule describes one search step. Neither should be confused with a security guarantee or a universal measure of meaning. A check must concern the particular implementation I use.

| Family | What is implemented |
| --- | --- |
| Information and statistics | Character and n-gram entropy, conditional entropy, index of coincidence and chi-square. |
| Search | N-gram log-likelihood, coordinate improvement, restarts and simulated annealing. |
| Algebra | Modular inverses, matrices over rings and elliptic-curve arithmetic. |
| Finite fields and codes | GF(2^8), GF(2^128), block transformations, Hamming and cyclic-code syndromes. |

Entropy makes the difference between a formula and an instrument concrete. With only one possible outcome, H(1) = 0: there is no uncertainty of choice. For two equally likely outcomes, H(1/2, 1/2) = 1 bit. The calculation is exact within its model; whether that model describes the actual problem is the next question.

For example, a bigram language model sums neighboring-character log probabilities. Search changes a candidate and compares its score. Simulated annealing sometimes accepts a worse move with a temperature-dependent probability to escape a local optimum. This is a concrete algorithmic mechanism that can be checked on controlled texts.

$$
H(X)=-\sum_x p(x)\log_2 p(x)
$$

A specific snapshot has a retained independent isolated run of 55 tests. I present the workbench as a mathematical and educational laboratory, combining theory, numerical transformations and edge-case checks. Implementing a cryptographic primitive does not make it a hardened library or demonstrate a break of modern cryptography.

Evidence basis: [B09](../../EVIDENCE.md#b09).

← [Previous](13-order.md) | [Next](15-continuity.md) →
