+++
title = "Installation on Ubuntu"
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

# How to Install on Ubuntu

Jupyter can be installed on Ubuntu using Python, `pip`, and optional virtual environments.  
It is a reliable environment for data exploration, visualization, and SHM/SA workflows.

---

## 1. Update System Packages

```bash
sudo apt update && sudo apt upgrade -y
```

---

## 2. Install Python and pip

Ubuntu typically includes Python, but you can ensure everything is installed with:

```bash
sudo apt install -y python3 python3-pip python3-venv
```

---

## 3. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4. Install Jupyter Notebook

```bash
pip install jupyter notebook
```

---

## 5. Start Jupyter Notebook

```bash
jupyter notebook
```

The interface will open in your browser at:

```
http://localhost:8888
```

If running on a remote server, you may need:

```bash
jupyter notebook --ip 0.0.0.0 --no-browser
```

---

## References

- Jupyter Project — https://jupyter.org  
- Installation Guide — https://jupyter.org/install  
- Python Virtual Environments — https://docs.python.org/3/library/venv.html  

---
