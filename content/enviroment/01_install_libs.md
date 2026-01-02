+++
title = "Installing Libraries"
weight = 2
+++

Once the environment is activated, we need to install the tools for data analysis and visualization. 

### 1. Core Research Stack
We will install the following libraries to handle large-scale data and signal processing:

* **Spyder:** The primary development environment.
* **DuckDB:** For high-performance analytical queries on Parquet files.
* **Plotly:** For interactive data visualization.
* **SciPy:** For signal processing and scientific computing.
* **Pandas & PyArrow:** For data frame manipulation and Parquet support.

### 2. Installation Command
Ensure your terminal shows `(shm)` before running the following:

```powershell
conda install spyder pandas duckdb matplotlib scipy pyarrow fastparquet -c conda-forge
```
> **Note:** We use the `-c conda-forge` channel to ensure we get the most up-to-date versions of these libraries. The installation may take several minutes as it resolves dependencies for the Spyder IDE.

### 3. Verification
To verify the installation and launch the development environment, simply type:

```powershell
spyder
```

---