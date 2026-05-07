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

## Metrics interpretation guardrails

- `run_completed: true` means the script executed and emitted its expected
  output artifacts.
- `synthetic_only: true` indicates controlled synthetic data was used.
- `clinical_result: false` indicates no clinical performance claim is being made.
- `result_scope: "synthetic_controlled_engineering_run"` marks the output as
  engineering-only evidence.
- `target_achieved: true` should only be used when measured outputs explicitly
  demonstrate a predeclared target was met.

## What counts as promising

- Measurable improvement in target metric
- Useful coherence/artifact diagnostics
- No loss of compatibility with complex data
- Reasonable runtime
- Stable, reproducible outputs

## What does not count

- Visual improvement without metric support
- Synthetic-only success framed as clinical proof
- A completed run (`run_completed`) framed as target attainment
- Unrepeatable output
- Unsupported claims

## Recommended OEM next step

Run offline replay against a small deidentified multicoil dataset and compare
against the OEM's existing reconstruction baseline.
