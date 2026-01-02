+++
title = "Commit changes"
weight = 3
+++

Since we have modified the project by creating the `Inspector.py` file, we should record these changes. We will use **GitHub Desktop** to manage our version history, allowing us to decide whether to push changes to GitHub or keep them stored locally.

---

### 1. Identify Changes
Open **GitHub Desktop**. The application automatically detects that a new file, `Inspector.py`, has been added to your project folder. You will see it listed in the **Changes** tab on the left sidebar with a green "+" icon.



### 2. Crafting the Commit
At the bottom of the left panel, you will find the "Summary" and "Description" fields. 

* **Summary (Required):** Enter a short, descriptive title like `Add SHM Data Inspector script`.
* **Description (Optional):** You can add more detail, such as "Added DuckDB integration and forensic plotting for temperature spikes."

Click the **Commit to main** (or your current branch) button. This "saves" the snapshot to your local database.

### 3. Syncing with GitHub (Optional)
After committing, the change is saved on your computer but not yet on the cloud. 

* **To Push:** Click the **Push origin** button at the top of the window to upload your local commits to the GitHub repository.
* **To Keep Local:** Simply do nothing further. Your changes are safely recorded in your local Git history, but won't be visible to others on GitHub.



> **Note:** Committing regularly is a best practice. It creates "save points" you can return to if your code stops working during future experiments.