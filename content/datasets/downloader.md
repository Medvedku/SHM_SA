+++
title = "Script – Downloader"
weight = 2
+++

# Downloader Script

This section introduces the downloader script that will automatically fetch newly uploaded Parquet files from the R2 bucket.  
It ensures your local dataset stays synchronized with the cloud dataset without manually checking which files are missing.

---

## 1. Create a Download Folder

Before writing the script, choose where the downloaded Parquet files will be stored.

You can place the folder *anywhere* on your system, but the most common setup is:


```bash
project/
│
├── SA_VENV/               # virtual environment (optional)
├── downloads/             ← recommended location
├── src/                   # downloader / analysis scripts
├── .env                   # environment variables (secret)
└── .gitignore             # must include ".env"
```

If the **`downloads/`** folder is inside your project directory, it is highly recommended to add it to your `.gitignore` so it is not committed to Git:

```
SA_VENV/
downloads/
```

---

## 2. Create the Downloader Notebook

Create a new Jupyter Notebook, for example:

```
src/00_downloader.ipynb
```

Inside this notebook we will:

- Load environmental variables from the `.env` file  
- Connect to the R2 bucket  
- Compare local files with remote files  
- Download only the missing Parquet files  
- Log or print status information (e.g. “Up-to-date”, “3 new files downloaded”, etc.)

---

## 3. Define the Download Path

At the beginning of the notebook, define the path where files will be saved.  
Adjust this path depending on where you created your folder:

```python
import pathlib

# Path to the directory where Parquet files will be downloaded
DOWNLOAD_DIR = pathlib.Path("../downloads")  

# Create folder if it does not exist
DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)

# DOWNLOAD_DIR  # Uncomment to see the download directory path
```

This ensures the script works even if the folder doesn’t exist yet.

[{{< figure src="https://rubint.sk/data/imgs/scrnshts/A_13.png" width="300" >}}](https://rubint.sk/data/imgs/scrnshts/A_13.png)

---

## 4. Load Environment Variables and Initialize the R2 Client

In this step, we load the credentials stored inside the `.env` file (access key, secret key, endpoint, and bucket name).  
These values are required to authenticate with Cloudflare R2 using its S3-compatible API.

We use:

- `python-dotenv` — to load variables from the `.env` file  
- `boto3` — Amazon’s S3 client library, which Cloudflare R2 supports fully

If all variables are loaded correctly, the script initializes an R2 client instance.  
This client object will be used for listing folders, checking files, and downloading missing Parquet files.


```python
import os
from dotenv import load_dotenv
import boto3

# Load environment variables from .env
load_dotenv()

R2_ACCESS_KEY_ID     = os.getenv("R2_ACCESS_KEY_ID")
R2_SECRET_ACCESS_KEY = os.getenv("R2_SECRET_ACCESS_KEY")
R2_ENDPOINT_URL      = os.getenv("R2_ENDPOINT_URL")
R2_BUCKET            = os.getenv("R2_BUCKET")

# Initialize S3 client for Cloudflare R2
s3 = boto3.client(
    "s3",
    aws_access_key_id=R2_ACCESS_KEY_ID,
    aws_secret_access_key=R2_SECRET_ACCESS_KEY,
    endpoint_url=R2_ENDPOINT_URL,
)

# R2_BUCKET # Uncomment to see the bucket name
```

---
## 5. Helper Functions for Reading the R2 Bucket Structure

Cloudflare R2 organizes objects using **prefixes** (folder-like paths).  
To synchronize local data with the cloud dataset, the script first needs to understand how the bucket is structured.

The helper functions below handle that:

### What these helpers do

- `list_r2_folders()`  
  Retrieves all top-level folder names inside the bucket (e.g., `"1hz/"`, `"fft_hub1/"`, etc.).

- `list_r2_files(prefix)`  
  Lists **all** files inside a given folder, handling pagination automatically so it works even with hundreds or thousands of Parquet files.

These reusable helpers allow the downloader to adapt dynamically to the bucket’s structure, without requiring any hardcoded folder names.


```python
# === Helper: List folders (prefixes) in R2 ===
def list_r2_folders(bucket: str):
    response = s3.list_objects_v2(
        Bucket=bucket,
        Delimiter="/"   # groups by folders
    )
    
    prefixes = response.get("CommonPrefixes", [])
    folders = [p["Prefix"].rstrip("/") for p in prefixes]
    return folders

# === Helper: List files inside an R2 folder ===
def list_r2_files(prefix: str):
    file_list = []
    continuation_token = None

    while True:
        params = {"Bucket": R2_BUCKET, "Prefix": prefix}
        if continuation_token:
            params["ContinuationToken"] = continuation_token
        
        resp = s3.list_objects_v2(**params)
        contents = resp.get("Contents", [])

        for obj in contents:
            key = obj["Key"]
            if not key.endswith("/"):
                file_list.append(key.split("/")[-1])

        if resp.get("IsTruncated"):
            continuation_token = resp["NextContinuationToken"]
        else:
            break

    return file_list

# === Load folder list from bucket ===
folders = list_r2_folders(R2_BUCKET)

#print("Folders in bucket:\n" + "\n".join(f" - {f}" for f in folders)) # Uncomment to see the folder list
```

---
## 6. Compare R2 Files with Local Files (Auto-Sync Check)

Before downloading anything, the script checks what already exists locally.

For every folder found in R2:

1. A matching local folder is created (if missing).  
2. Local `.parquet` files in that folder are listed.  
3. Remote `.parquet` files in the same folder are listed.  
4. Missing files are detected using a set comparison.  
5. A dictionary called `sync_plan` is populated with:

```
folder_name → [list_of_missing_files]
```

This step acts as a **dry-run synchronization preview**.  
It prints a clear, human-readable summary of how many files exist locally, how many are in the bucket, and which ones need to be downloaded.


```python
from pathlib import Path

print("=== AUTO-SYNC CHECK STARTED ===\n")

sync_plan = {}  # folder → list of missing files

# Loop through all folders in the bucket
for selected_folder in folders:

    print(f"\n--- Checking folder: {selected_folder} ---")

    # Create local folder if missing
    local_folder = DOWNLOAD_DIR / selected_folder
    local_folder.mkdir(parents=True, exist_ok=True)

    # --- LIST R2 FILES ---
    r2_files = list_r2_files(selected_folder + "/")

    # --- LIST LOCAL FILES ---
    local_files = {f.name for f in local_folder.glob("*.parquet")}

    # --- FIND MISSING ---
    missing_files = sorted(list(set(r2_files) - local_files))

    # Save plan
    sync_plan[selected_folder] = missing_files

    # Summary output
    print(f"Local files : {len(local_files)}")
    print(f"R2 files    : {len(r2_files)}")
    print(f"Missing     : {len(missing_files)}")
    if missing_files:
        print(" Missing files:")
        for f in missing_files:
            print("  -", f)

print("\n=== AUTO-SYNC CHECK COMPLETE ===")

#sync_plan  # Uncomment to see the sync plan
```

---
## 7. Download Missing Files from R2

Once the synchronization plan is ready, the script begins downloading any missing files.

For each missing Parquet file:

- It generates the correct R2 key (`folder/filename`)  
- Streams the file directly from R2 using `download_fileobj`  
- Saves it into the appropriate local folder  
- Performs a **size validation** step:

  - Retrieves the remote file size using `head_object`
  - Compares it to the size of the downloaded file  
  - Reports **OK** if the sizes match  
  - Prints a **SIZE MISMATCH** warning if not

When all folders have been processed, your local dataset is fully synchronized with the R2 bucket.


```python
from pathlib import Path

print("=== DOWNLOAD STARTED ===\n")

# Loop through each folder and its missing files
for folder, files in sync_plan.items():

    if not files:
        print(f"No missing files for folder: {folder}")
        continue

    print(f"\n--- Downloading folder: {folder} ---")
    local_folder = DOWNLOAD_DIR / folder

    for fname in files:
        r2_key = f"{folder}/{fname}"
        local_path = local_folder / fname

        print(f"Downloading {r2_key} ... ", end="")

        # Stream download from R2
        with open(local_path, "wb") as f:
            s3.download_fileobj(R2_BUCKET, r2_key, f)

        # Validate size
        head = s3.head_object(Bucket=R2_BUCKET, Key=r2_key)
        r2_size = head["ContentLength"]
        local_size = local_path.stat().st_size

        if r2_size == local_size:
            print("OK")
        else:
            print("SIZE MISMATCH ❌")
            print(f"  R2 size   : {r2_size}")
            print(f"  Local size: {local_size}")

print("\n=== DOWNLOAD COMPLETE ===")

```

---
After a successful synchronization between the cloud bucket and your local dataset,  
all newly detected Parquet files will appear inside their corresponding folders.  
This provides a clear visual confirmation that the downloader has updated your local database.

[{{< figure src="https://rubint.sk/data/imgs/scrnshts/A_14.png" width="300" >}}](https://rubint.sk/data/imgs/scrnshts/A_14.png)

---

These steps together form a complete, incremental cloud-to-local dataset sync workflow.  
You only need to run the downloader once per month after uploading new Parquet files.
