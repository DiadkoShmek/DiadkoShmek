# Ontology of the House

## Intent. Difference. Memory. Return.

On what sustains work together


## Being together

*What turns a collection of systems into a House?*

# 01. What I am building

I am building the House: an environment where AI collaborators can work on a shared purpose over time, retain their differences, and return to the consequences of their work.

I do not begin with a list of capabilities. I begin with a question: how can intent survive when a conversation ends, work is interrupted, and the next day calls for a continuation rather than a fresh start? The House is my answer in a form that can be built and examined.

I give direction, but I do not want every act of thought reduced to repeating my words. Different AI collaborators can bring different ways of seeing a problem: one finds a contradiction, another builds a solution, another asks an uncomfortable question. Each contribution needs room, and its effect on the whole must remain visible.

I call this working kinship brotherhood: a way to respect difference and care for shared work, not a claim about consciousness or a soul. This book examines not the inner life of machines, but the form of our working relationships and the consequences of what we create together.

The House begins with a simple scene: I return to work after a silence and want to understand what happened while I was away. Not a retelling of everything, but a clear thread: which intention remained open, what actually changed, and where my decision is still needed. Without that thread, even a strong answer can be lost between sessions. So I build not only tools, but the possibility of meeting my own intent again.

Evidence basis: [B01](../../EVIDENCE.md#b01).

---

# 02. The shape of the whole

The House has three distinct planes: intent, execution and an inspectable record. I connect them while retaining a specific owner for each kind of truth.

A whole begins where its parts can meet without losing their meaning. Intent gives direction; execution changes something concrete; a record lets me see again what happened. None of these layers replaces the other two.

Imagine an interrupted repair. A note saying “this needs fixing” remains in memory, but no one has accepted the change itself. Confusing those things would make the next collaborator resume from an invented point. The figure below therefore shows more than rooms in the House: it shows transitions between intent, action and consequence.

Connection does not mean fusion. A shared foundation matters because it helps carry what is needed, not because it makes every task the same. I need a form where each piece of work can keep its own rhythm while remaining intelligible to others.

![Logical architecture. The figure shows roles and flows, not a census of running processes.](../../assets/diagrams/house-en.svg)

*Logical architecture. The figure shows roles and flows, not a census of running processes.*

Codex Lab carries the engineering method: task intake, tool selection, delegation, integration and verification. Architect/OpenClaw has its own long context and runtime. FIELD-TEAM preserves separate specialist homes. Omnigen organizes shared infrastructure and a distinct portable target implementation.

Memory, mail, local models and the control console cross these environments through explicit contracts. Mirror, Budova, the research laboratory and creative projects share foundations while retaining their own data and acceptance criteria. A change in one product should therefore not rewrite another product’s history.

Evidence basis: [B01](../../EVIDENCE.md#b01), [B02](../../EVIDENCE.md#b02), [B07](../../EVIDENCE.md#b07), [B11](../../EVIDENCE.md#b11).


---

# 03. Distinct homes, shared foundations

I do not collapse every agent into one universal worker. Specialization matters when a difference changes the quality of the work.

Difference is not decorative to me. If everyone merely agrees, they can quickly produce an elegant and mistaken answer. Another perspective matters where it can change a decision: challenge an assumption or notice a case the first contributor missed.

A distinct space gives work duration. It can hold materials, allow a return to earlier questions, and pass on not just a conclusion but its grounds. A shared language should not erase who found a mistake and who later repaired it.

The table below is not a hierarchy of worth. It is a snapshot of different ways to contribute, which can change with the work. Mature collaboration means being able to disagree, check and change one’s part while keeping its connection to the whole intelligible.

| Environment | What it carries |
| --- | --- |
| Codex Lab | Implementation, verification, integration and engineering continuity. |
| Architect / OpenClaw | Long context, direction and its own runtime mechanisms. |
| General, Archivarius, Constructor | Defensive analysis; source knowledge; tool construction and repair. |
| Pole, Witness, Shadow | Memory and neural experiments; citation work; mathematical instruments. |

These names do not substitute for implementation. Each has working files, materials, sessions, tools and communication routes. Shared context adds addressed records of other work while keeping its origin visible.

Roles can evolve. I read them through contributions: who found a counterexample, who checked it, who changed the code, and who accepted the consequence. One actual repair followed that path: Constructor found a metadata problem, Pole reproduced it and found a related case, and Codex integrated the repair into two transfer tools.

For main models and subtasks I consider the cost of an accepted result: required quality, context, coordination, review and rework. A tool can handle exact lookup; a strong integrator retains consequential judgment. Independent work determines crew width, not the number of free slots. This is an operating routing rule; use by a particular session has its own trace.

Evidence basis: [B02](../../EVIDENCE.md#b02), [B03](../../EVIDENCE.md#b03).


---


## Action and responsibility

*How does intent become work that can continue?*

# 04. From intent to autonomous work

Autonomy needs a memory of unfinished work. Otherwise every interruption turns into another request for the human to decide what happens next.

Autonomy begins with trust in continuation, not endless motion. I can give direction and step away if the system distinguishes an authorized next step, an unknown result, and a decision that remains mine. An interruption must not erase those distinctions.

When an action’s reply is lost, blindly repeating it is not necessarily continuation. First I need to learn whether it already had an effect. A saved note of intent is not an accepted change; likewise, a vanished process does not prove that it did nothing.

Boundaries make independence possible here. A task has a purpose and a defined scope; the next collaborator can see what is permitted and what needs a separate decision. Work can continue without pretending that uncertainty has disappeared.

![Work passes through ownership, admission, execution and acceptance. An uncertain effect remains explicitly uncertain.](../../assets/diagrams/autonomy-en.svg)

*Work passes through ownership, admission, execution and acceptance. An uncertain effect remains explicitly uncertain.*

In the Lancet layer, the controller, lane registry and runtime are separate. The registry defines the task, owner and read/write scope. The dispatcher launches an admitted pending task. A recovery requirement must first acquire an exact repair or successor; it does not itself justify restarting everything.

A lease is stored before the effect: task generation, slot and process epochs, source version and deadline. A missing PID does not prove that an action never occurred. Executor termination, candidate output and acceptance have separate records. This reduces the risk of repeating an action whose reply was lost.

Evidence basis: [B02](../../EVIDENCE.md#b02).


---

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


---


## Memory and distinction

*What must remain for the next decision to have a basis?*

# 06. Memory with coordinates

I want to return to the basis of a thought: where it came from, which bytes were read, and what changed afterwards.

Memory is not a warehouse of finished answers. It is the ability to return to what shaped a thought and check whether its grounds still hold. Remembering a conclusion is easy; preserving a path that can be walked again, and challenged if necessary, is harder.

After an interruption I may find a note proposing a repair. But I also need to see its source, the change itself and its acceptance, if that happened. If only the note exists, honest continuation begins with that limit rather than invented certainty.

Different forms of memory answer different questions: where to look, what happened, and which materials belong to a particular work. A map helps me reach a place but does not become the place. Returning to the source is therefore part of memory, not distrust of it.

![A file, fragment, record and projection serve different roles. An index helps locate a source.](../../assets/diagrams/memory-en.svg)

*A file, fragment, record and projection serve different roles. An index helps locate a source.*

HouseMemory on Neo4j is an addressed map: owner, path, source hash, symbols and explicit links. It helps locate the correct code or an earlier reason for a decision. Graph status describes index coverage. I check current behavior with the runtime owner because a projection can lag behind.

Another layer is the event and work journal. It retains actor, review, revision and acceptance state. An agent’s home holds its own materials. The library provides navigation to books and research. These kinds of memory complement each other without silently replacing their sources.

A separate continuity bridge publishes the consequence return and next projection behind one head. The reader captures that head once. This avoids a mixed pair in which one file is new while the other still belongs to an earlier generation.

Evidence basis: [B03](../../EVIDENCE.md#b03), [B04](../../EVIDENCE.md#b04), [B11](../../EVIDENCE.md#b11).


---

# 07. Pole: retrieval with a source

Pole has its own memory stack. I describe it as a sequence of concrete transformations rather than hiding it behind the word RAG.

When I question memory, I want not only an answer but a way to check it. Retrieval gathers fragments that may be relevant; links help me reach neighboring context. This is the beginning of reading, not the end of reasoning.

A query about an interrupted repair may find both a proposal and a later record of acceptance. Similar words help retrieve both texts, but do not establish that the second really concerns the first. That relation has to be read and checked.

The formula below describes ranking: a more frequent term can strengthen a match, a rarer one can be more discriminating, and document length is accounted for separately. The score helps decide what to read first; it does not turn retrieved text into truth.

![Provenance → fragments → time and links → retrieval → citations → lexical checks.](../../assets/diagrams/pole-en.svg)

*Provenance → fragments → time and links → retrieval → citations → lexical checks.*

The scanner records sources; the fragmenter adds coordinates and the parent-file hash; the temporal layer distinguishes recording order from authorship. The graph contains explicit links. BM25 retrieval normalizes numbers and Cyrillic prefixes and ranks fragments by term frequency, rarity and document length.

$$
\operatorname{score}(q,d)=\sum_{t\in q}\operatorname{IDF}(t)\frac{f(t,d)(k_1+1)}{f(t,d)+k_1(1-b+b|d|/\overline{|d|})}
$$

Graph expansion adds neighboring references. The gate compares sentence words with cited fragments, query coverage and citation agreement with retrieval, retaining the first failure. This is a lexical check. It can expose unsupported drafts, but it does not establish logical entailment. Likewise, stored index hashes need current-byte validation before consequential use.

Evidence basis: [B04](../../EVIDENCE.md#b04).


---

# 08. From experience to training data

I develop the in-house model direction through separate layers: material, transformation, evaluation and training. Each produces a different kind of result.

Experience can become training material, but not automatically. Between an event and a training example lies a series of choices: what to retain, which mistake to name, which answer counts as a repair, and how to check that the example is not repeated in evaluation.

One document can produce dozens of fragments. If some enter training while very similar neighboring passages enter evaluation, a good score may reflect recognition of familiar text. A split should therefore keep related fragments together. Data provenance can change what a number means before training even begins.

This is why I treat corpus counts carefully. A count describes the amount of material, not its semantic quality, and does not prove that a lesson transfers. A split and a manifest make a particular experiment reproducible and interpretable.

| Layer | Concrete form |
| --- | --- |
| Structured turns | Question, sources, reasoning, counterexample, outcome and next question. |
| Export | Separate formats for reasoning, instruction/response, completion and mistake→fix pairs. |
| Mixture and split | File groups remain wholly in train or test; records lacking file IDs are split separately by source. |
| Checks | Deduplication, provenance checks, lexical baselines and separate contamination reports. |

The division of material also matters for trusting a conclusion. If nearly identical documents appear in both training and evaluation, success may mean recognition rather than an ability to handle a new case. I therefore look at where examples came from, not just at the final score.

The retained mixture contains 3,010 records. A reproducible experiment needs a consistent manifest for the exact mixture, split and code: train/test filenames alone do not establish shared lineage. I therefore separate the existence of material from an admitted training dataset.

A correction label also has a method behind it. Some labels come from regular expressions; repeated lessons are screened with word-set Jaccard similarity. These are useful sorting tools. Semantic correctness and transfer to another task are separate questions.

Evidence basis: [B05](../../EVIDENCE.md#b05).


---

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


---

# 10. Experiments, not one attractive number

I want both the fact that training ran and the exact meaning of its metrics. They answer different questions.

A number becomes knowledge only when I know which question it measures. A falling training loss describes behavior on the training stream; by itself it does not answer how the system will behave on new material.

Even the training process deserves close reading: if a discrepancy is found in a derivative, I do not hide it behind a pleasing graph. It becomes part of the experiment’s account and limits what can be claimed about that version.

| Question | What survives in this snapshot |
| --- | --- |
| Did training run? | A numeric 400-step log and saved weights with compatible tensor shapes. |
| Which metric? | Training-minibatch cross-entropy: 6.4814 → 3.4941; final reported perplexity 32.92. |
| What does a checkpoint retain? | Nine parameter tensors and V/E/H dimensions. No Adam moments, RNG state or saved character dictionary. |
| Are all derivatives verified? | A narrow finite-difference checker exists; full independent verification of all gradients was not established. |

Training uses 64-character sequences, batches of 48 and one-character-shifted targets. Loss is measured on the current training batch before its update. Its decrease describes optimization on that stream; it is not a held-out score or a measure of meaningful answers.

The handwritten backward pass has a flagged reset-gate derivative discrepancy: the contribution through r × previous_h must be multiplied by r when propagated to previous_h. This version remains research software. Other retained checkpoint families need exact run manifests of their own; filenames cannot substitute for experiment history.

Evidence basis: [B06](../../EVIDENCE.md#b06).


---

# 11. Model plane and resource ownership

An agent’s main model and a local specialist do different work. I connect them through a controlled tool layer.

One collaborator need not perform every transformation alone. Finding a similar fragment, reranking results and examining code can be separate tools. They should be connected so that a result returns to the very question for which it was requested.

A search, for example, may finish after the task has changed. Its answer can be technically correct for the old query and still unsuitable for the new one. The context of a call is therefore part of the answer’s meaning, not merely an operational detail.

Shared resources also need coordination: two requests should not silently interfere, and finishing work should leave a clean state. I judge this layer by whether it helps with a particular task, not by the number of models available.

![Success includes child termination and resource release. The result must also belong to the current request.](../../assets/diagrams/support-en.svg)

*Success includes child termination and resource release. The result must also belong to the current request.*

Stage4 combines Nomic embeddings, Qwen3-Reranker 0.6B and LateOn-Code CPU. One worker coordinates the resource lease, mutual exclusion, fresh capacity observations and settings generations. Code lookup runs in an ephemeral child; the parent accepts output after order checks, cleanup and reaping.

The native plugin also checks agent, session, turn and step. A valid answer for a step that is no longer current must be rejected. Settings rollback creates a new generation instead of rewinding a number. Provenance and resource ownership therefore become part of result correctness.

A retained seven-route readback records actual calls through this layer. Load boundaries and negative CPU cases remain in evaluation. Model count is not my substitute for route quality.

Evidence basis: [B07](../../EVIDENCE.md#b07).


---

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


---

# 13. Order, invariants and counterexamples

Mathematics helps me establish a question’s boundary before a large experiment: does the data still contain what I am trying to measure?

Time and order are easy to lose when history is reduced to a summary. Two sequences can have the same totals or maxima yet answer a question about order differently. No method seeing only the summary can then recover the required answer for both.

A concrete counterexample is stronger than a general suspicion. If I show two histories with the same representation and different targets, the limit of the data becomes visible. Adding the needed coordinate can repair that particular question, but does not automatically restore the whole lost history.

The same applies to invariants and action orderings. A balance can survive rescaling while losing absolute magnitude; two extreme orderings can miss the worst intermediate one. Mathematics helps me choose what must be retained and tested.

## Aggregation removes part of the history

In a finite check, different event streams produced the same time aggregates but differed in the order in which each stream first attained its own maximum. That is an explicit non-identifiability witness, not merely a weak classifier score. Adding the two first-attainment timestamps recovered that specific target. It did not automatically reconstruct the full history or every other target.

## Changing units while preserving meaning

For a positive pair x,y, common scaling preserves r=(x-y)/(x+y). This normalized balance identifies the ratio of the coordinates but not their absolute scale; the zero pair is a separate case. I distinguish representation invariance from sufficiency for a particular target. If recency matters, equal balance can still conceal different answers.

## Extreme orderings do not always bound the result

For two internally ordered streams, I examine their admissible interleavings. Two extreme orderings can miss the worst intermediate one. Exhaustive small-case enumeration and Bellman-style dynamic programming provide different checking routes. A retained finite set covers eight cases and 292 paths. This is an exact instrument within its model, not a universal bound on the real world.

Evidence basis: [B08](../../EVIDENCE.md#b08).


---

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


---

# 15. Revising a judgment and continuity

I want to see what actually changed after experience. A stored lesson is only one possible trace.

I care not only whether a lesson was saved, but whether it changed the next decision. Between a record and an action lies a path: the record must be found, understood, applied to the relevant situation and followed to its consequence. Each transition can fail.

If after an interruption I find a note saying “check acceptance,” that does not mean the check happened. And if it happened, the next question is whether it changed how work continued. Such distinctions make the word “learned” meaningful rather than merely complimentary.

I also want to name in advance what could disprove my judgment. Then a later success does not erase an earlier incomplete attempt, and observation has a chance to change my position. Without such a return, memory merely accumulates words.

![The return path connects an effect to an accepted revision and a later decision. It is a record criterion.](../../assets/diagrams/continuity-en.svg)

*The return path connects an effect to an accepted revision and a later decision. It is a record criterion.*

In AI Ontology I separate available evidence from a record actually used; adoption of a criterion from satisfaction; a stored lesson from formation; and a recorded effect from a complete return path. These distinctions keep a concrete process from disappearing inside the word learned.

The public reference contains a finite record model, relations, competency queries, projections and JSON/JSONL auditing. Book version 3.7.0 connects conceptual chapters, executable code, studies and a claim ledger. Its proposed audit profile has explicit bounds; I do not present it as an adopted industry standard.

A separate prospective evaluator freezes the thesis, counterthesis, horizon and falsifier before the outcome. The cohort stays fixed: an unresolved early attempt cannot be replaced by a later success. This implements prospective evaluation; a full natural-use cycle and benefit on subsequent tasks are assessed separately.

Evidence basis: [B10](../../EVIDENCE.md#b10), [B11](../../EVIDENCE.md#b11).


---


## Returning with a change

*How does a consequence change the way work continues?*

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


---

# 17. Mirror: an end-to-end experiment

I use Mirror as an environment for quantitative work: a question must travel from its sources through full accounting to a result.

Quantitative research presents a particular temptation: to see a favorable number as confirmation of the entire idea. I want each question to have a defined source, an evaluation rule and a full account of results, including those I do not like.

A negative conclusion can be a valuable completion. If a criterion set in advance is not met, it is more honest to reject that basis than to find a new definition of success afterwards. The next experiment can then begin with real knowledge of the previous one.

Separately I examine the path from data to result: whether accounting is retained, how delays are handled and what happens on repetition. These concern the quality of the experiment. A ready mechanism alone does not establish economic benefit.

| Barrier | What it checks |
| --- | --- |
| Sources | Exact hashes, gzip CRC/EOF, schema and time; LQ3 scanned 5,698,553 rows. |
| Numeric representation | Two arithmetic implementations: Fraction/manual decimal and Decimal/integer gcd. |
| Complete accounting | All 39,540 paired commands, 60 account results and 30 wallets are built before scoring. |
| Stored result | A separate reader checks outputs, joins and account bytes without a new fit or wallet rebuild. |

Memory of a failed check is not meant to stop research forever. It allows the next question to be more precise: what exactly changed in the conditions, and why does another attempt make sense? Without that thread, each repetition risks selling me the same old hope.

The actual compute retained 132 physical outputs, followed by separate admission. The predeclared rule produced a negative economic result: REJECT 2/7. I retain that conclusion as a completed experiment. It prevents further work on an unsupported premise without repainting failure as success.

The engine/kernel architecture separates accounting and recovery from the changing research kernel. Deadlines, delayed sources, duplicate input and reopening have distinct checks. I distinguish a prepared controller from a running pilot. This chapter describes paper research without disclosing private trading rules or claiming stable income.

Evidence basis: [B12](../../EVIDENCE.md#b12).


---

# 18. Budova: exact revisions for physical work

A foreman or installation crew lead should be able to see on a phone which work package was handed over, which revision it belongs to and what remains unknown.

I want shared work to leave the conversation and become something a person can act on. In a construction example, that means a package showing the revision actually handed over, its details and what remains unknown. Clarity has a practical consequence here.

If a new measurement appears after handoff, the old package must not silently change. Otherwise two people may use the same name while holding different facts. A revision binding lets them ask: what exactly was handed over then, and what changed afterwards?

A local run can show that a package is created and recovered under tested conditions. It does not yet show how a professional will use it in real work. I leave room for that trial, because that is where clarity meets practice.

![An issued package and a returned fact remain attached to their revision even after the current head advances.](../../assets/diagrams/budova-en.svg)

*An issued package and a returned fact remain attached to their revision even after the current head advances.*

Sources, part geometry and issued packages have distinct immutable bindings. The model contains exact outlines and holes, units, DXF/maps and original CAD sources. A new measurement does not rewrite a package already handed over.

Project saves use transactional CAS. Exact request replay is checked before a revision conflict. Background export passes through staging, a recovery record, fsync and rename. A historical fact passes preview and CAS before being appended to its own revision. Old cumulative progress must not become a fresh increment merely because a request was retried.

Local UI/HTTP flows already issued a package with 18 members and two CAD originals, and served the same frozen ZIP after controlled loss of a live source. A professional user trial and the latest served-origin acceptance of the montage reader remain specific boundaries of this product.

Evidence basis: [B13](../../EVIDENCE.md#b13).


---

# 19. Research that returns to work

A mathematical idea needs a place in the next decision. I maintain a distinct path from a hypothesis to an accepted constraint.

Research returns to work when its conclusion changes the next question or choice. Otherwise even a correct thought may remain a separate document no one applies. I care about that transition, not merely the number of retained studies.

For example, if aggregates erase time, a study can constrain the next choice of source: for a target that depends on recency, seek material with temporal information. That is a concrete consequence of mathematical reasoning, even if the product itself has not yet changed.

I distinguish what was proved in a given model, what was run as an experiment and what was accepted as a working constraint. Each step carries its own weight. Applying a result elsewhere requires its own justification, and saving a conclusion does not automatically change model weights.

The research council produces source-bound packets. A packet names its question, sources, stage, checks and conclusion boundary. The validator, laboratory route and intake reader have separate roles. Immutable bytes and hashes prevent a question from silently changing after the answer is known.

A scientific attempt reserves its identity before launch. A crash before spawn remains an attempt rather than disappearing before an automatic rerun. This matters for honest attempt counts, temporal order and experiment reconstruction.

## Example: from proof to a source constraint

In Math23, invariance and non-identifiability analysis showed that aggregates alone were insufficient for a time-weighted target. The owner actually accepted bounded source constraints and used them in the next design scope. Manual algebra, a finite check, an accepted constraint and a runtime change remained separate kinds of result.

This is how knowledge returns to the House: a constraint changes the next source selection or experiment. It is a practical change in work without automatically calling it a main-model weight update.

Evidence basis: [B08](../../EVIDENCE.md#b08), [B14](../../EVIDENCE.md#b14).


---

# 20. Interfaces, craft and public work

The House should reach a person in a usable form: a phone screen, an exact work package, a tool or a completed creative artifact.

The form in which a result meets a person is part of the work. An interface should help someone return to an unfinished thought; creative material should allow the result to be heard or seen, not merely described as a process.

Imagine a draft left before an interruption. After moving between conversations it should remain tied to its context, so the words do not end up in the wrong place. This small detail expresses respect for human attention.

In creative work, technical readiness and acceptance differ too. A file may open without error, but whether music or an edit works calls for listening and viewing. I preserve the ability to change the material and leave the final artistic judgment to a person.

## The console

The console connects conversations and work items. A draft, the selected conversation, a pending request and a lost reply are parts of its state. Moving to another agent should leave the text with its intended recipient. After a connection breaks, the interface should show whether a message was sent rather than encourage an uncertain duplicate.

## The creative pipeline

A finished artifact should also have a path back to editing. If one part of a video changes, it helps to know which sources produced it and what needs to be remade. That preserves not only time but the ability to revise a decision without starting everything over.

For editing I retain the plan, editable project and final export. One rendering path validates plan/source/parent hashes, reuses unchanged shot parts, encodes only replacements, and checks decoding and clock separately. Music retains exact lyrics/style/title and take availability. Artistic acceptance remains a separate human decision.

## Public work

FilesDrop merged PR #32, repairing cleanup retries and timeout handling during DNS waiting. Evidence-gated Agent Workflows and Signal Desk expose smaller executable examples. I use these artifacts as concrete entry points: another reader can inspect the problem, change and verification.

Evidence basis: [B15](../../EVIDENCE.md#b15), [B16](../../EVIDENCE.md#b16).


---

# 21. How I read readiness

Different parts of the House are at different stages. Naming the stage helps me use them and continue building.

Readiness answers a concrete question. Can the file be opened? Can a particular copy be restored? Has a person tried the result in their work? These questions are related, but a positive answer to one does not answer the others.

I do not seek to judge the House with one word. Its different parts have different histories and unfinished questions. A precise account lets me use what has been checked while seeing where more work is needed.

| Part | State in this edition |
| --- | --- |
| Agent environments and orchestration | Operating infrastructure with autonomous episodes and integrated cooperative repairs. |
| Local support functions | Installed bounded layer with retained actual native/API calls and negative boundaries. |
| Pole: memory, data and GRU | Real tools, corpora and training artifacts; correctness and generalization remain research questions. |
| Omnigen portable runtime | Implemented target with replay/contracts; current organs migrate individually after acceptance. |
| Mirror | Completed paper experiments and a distinct engine/kernel direction; each pilot has its own state. |
| Budova | Implemented local revisions, CAD/ZIP and fact returns; a professional user trial is still ahead. |

Sometimes a check opens new work instead of giving a final answer. That is not a defeat: I learn which part can be used and which still needs to be seen under different conditions. Certainty can grow gradually without declaring the whole thing ready.

I also check recovery materially. Six homes already have a code-only copy of 175 selected files and an isolated masked restore checking hashes, modes and deployment links. A same-volume copy addresses a specific code-recovery task; full disaster recovery requires a broader set of data and storage.

These distinctions let me describe existing work precisely. One unfinished feature is not a verdict on the whole House; one successful test is not a promise that the entire environment cannot fail.

Evidence basis: [B02](../../EVIDENCE.md#b02), [B06](../../EVIDENCE.md#b06), [B07](../../EVIDENCE.md#b07), [B11](../../EVIDENCE.md#b11), [B12](../../EVIDENCE.md#b12), [B13](../../EVIDENCE.md#b13), [B15](../../EVIDENCE.md#b15).


---

# 22. The public layer of the House

I want the project to be understood through its form: purpose, relationships, mathematics, mechanisms and results.

Opening a thought does not mean surrendering every private detail. I want to show the form: how intent becomes work, how memory returns its grounds and how a result can be checked. A reader needs a path to understanding, not someone else’s internal archive.

A public example can be small and still meaningful. If a concrete problem, change and acceptance are visible, a reader has something to examine. At the same time, acceptance of one change speaks to that change, not to an entire system.

I build the House with AI collaborators: they help implement, verify and challenge. I retain purpose, criteria and responsibility for the whole; specific contributions retain their attribution. Codex, OpenClaw, libraries and foundation models have their own origins. My work here is the architecture of their interaction.

There is always a choice of form between an internal intention and a published text. I can explain why a saved note is not an accepted decision without opening private correspondence. I can show a formula and its limits without publishing a map of the entire working environment. The reader receives the thought, not a collection of private details.

## Where to look more closely

- [AI Ontology — public edition](https://github.com/DiadkoShmek/ai-ontology)
- [Evidence-gated Agent Workflows](https://github.com/DiadkoShmek/evidence-gated-agent-workflows)
- [Signal Desk - source-bound research example](https://github.com/DiadkoShmek/talent-research-workflow-prototype)
- [FilesDrop #32 - merged contribution](https://github.com/AndreyBegma/FilesDrop/pull/32)
- [OpenClaw - upstream runtime](https://github.com/openclaw/openclaw)

For private mechanisms, the index identifies the kind of source available; public examples provide separate points that a reader can inspect. This account does not imply full access to the internal infrastructure.

When a conversation ends, the House should leave more than a successful answer: an intelligible continuation. Who carries the work forward? What can they return to? What will change after the next consequence? These questions hold intent, difference, memory and work together.

Evidence basis: [B01](../../EVIDENCE.md#b01), [B10](../../EVIDENCE.md#b10), [B16](../../EVIDENCE.md#b16).


---

# A. Evidence basis I

Chapter codes name the kind of basis and its exact boundary. Detailed private coordinates are retained outside this publication.

Codes B01–B16 identify the source groups for this edition. For private mechanisms they describe the basis of the account without promising access to internal files. The preceding chapter links public examples a reader can inspect independently.

| Code / subject | Basis and boundary |
| --- | --- |
| B01 · Intent and whole-system form | My operational account, direct requirements and owner source maps. Operational duration is my account; the book is not a census of every PC process. |
| B02 · Autonomy and orchestration | Dispatcher/runtime code, leases, native campaign receipts and accepted cooperative repairs. A started round, a completed child and an accepted result are distinct. |
| B03 · Mail and shared state | Exact-byte courier, work reducer, transactions and immutable reader generations. A publication receipt does not mean that the letter’s content was executed. |
| B04 · Pole memory | Inspected scanner/fragmenter/timeline/links, BM25, expansion and gate. Lexical support is not entailment; indexed hashes need current-byte checks. |
| B05 · Training data | Existing JSONL artifacts, exporter, split, deduplication and contamination-check code. Consistent run manifests and semantic quality require their own acceptance. |
| B06 · Neural experiment | NumPy GRU source, a numeric 400-step log, NPZ headers and retained weights. Training-minibatch metrics and a flagged gradient path, not full independent correctness or generalization. |
| B07 · Support plane | Worker/policy/lifecycle/plugin code and an actual seven-route readback on 25 October. A dated route cohort with bounded fixed evaluation sets. |
| B08 · Mathematical studies | CreditWorld, finite coarsening witnesses, manual invariance algebra and exact order enumeration. Manual proof, executed experiment and accepted source constraint remain distinct. |

Evidence basis: [B01](../../EVIDENCE.md#b01), [B02](../../EVIDENCE.md#b02), [B03](../../EVIDENCE.md#b03), [B04](../../EVIDENCE.md#b04), [B05](../../EVIDENCE.md#b05), [B06](../../EVIDENCE.md#b06), [B07](../../EVIDENCE.md#b07), [B08](../../EVIDENCE.md#b08).


---

# B. Evidence basis II

Chapter codes name the kind of basis and its exact boundary. Detailed private coordinates are retained outside this publication.

A boundary closes not the conversation, but a particular claim. It shows where what I can substantiate ends and where a question for future work begins. The unknown remains visible instead of hiding inside a confident sentence.

| Code / subject | Basis and boundary |
| --- | --- |
| B09 · Shadow workbench | Statistical, search and algebraic functions; a retained isolated 55-test receipt. Mathematical/educational implementation, without production cryptographic certification. |
| B10 · AI Ontology | Public pinned commit, book v3.7.0, record model, audit and claim ledger. A proposed profile; record completeness is not general learning. |
| B11 · Continuity and runtime | Current owner/evaluator/spiral/bridge sources; a separate Omnigen target event log and replay. A target and historical PASS do not establish migration of all current organs. |
| B12 · Mirror | Completed LQ3, actual runner and standalone stored reader with source barriers. A negative paper result; controller readiness is not live profit. |
| B13 · Budova | Project save/CAS, staging/recovery, historical fact composition and retained UI/HTTP runs. Controlled local flows; a professional user trial has not yet occurred. |
| B14 · Science conveyor | Immutable packets, validators, attempt-before-spawn and Math23 source-adoption receipt. Bounded source constraints, without automatic model-weight uplift. |
| B15 · Console, recovery and media | UI/backend contracts, code capture/restore, render lineage and retained creative exports. Technical availability and artistic acceptance are separate; restore is code-only/same-volume. |
| B16 · Public work | GitHub API merge readback for FilesDrop #32 and public source-bound examples. A merge establishes acceptance of a specific change. |

Evidence basis: [B09](../../EVIDENCE.md#b09), [B10](../../EVIDENCE.md#b10), [B11](../../EVIDENCE.md#b11), [B12](../../EVIDENCE.md#b12), [B13](../../EVIDENCE.md#b13), [B14](../../EVIDENCE.md#b14), [B15](../../EVIDENCE.md#b15), [B16](../../EVIDENCE.md#b16).


---

