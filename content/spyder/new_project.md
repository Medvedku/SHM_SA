+++
title = "Project"
weight = 1
+++

Once your environment is set up, you can launch and manage the project directly through the Spyder IDE.

### 1. Launching Spyder
Ensure your `shm` environment is active in PowerShell, then launch the program:

```powershell
# Activate if not already active
conda activate shm

# Start the IDE
spyder
```

### 2. Initializing the Project
Spyder uses a "Project" system to manage files, similar to a Workspace in VS Code. To link the repository:

1. In the top menu, go to `Projects` → `New Project...`
2. In the popup window, select `Existing directory`.
3. Browse to and select the path of your cloned repository.
{{< figure src="/SHM_SA/C_spyder/C01.png" link="/SHM_SA/C_spyder/C01.png" width="700" title="Selecting an existing directory in Spyder" >}}
4. Click `Create`.

### 3. Project Interface
After confirmation, a navigation panel appearing as a **Project Tree** will show up on the left side. You can now use **Spyder** as a full-featured editor to manage:
* **Python Scripts** (.py)
* **Documentation** (README.md)
* **Configuration** (.gitignore)

---