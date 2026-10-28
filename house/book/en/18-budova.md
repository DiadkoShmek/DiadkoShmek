# 18. Budova: exact revisions for physical work

My domain experience gives the product a concrete reader: a foreman or crew lead needs to know exactly what was handed over and on what basis.

![An issued package and a returned fact remain attached to their revision even after the current head advances.](../../assets/diagrams/budova-en.svg)

*An issued package and a returned fact remain attached to their revision even after the current head advances.*

Sources, part geometry and issued packages have distinct immutable bindings. The model contains exact outlines and holes, units, DXF/maps and original CAD sources. A new measurement does not rewrite a package already handed over.

Project saves use transactional CAS. Exact request replay is checked before a revision conflict. Background export passes through staging, a recovery record, fsync and rename. A historical fact passes preview and CAS before being appended to its own revision. Old cumulative progress must not become a fresh increment merely because a request was retried.

Local UI/HTTP flows already issued a package with 18 members and two CAD originals, and served the same frozen ZIP after controlled loss of a live source. A professional user trial and the latest served-origin acceptance of the montage reader remain specific boundaries of this product.

Evidence basis: [B13](../../EVIDENCE.md#b13).

← [Previous](17-mirror.md) | [Next](19-science.md) →
