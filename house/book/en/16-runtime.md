# 16. Runtime across interruption

I place a changeable model inside a durable runtime. History, ownership and action authority should survive a model change.

Continuity does not mean there will never be an interruption. It means that afterwards enough relationships can be recovered to understand where work stopped and what remains unknown. For that, history must be more durable than any one session.

The model may change, but the change must not rewrite past events. Imagine returning to a repair: the new collaborator needs the proposal, the actual change and the decision about it, not the impression that all of this happened in one uninterrupted conversation.

After an interruption, the same event may arrive again. If its ID and bytes match an accepted record, rereading it should not change state a second time. If the same ID carries different content, that is a conflict to expose. This distinction lets work recover without inventing what happened between two visits.

![An exact retry returns its receipt. A different write against an old revision receives a conflict.](../../assets/diagrams/recovery-en.svg)

*An exact retry returns its receipt. A different write against an old revision receives a conflict.*

In the portable Omnigen target, a SQLite event stream is canonical. Append validates schema and ingress, opens BEGIN IMMEDIATE, attests the prefix and predecessor hash. The same event ID and bytes mean a retry; different bytes under that ID are refused. A semantic reducer checks the transition before commit.

State is rebuilt from one verified prefix; recovery capture keeps events and their matching snapshot together. Current cold replay starts from genesis. A model-route change is a separate event, not a rewrite of history. Compatible deterministic adapters here do not imply arbitrary connected providers.

This is a target implementation, separate from the current OpenClaw organs. I transfer ownership per organ after compatibility and consumer checks. A hash chain describes integrity between linked records; it does not by itself authenticate the truth of their content or an independent author.

Evidence basis: [B11](../../EVIDENCE.md#b11).

← [Previous](15-continuity.md) | [Next](17-mirror.md) →
