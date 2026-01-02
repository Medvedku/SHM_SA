+++
title = "Inspector"
weight = 2
+++


## Project Setup

Before running any analysis, you need to create the script file within your environment.
1. In **Spyder**, right-click anywhere within the Project Tree.
2. Select `New` -> `Python file...`.
3. Select module name and click `OK` to confirm. {{< figure src="/SHM_SA/C_spyder/C02.png" link="/SHM_SA/C_spyder/C02.png" width="700">}}
4. At the very top of your file, ensure the encoding and header are set:
```python
# -*- coding: utf-8 -*-
"""
SHM Data Inspector
"""
```
---
### `Cell [0]`: Initializing the Engine
The first step is to load our "Toolkit." We use `pathlib` for navigating Windows folders, `DuckDB` for lightning-fast data processing, and `Matplotlib` for plotting inside the Spyder interface.
```python
#%% [0] Imports
import pathlib
import pandas as pd
import duckdb
import matplotlib.pyplot as plt

print("Libraries loaded. Ready to inspect.")
```
> **Note:** Once you run this cell, the libraries stay loaded in your current session. You only need to run this again if you restart Spyder.
---

### `Cell [1]`: Data Inventory & Indexing
This cell scans your `parquets/` directory and generates a "Catalog" of your data. It looks for subfolders and counts exactly how many Parquet files are inside each.

```python
#%% [1] List available data folders and file counts
# Define the path to parquets
parquet_path = pathlib.Path("parquets")

# Formatting the output table
print(f"{'Index':<7} | {'Folder Name':<25} | {'Files':<8}")
print("-" * 45)

# Scans directories and counts files
folders = [f for f in parquet_path.iterdir() if f.is_dir()]

for index, folder in enumerate(folders):
    # Count only files ending in .parquet
    file_count = len(list(folder.glob("*.parquet")))
    print(f"[{index:<3}] | {folder.name:<25} | {file_count:<8}")
```
> **How to use it:** Look at the generated table in your console. Note the Index (e.g., `5`) of the folder you want to inspect. You will enter this index number in the next step to select your target data.
---

### `Cell [2]`: Global Statistical Health Check
This is where the heavy lifting happens. Instead of loading files one by one, `DuckDB` treats all files in your selected folder as a single, massive table.

This cell provides:
* **Total Volume:** A count of every single measurement across the entire history of that hub.
* **Time Window:** The exact dates the sensors were active.
* **Sensor Range:** A summary of the Min, Max, and Average values for every sensor.

```python
#%% [2] Inspect Whole Table (All 75 files combined)
selection = 5 # Index for sst_hub1

if selection < len(folders):
    target_folder = folders[selection]
    parquet_pattern = (target_folder / "*.parquet").as_posix()
    
    print(f"Generating Global Statistics for: {target_folder.name}")
    print("Please wait, scanning all 75 files...")
    print("-" * 60)
    
    # 1. Use DuckDB to calculate stats for the entire dataset at once
    # We exclude 'datetime' and 'filename' from numeric stats
    summary_query = duckdb.query(f"""
        SELECT 
            column_name,
            column_type
        FROM (DESCRIBE SELECT * FROM '{parquet_pattern}')
    """).to_df()
    
    # Filter for numeric columns only to get Mean/Min/Max
    numeric_cols = summary_query[summary_query['column_type'].str.contains('DOUBLE|FLOAT|INT|DECIMAL')]['column_name'].tolist()
    
    # Construct a query to get stats for all numeric sensors
    stats_list = [f"mean({c}) as {c}_avg, min({c}) as {c}_min, max({c}) as {c}_max" for c in numeric_cols]
    stats_sql = ", ".join(stats_list)
    
    global_stats = duckdb.query(f"""
        SELECT 
            count(*) as total_records,
            min(datetime) as global_start,
            max(datetime) as global_end,
            {stats_sql}
        FROM '{parquet_pattern}'
    """).to_df()
    
    print(f"Total Combined Rows: {global_stats['total_records'][0]:,}")
    print(f"Time Span: {global_stats['global_start'][0]} to {global_stats['global_end'][0]}")
    print("\nSensor Statistics (Global):")
    
    # Reshape the data for a cleaner display
    display_stats = []
    for c in numeric_cols:
        display_stats.append({
            'Sensor': c,
            'Average': global_stats[f'{c}_avg'][0],
            'Min': global_stats[f'{c}_min'][0],
            'Max': global_stats[f'{c}_max'][0]
        })
    
    print(pd.DataFrame(display_stats).to_string(index=False))

else:
    print("Invalid selection!")
```
> **Note:** Suspicious values appeared as maximum values in columns for sensors T4 and T6. In both cases, the value {{< katex >}}85.000 °C{{< /katex >}} appeared. 
> 1. It is statistically odd that the value is a perfect integer.
> 2. This value is physically improbable for an indoor measurement, suggesting an error.
---

### `Cell [3]`: Forensic Anomaly Scan
If the previous step flagged suspicious values, this cell performs a deep-dive "Forensic Scan." It counts exactly how many times these errors occurred and checks if they happened on multiple sensors simultaneously.

```python
#%% [3] Numeric Investigation of Temperature Suspects (85.0)

target_val = 85.0

print(f"Deep Scan: Investigating {target_val} error values...")
print("-" * 60)

# 1. Detailed breakdown using DuckDB
# We check T4 and T6 counts, and importantly, how many times BOTH failed at once
investigation = duckdb.query(f"""
    SELECT 
        count(*) FILTER (WHERE T4 = {target_val}) as T4_only_errors,
        count(*) FILTER (WHERE T6 = {target_val}) as T6_only_errors,
        count(*) FILTER (WHERE T4 = {target_val} AND T6 = {target_val}) as Both_failed,
        min(datetime) FILTER (WHERE T4 = {target_val} OR T6 = {target_val}) as first_error,
        max(datetime) FILTER (WHERE T4 = {target_val} OR T6 = {target_val}) as last_error
    FROM '{parquet_pattern}'
""").to_df()

t4_total = investigation['T4_only_errors'][0]
t6_total = investigation['T6_only_errors'][0]
both = investigation['Both_failed'][0]

print(f"Occurrence Report:")
print(f"  - T4 error count: {t4_total:,}")
print(f"  - T6 error count: {t6_total:,}")
print(f"  - Simultaneous failures (Both): {both:,}")
print("-" * 45)

if t4_total > 0 or t6_total > 0:
    print(f"Timeline of issues:")
    print(f"  - First detected: {investigation['first_error'][0]}")
    print(f"  - Last detected:  {investigation['last_error'][0]}")
    
    # Let's find the longest continuous "flatline" of 85.0 
    # This helps see if the sensor was dead for a long time
    print("\nSample of most recent error timestamps:")
    recent_errors = duckdb.query(f"""
        SELECT datetime, T4, T6 
        FROM '{parquet_pattern}' 
        WHERE T4 = {target_val} OR T6 = {target_val}
        ORDER BY datetime DESC
        LIMIT 10
    """).to_df()
    print(recent_errors)
else:
    print("No instances of 85.0 found in this folder.")
```
> **Output:** This cell executes a conditional filtering operation to isolate and quantify erroneous {{< katex >}}85.000 °C{{< /katex >}} data points, providing a diagnostic summary of measurement frequency and temporal distribution.
---

### `Cell [4]`: Visualizing the "Glitch"
To be 100% sure of what is happening, we generate a series of "Zoom Plots." For every error detected, the script creates a dedicated chart showing the 30 minutes before and after the event.


```python
#%% [4] Individual Forensic Plots (85.0 spikes)


# 1. Get the list of timestamps where errors occurred
error_timestamps = duckdb.query(f"""
    SELECT datetime 
    FROM '{parquet_pattern}' 
    WHERE T4 = 85.0 OR T6 = 85.0
    ORDER BY datetime
""").to_df()['datetime']

print(f"Generating {len(error_timestamps)} detailed plots...")

# 2. Iterate and create a unique plot for each event
for i, ts in enumerate(error_timestamps):
    # Fetch 30 mins before and after
    window_df = duckdb.query(f"""
        SELECT datetime, T4, T6 
        FROM '{parquet_pattern}' 
        WHERE datetime BETWEEN '{ts}'::timestamp - INTERVAL '30 minutes' 
                          AND '{ts}'::timestamp + INTERVAL '30 minutes'
        ORDER BY datetime
    """).to_df()
    
    # Create a new figure for every event
    plt.figure(figsize=(12, 5))
    
    # Plot both sensors
    plt.plot(window_df['datetime'], window_df['T4'], label='T4', color='#1f77b4', linewidth=1.5)
    plt.plot(window_df['datetime'], window_df['T6'], label='T6', color='#2ca02c', linewidth=1.5)
    
    # Mark the error point
    plt.axvline(ts, color='red', linestyle='--', alpha=0.6, label=f'Error at {ts.strftime("%H:%M:%S")}')
    
    # Styling
    plt.title(f"Event {i+1} Investigation: {ts.strftime('%Y-%m-%d %H:%M:%S')}", fontsize=14)
    plt.xlabel("Time (30 min window)")
    plt.ylabel("Temperature (°C)")
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(loc='upper right')
    
    # This forces the creation of a new plot entry in Spyder
    plt.tight_layout()
    plt.show()

print("All plots generated. You can scroll through them in the 'Plots' tab.")
```
> **Using the Plots Pane**: All 8 plots will appear in Spyder's **Plots** tab. You can scroll through them to see the signal behavior. Typically, you will see a steady temperature line followed by a vertical "spike" to {{< katex >}}85.000 °C{{< /katex >}} and an immediate return to normal. This confirms the value is a singular wrong measurement rather than a physical heating event.

---