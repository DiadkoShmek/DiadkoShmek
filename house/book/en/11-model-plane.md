# 11. Model plane and resource ownership

An agent’s main model and a local specialist do different work. I connect them through a controlled tool layer.

![Success includes child termination and resource release. The result must also belong to the current request.](../../assets/diagrams/support-en.svg)

*Success includes child termination and resource release. The result must also belong to the current request.*

Stage4 combines Nomic embeddings, Qwen3-Reranker 0.6B and LateOn-Code CPU. One worker coordinates the resource lease, mutual exclusion, fresh capacity observations and settings generations. Code lookup runs in an ephemeral child; the parent accepts output after order checks, cleanup and reaping.

The native plugin also checks agent, session, turn and step. A valid answer for a step that is no longer current must be rejected. Settings rollback creates a new generation instead of rewinding a number. Provenance and resource ownership therefore become part of result correctness.

A retained seven-route readback records actual calls through this layer. Load boundaries and negative CPU cases remain in evaluation. Model count is not my substitute for route quality.

Evidence basis: [B07](../../EVIDENCE.md#b07).

← [Previous](10-experiment.md) | [Next](12-sufficiency.md) →
