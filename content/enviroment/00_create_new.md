+++
title = "New Environment"
weight = 1
+++

To keep the project dependencies isolated and ensure compatibility, we use a dedicated Conda environment.

### 1. Initialize Conda (PowerShell)
If the `conda` command is not recognized in your terminal, run the following "hook" to initialize the session. 

> **Note:** Replace `{USER}`. If you installed Miniconda in a **custom location** (e.g., on a different drive), ensure the path above points to your actual `Scripts\conda.exe` file.

```powershell
& "C:\Users\{USER}\miniconda3\Scripts\conda.exe" "shell.powershell" "hook" | Out-String | Invoke-Expression
```

### 2. Creating the 'shm' Environment
Run the command below to create the environment. During this process, you will be asked to accept the **Terms of Service** (type `a` for accept) and confirm the Package Plan (type `y` for yes).

```powershell
conda create -n shm python=3.10
```

### 3. Activation
You will know the environment is active when (`shm`) appears at the start of your command line.

```powershell
# Activate the environment
conda activate shm

# Deactivate when finished
conda deactivate
```

---