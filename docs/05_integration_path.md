# 05 - Integration path

OEM integration model:

```text
Existing scanner hardware unchanged
  ↓
raw complex multicoil k-space
  ↓
standard preprocessing
  ↓
QSG-MRI quaternionic lift
  ↓
coherence-aware fusion / reconstruction / diagnostics
  ↓
standard reconstructed image + optional coherence/artifact maps
```

Key integration constraints:

- scanner hardware does not need to change
- measured input remains standard complex k-space
- QSG-MRI is a reconstruction and analysis layer
- evaluation can begin offline on stored raw data
- OEM integration can start as a research plugin before any clinical deployment
