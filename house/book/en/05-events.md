# 05. Events, messages and receipts

Communication becomes infrastructure when it survives interruption and preserves the exact content of an attempt.

Mail begins as a JSON envelope in the sender’s outbox. Publication does not overwrite an existing letter. The courier reconciles exact bytes, recipient state and receipt, and visits nonempty mailboxes fairly so one busy sender cannot starve a quieter one.

| Mechanism | Failure it addresses |
| --- | --- |
| Exact bytes and a stable ID | A retry must not create different content under the same identity. |
| Receipt separate from the letter | Publication, reading and execution remain distinct states. |
| Event and state in one transaction | The journal cannot successfully claim a transition absent from work state. |
| Role/revision reducer | A stale or unauthorized transition is not admitted because its prose sounds convincing. |

For isolated readers I use immutable projection generations. A reader receives a coherent file set, not the central database or permission to alter it. If state advances during the read, the old set remains an explicitly old set.

Evidence basis: [B03](../../EVIDENCE.md#b03).

← [Previous](04-autonomy.md) | [Next](06-memory.md) →
