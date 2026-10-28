# 05. Events, messages and receipts

Communication becomes infrastructure when it survives interruption and preserves the exact content of an attempt.

A message is an attempt to carry a thought across time and between working contexts. It must retain its content even when the sender has finished and the recipient has not yet returned. Without that, a conversation easily becomes an assumption about what someone else supposedly heard.

I distinguish what was sent, read and done. A message proposing a repair may be delivered while the change itself is still under discussion. After an interruption, no one should read delivery as proof of acceptance.

The mechanisms below serve that simple distinction. They preserve a message’s identity and make it possible to recover a coherent view. Their value lies not in infrastructure complexity, but in letting the next conversation begin from a truthful place.

Mail begins as a JSON envelope in the sender’s outbox. Publication does not overwrite an existing letter. The courier reconciles exact bytes, recipient state and receipt, and visits nonempty mailboxes fairly so one busy sender cannot starve a quieter one.

Communication has another human dimension: it lets me stop holding everything in my head. I can return later and see where a conversation stopped. Yet a deferred question does not become an answer merely because it was reliably preserved.

| Mechanism | Failure it addresses |
| --- | --- |
| Exact bytes and a stable ID | A retry must not create different content under the same identity. |
| Receipt separate from the letter | Publication, reading and execution remain distinct states. |
| Event and state in one transaction | The journal cannot successfully claim a transition absent from work state. |
| Role/revision reducer | A stale or unauthorized transition is not admitted because its prose sounds convincing. |

For isolated readers I use immutable projection generations. A reader receives a coherent file set, not the central database or permission to alter it. If state advances during the read, the old set remains an explicitly old set.

Evidence basis: [B03](../../EVIDENCE.md#b03).

← [Previous](04-autonomy.md) | [Next](06-memory.md) →
