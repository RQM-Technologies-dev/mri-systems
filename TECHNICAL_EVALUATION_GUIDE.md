# Technical Evaluation Guide

## Purpose

This guide explains how an MRI OEM engineering team can evaluate MRI-systems
without adopting it into a scanner product.

## Evaluation assumptions

- Software-only
- Offline first
- Complex k-space remains input
- Existing reconstruction remains baseline
- Synthetic tests precede deidentified-data tests

## Minimum evaluation workflow

1. Install package.
2. Run unit tests.
3. Run phantom baseline simulation.
4. Run multicoil fusion simulation.
5. Inspect `metrics.json`.
6. Inspect coherence-defect map.
7. Compare against baseline.
8. Decide whether to test internal deidentified data.

## What counts as promising

- Measurable improvement in target metric
- Useful coherence/artifact diagnostics
- No loss of compatibility with complex data
- Reasonable runtime
- Stable, reproducible outputs

## What does not count

- Visual improvement without metric support
- Synthetic-only success framed as clinical proof
- Unrepeatable output
- Unsupported claims

## Recommended OEM next step

Run offline replay against a small deidentified multicoil dataset and compare
against the OEM's existing reconstruction baseline.
