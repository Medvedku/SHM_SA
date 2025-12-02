+++
title = "Installation on Windows"
weight = 1
+++

# Recommendation  
## Use Jupyter Inside Visual Studio Code

Although Jupyter Notebook works standalone, we recommend using Jupyter inside **Visual Studio Code** for the best workflow.  
VS Code provides:

- native support for `.ipynb` notebooks  
- enhanced editing and IntelliSense  
- integrated terminal and environment management  
- variable explorer and data viewer  
- improved workflows with DuckDB, Parquet, and MongoDB  

### Install:

- Visual Studio Code — https://code.visualstudio.com  
- Python Extension — https://marketplace.visualstudio.com/items?itemName=ms-python.python  

After installation, open or create any `.ipynb` file directly in VS Code.

---

The following instructions describe how to install and run **Jupyter Notebook standalone**.  
They are provided for completeness or for users who prefer not to use Visual Studio Code.

---

# How to Install on Windows

Jupyter can be installed on Windows using Python and the built-in package manager `pip`.  
It is a practical environment for data exploration, visualization, and SHM/SA workflows.

---

## 1. Install Python

Download and install Python from:  
https://www.python.org/downloads/windows/

During installation, enable:  
✔ **Add Python to PATH**

---

## 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3. Install Jupyter Notebook

```bash
pip install jupyter notebook
```

---

## 4. Start Jupyter Notebook

```bash
jupyter notebook
```

The interface will open in your browser at:

```
http://localhost:8888
```

---

## References

- Jupyter Project — https://jupyter.org  
- Installation Guide — https://jupyter.org/install  
- Python Virtual Environments — https://docs.python.org/3/library/venv.html  

---
