+++
date = '2025-11-27T16:19:36+01:00'
draft = false
title = "SHM Swag Analysis up 18:25"
+++

# Welcome to the SHM Sound Analysis Project

This website provides clear documentation and tutorials for working with data from our **Structural Health Monitoring (SHM)** system.  
It is designed for students, researchers, and collaborators who want a practical, step-by-step guide for accessing, processing, and analyzing the collected sensor data.

## What You Will Find Here

### 📡 Understanding the SHM System
A high-level overview of the SHM setup, the sensors involved, and the purpose of the monitoring project.

### 🗄️ Working With MongoDB
Our raw data is originally collected and stored in **MongoDB**.  
This section explains:
- how the monthly data is structured,  
- how to export data from MongoDB, and  
- how to run useful queries for inspection.

### 🦆 Converting Data to DuckDB / Parquet
For efficient analysis, the MongoDB exports are converted into **Parquet** files and loaded into **DuckDB**.  
You will find instructions on:
- converting monthly datasets,  
- understanding the resulting Parquet structure,  
- querying data using DuckDB.

### 🗂️ Dataset Overview
Each month contains nine Parquet files representing different signal components and metadata.  
This documentation explains:
- how each file is structured,  
- how the monthly data fits together,  
- where to download the datasets (via Cloudflare R2).

### 📊 Examples and Analysis
Practical examples showing how to:
- visualize vibration signals,  
- generate spectrograms,  
- perform basic exploratory analyses.

## How To Use This Documentation
Use the **sidebar** to navigate through sections.  
Start with *Introduction* if you are new to the project, or jump directly to *Setup*, *MongoDB*, or *DuckDB* depending on your needs.

This site will grow as the project continues and new monthly datasets are collected.
