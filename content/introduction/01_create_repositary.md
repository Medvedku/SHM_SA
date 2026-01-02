+++
title = "Create repositary"
weight = 1
+++

For this demonstration, we will use the **GitHub Desktop** application to create a new repository.

### 1. Create a New Repository
You can create a new repository using the `Ctrl + N` shortcut or via the menu: `File` -> `New repository`.

{{< figure src="/SHM_SA/A_git/A01_new.png" link="/SHM_SA/A_git/A01_new.png" width="700" >}}

### 2. Configure Repository Settings
In the **Create a New Repository** menu, fill in the following details:

{{< figure src="/SHM_SA/A_git/A02_newrepo.png" link="/SHM_SA/A_git/A02_newrepo.png" width="700" >}}

* **Name & Description**: These are self-explanatory; choose a clear name for your project.
* **Local Path**: Usually the same path where you store your other GitHub projects.
* **Initialize with a README**: This is good practice as it provides an immediate description of your project.
* **Git Ignore**: Choose the **Python** template, since we will be working with Python.
* **License**: We will choose the standard **MIT License**, as we are not planning to monetize this project.

### 3. Project Folder

After clicking to `Create repositary` button new folder is created located in chosen path.
{{< figure src="/SHM_SA/A_git/A03_folder_before.png" link="/SHM_SA/A_git/A03_folder_before.png" width="700" >}}

It might be handy to move our bucket mirror here.
{{< figure src="/SHM_SA/A_git/A04_folder_after.png" link="/SHM_SA/A_git/A04_folder_after.png" width="700" >}}

We need to keep in mind that path will change and we will need to change it in **SA_R2 Downloader** aplication.

### 4. Update `.gitignore`

After moving database to project folder, git will track it as a change of project. 
{{< figure src="/SHM_SA/A_git/A05_git_before.png" link="/SHM_SA/A_git/A05_git_before.png" width="700" >}}

Since we dont need to track changes `parquets` folder, and we dont want to uplad whole database to GitHub, we include whole folder in `.gitignore` file.
We open this file in any text editor, scroll down and add name of database folder in my case its `parqets` with suffix `/` that indicates everything within this folder needs to be ignored.
{{< figure src="/SHM_SA/A_git/A06_gitignore_edit.png" link="/SHM_SA/A_git/A06_gitignore_edit.png" width="700" >}}

After saving change in `.gitignore` file, git will stop track changes within ignored files/folder of project. Number of changes droped down significantly.
{{< figure src="/SHM_SA/A_git/A07_git_after.png" link="/SHM_SA/A_git/A07_git_after.png" width="700" >}}

### 5. Initial Commit & Publishing

With the `.gitignore` file configured, it is time to perform the first commit and publish the repository to GitHub.

#### Committing Changes
It is necessary to provide a **Summary** for your changes. While it may feel tedious at first, adding a brief description to your commits is a vital habit that makes tracking the project's history much easier in the future. Once you have filled in these details, click the **Commit to main** button.

{{< figure src="/SHM_SA/A_git/A08_commit.png" link="/SHM_SA/A_git/A08_commit.png" width="700" >}}

#### Publishing to GitHub
After committing the initial project setup and the `.gitignore` edits, you need to push the code to the cloud. Click the **Publish repository** button. 

In the popup menu, you can finalize the repository name and description. You also have the option to keep the code **Private** or make it **Public**.

{{< figure src="/SHM_SA/A_git/A09_github.png" link="/SHM_SA/A_git/A09_github.png" width="700" >}}

---

The showcase repository for this project is available at: [https://github.com/Medvedku/sa_analysis](https://github.com/Medvedku/sa_analysis)

---
