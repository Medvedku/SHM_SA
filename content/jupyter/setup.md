+++
title = "New Project Setup"
weight = 2
+++

# New Project Setup

Follow these steps to create and prepare a new Python project inside **Visual Studio Code**.

---

## 1. Open Visual Studio Code

- Launch **Visual Studio Code**
- Open a new window:  
  **File → New Window**  
  or use the shortcut:  
  **Ctrl + Shift + N**

[![thumb](https://picsum.photos/200/120)](https://picsum.photos/1200/800)



---

## 2. Open Your Project Folder

Inside the new VS Code window:

- Go to **File → Open Folder**
- Select a **new empty project folder** or an existing **GitHub repository folder**

---

## 3. Open a Terminal

Open an integrated terminal:

- **Terminal → New Terminal**  
  or shortcut: **Ctrl + Shift + `**  
  (backtick key is usually above Tab)

---

## 4. Create a New Virtual Environment

A virtual environment keeps your project’s Python packages isolated and organized.  
You may name the environment *anything you like*—the examples below use `SA_VENV` on both Ubuntu and Windows.

{{< tabs >}}

{{% tab "Ubuntu" %}}
### Create and Activate Virtual Environment (Ubuntu / Linux)

```bash
python3 -m venv SA_VENV
```
{{% /tab %}}

{{% tab "Windows" %}}
### Create and Activate Virtual Environment (Windows)

```bash
python -m venv SA_VENV
```
{{% /tab %}}

{{< /tabs >}}


[{{< figure src="https://rubint.sk/data/imgs/scrnshts/A_1.png" width="300" >}}](https://rubint.sk/data/imgs/scrnshts/A_1.png)

---

## 5. Activation of a Created Virtual Environment

After creating a virtual environment (in this example named `SA_VENV`), you can activate it using the commands below.  

> **Note:** If you plan to work *exclusively inside Jupyter Notebook*, activating the environment in the terminal is not required.  
> The notebook will use the correct environment **once its kernel is registered and selected**.

{{< tabs >}}

{{% tab "Ubuntu" %}}
### Activate Virtual Environment (Ubuntu / Linux)

```bash
source SA_VENV/bin/activate
```
{{% /tab %}}

{{% tab "Windows" %}}
### Activate Virtual Environment (Windows)

```bash
SA_VENV\Scripts\activate
```
{{% /tab %}}

{{< /tabs >}}

[{{< figure src="https://rubint.sk/data/imgs/scrnshts/A_10.png" width="300" >}}](https://rubint.sk/data/imgs/scrnshts/A_10.png)


---

## 6. Installing Packages

Packages can be installed in two ways:  
1. **In the terminal** (after activating your virtual environment)  
2. **Inside a Jupyter Notebook cell** using the `!` prefix  
   - *Note: Be sure the correct kernel (your virtual environment) is selected in Jupyter.*

{{< tabs >}}

{{% tab "Terminal" %}}
### Installing Packages in the Terminal

Ensure your virtual environment is activated, then run:

```bash
pip install <package-name>
```

**Example:**

```bash
pip install numpy pandas matplotlib
```
{{% /tab %}}

{{% tab "Jupyter Notebook" %}}
### Installing Packages Inside a Jupyter Notebook Cell

Use the `!` prefix to execute installation commands:

```python
!pip install <package-name>
```

**Example:**

```python
!pip install numpy pandas matplotlib
```

> **Tip:** Packages install into the environment used by the currently selected notebook kernel.
{{% /tab %}}

{{< /tabs >}}

---
---

