+++
title = "Project Environment"
weight = 2
+++

Why use a separate environment for this project?

- Isolation: keeps project packages separate from system Python, avoiding version conflicts.
- Reproducibility: pinning dependencies (requirements.txt) ensures results can be reproduced later.
- Safety: experiments and installs won't break other projects or global tools.
- Portability: sharing a requirements file or environment makes it easy for others to run the same code.

For this Parquet showcase, a dedicated environment keeps `pandas` and `pyarrow` at compatible versions so data loading and analysis work predictably.