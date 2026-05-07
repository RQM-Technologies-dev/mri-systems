# Theory

MRI measurement pipelines are complex-valued by default, but reconstruction quality is strongly influenced by coupled effects across phase, coil geometry, and motion/orientation drift.

Quaternionic states provide a compact way to represent these coupled components:

- Complex coil signal: `z_c = a_c + i b_c`
- Quaternionic state: `q = w + x i + y j + z k`

This repository treats quaternionic modeling as a geometric representation upgrade, not a claim of automatic quality improvement.
