+++
title = "Datasets"
weight = 3
+++

# Datasets

This section describes how the SHM datasets are structured, how they are produced from the monthly raw JSON exports, and how to build a downloader script capable of detecting and retrieving only the missing parts of the dataset from the cloud storage (R2 bucket).

---

## 1. Overview of the Data Pipeline

Every month, a large JSON export (~3 GB) is generated from MongoDB.  
This JSON contains all SHM measurements collected from 4 hubs, covering two periodicities:

- **1 Hz** — high-frequency acceleration time series  
- **1/60 Hz** — low-frequency strains, temperatures, and FFT results derived from accelerations  

Each monthly JSON file is processed and converted into **9 structured Parquet tables**, enabling efficient downstream analysis using DuckDB.

---

## 2. Parquet Dataset Structure

The dataset is organized into nine Parquet tables:

### 1 Hz Data
- **1 table**: Acceleration measurements (all hubs combined)  
  - Path example: `parquet/1hz/acceleration_<YYYY-MM>.parquet`

### 1/60 Hz Data
- **4 tables**: FFTs per hub  
  - Example paths:  
    - `parquet/1_60hz/fft_hub1_<YYYY-MM>.parquet`  
    - `parquet/1_60hz/fft_hub2_<YYYY-MM>.parquet`  
    - …  

- **4 tables**: Strains + temperatures per hub  
  - Example paths:  
    - `parquet/1_60hz/strain_temp_hub1_<YYYY-MM>.parquet`  
    - `parquet/1_60hz/strain_temp_hub2_<YYYY-MM>.parquet`  
    - …  

This structure allows the analysis workflow (usually executed in DuckDB) to efficiently query exactly the tables needed.

---

## 3. Monthly Data Update Workflow

Each month:

1. A new ~3 GB JSON dump is exported from MongoDB.  
2. The JSON is processed and split into the **nine Parquet tables** listed above.  
3. The new Parquet files are uploaded into the **R2 bucket**, maintaining a consistent folder and file naming structure.  
4. Analysts run their DuckDB-based pipelines using the updated dataset.

---

## 4. Automatic Dataset Downloader (Planned Section)

This section will provide a step-by-step guide for creating a **downloader script** that:

1. Connects to the R2 bucket containing the Parquet files  
2. Compares the remote file list with the local datasets  
3. Detects which monthly Parquet files are missing  
4. Downloads only the missing parts to avoid redundant data transfer  
5. Reports the dataset status (e.g., “Up to date”, “3 files missing”, etc.)

The downloader will typically be run **once per month**, right after new data has been uploaded.

This ensures every local analysis environment has an up-to-date and complete Parquet dataset without requiring full re-downloads.

---

## 5. Goals of This Section

In the following subsections, we will cover:

- Dataset folder structure  
- Naming conventions for monthly Parquet files  
- How to list objects in an R2 bucket (using S3-compatible API)  
- How to compare remote vs. local dataset states  
- How to build an incremental downloader script  
- Example implementation in Python (with optional DuckDB checks)  

These components will provide a reliable foundation for maintaining synchronized local datasets for SHM analytics.

---
