# 06 - Software package

Python package name: `qsg_mri`

Package goals:

- Provide auditable, minimal primitives for quaternionic MRI research software.
- Preserve complex-data compatibility and baseline reconstruction behavior.
- Support controlled simulation and hypothesis testing.

Current module map:

- `quaternion.py`: core quaternion array operations and fixed-axis helpers
- `kspace.py`: spatial-frequency utilities and centered grid helpers
- `coil_state.py`: coil-state construction and channel packing
- `coherence.py`: coherence score and defect
- `reconstruction.py`: baseline + placeholder QCSM fusion
- `baselines.py`: standard reconstruction helpers
- `phantoms.py`: synthetic phantom and sensitivity generation
- `metrics.py`: evaluation metrics

Implementation status is intentionally conservative: this is not production-grade
clinical reconstruction software.
