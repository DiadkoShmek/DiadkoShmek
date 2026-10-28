# 13. Order, invariants and counterexamples

Mathematics helps me establish a question’s boundary before a large experiment: does the data still contain what I am trying to measure?

## Aggregation removes part of the history

In a finite check, different event streams produced the same time aggregates but differed in the order in which each stream first attained its own maximum. That is an explicit non-identifiability witness, not merely a weak classifier score. Adding the two first-attainment timestamps recovered that specific target. It did not automatically reconstruct the full history or every other target.

## Changing units while preserving meaning

For a positive pair x,y, common scaling preserves r=(x-y)/(x+y). This normalized balance identifies the ratio of the coordinates but not their absolute scale; the zero pair is a separate case. I distinguish representation invariance from sufficiency for a particular target. If recency matters, equal balance can still conceal different answers.

## Extreme orderings do not always bound the result

For two internally ordered streams, I examine their admissible interleavings. Two extreme orderings can miss the worst intermediate one. Exhaustive small-case enumeration and Bellman-style dynamic programming provide different checking routes. A retained finite set covers eight cases and 292 paths. This is an exact instrument within its model, not a universal bound on the real world.

Evidence basis: [B08](../../EVIDENCE.md#b08).

← [Previous](12-sufficiency.md) | [Next](14-shadow.md) →
