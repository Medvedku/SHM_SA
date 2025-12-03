+++
title = "Environmental Variables"
weight = 1
+++

# Environmental Variables

When working with cloud storage, APIs, or databases, it is considered good practice **not to hard-code credentials** directly into scripts.  
Instead, sensitive values (API keys, endpoints, bucket names, tokens, etc.) should be stored in a dedicated file called **`.env`**.  
This file contains key–value pairs that your application can load at runtime, keeping credentials out of source code and version control.

---

## Example `.env` File

Below is an example of how your `.env` file may look.  
Only the bucket name is real — **you must replace the access key, secret key, and endpoint with your own values**.

```env
R2_ACCESS_KEY_ID=a9f3d7b4c2e8f1a6b0d4c7e3f9a2b6d1

R2_SECRET_ACCESS_KEY=a1c9e3b7f5d2c4a8e6f0b3d1c7a9f2e4b6d8c0f3a5e7b2d4c6f1a8b0d3c5e9f7a2

R2_ENDPOINT_URL=https://b7e2d9c4f1a3e8c6d0b4f2a7c3e9d1f5.r2.cloudflarestorage.com

R2_BUCKET=shm-parquets
```

> **Important:**  
> Never commit `.env` files into GitHub or any version control system.  
> Add `.env` to your `.gitignore`.

---

## Loading `.env` Inside Jupyter Notebook


Before loading environment variables, ensure that the required Python packages (such as `python-dotenv`) are installed.  
If you need help installing packages inside Jupyter or the terminal, refer to **[6. Installing Packages](/SHM_SA/jupyter/setup/#6-installing-packages)**.

To load variables from your `.env` file inside a Jupyter Notebook, first install the `python-dotenv` library:



```bash
pip install python-dotenv
```

Now create a cell in your notebook:

```python
from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Example usage:
access_key = os.getenv("R2_ACCESS_KEY_ID")
secret_key = os.getenv("R2_SECRET_ACCESS_KEY")
endpoint   = os.getenv("R2_ENDPOINT_URL")
bucket     = os.getenv("R2_BUCKET")

print("Bucket:", bucket)
```

The variables are now available for any code that needs to connect to your R2 bucket or API.

[{{< figure src="https://rubint.sk/data/imgs/scrnshts/A_12.png" width="300" >}}](https://rubint.sk/data/imgs/scrnshts/A_12.png)

---

## Example of Project Structure

```bash
project/
│
├── SA_VENV/               # virtual environment (optional)
├── downloads/             # folder for database
├── src/                   # downloader / analysis scripts
├── .env                   # environment variables (secret)
└── .gitignore             # must include ".env"
```

---

If you are using VS Code, it will automatically pick up `.env` variables when running Python scripts (optional setting available).
