# Getting Started with JupyterLab in a Kubeflow Environment

This guide provides a quick reference for running Python scripts and managing dependencies from a **JupyterLab notebook within a Kubeflow environment**.

---

### 1. Running a Python Script

The most common way to execute your Python code is by using the terminal.

1. **Create your Python file** (e.g., `main.py`) inside your persistent volume.  
2. Open a new **terminal** from the JupyterLab interface (click the **`+`** icon in the file browser):  

   ![Run Command](./terminal%20luncher.png "Open Terminal in JupyterLab")  

3. Navigate to the directory where your file is saved.  
4. Execute the script using the following command:

```bash
python3 your_file_name.py


> **Note:** Kubeflow notebooks are pre-configured to use `python3` as the standard interpreter.

---

### 2. Making a Script Executable

For convenience, you can make your Python script directly executable, similar to a shell command.

1. Add a **shebang line** to the very top of your Python file. This tells the system to use the `python3` interpreter:

```python
#!/usr/bin/env python3
```

2. In the terminal, grant the file executable permissions:

```bash
chmod +x your_file_name.py
```

3. Now, you can run the script directly from the terminal by typing its path:

```bash
./your_file_name.py
```

💡 **Practice:** Try making the [`log_run.py`](https://github.com/aymenabid-lab/kubeflowCESLab/blob/main/log_run.py) script from the example repository executable and then run it.


---

### 3. Installing Python Dependencies

To ensure your code runs correctly, you'll need to install any required libraries listed in the `requirements.txt` file.

1. Open a terminal in the same directory where your `requirements.txt` file is located.
2. Run the following command to install all the dependencies:

```bash
pip install -r requirements.txt
```

This command uses `pip`, Python's package installer, to read the list of libraries from the file and install them into your JupyterLab environment.

```


# GiT use
#Push error
if it's
```
! [rejected] master -> master (non-fast-forward)

error: failed to push some refs to 'https://github.com/
```
or you are in this pahse
```
  GNU nano 6.2       /home/jovyan/.git/MERGE_MSG                

Merge remote-tracking branch 'refs/remotes/solution/master'
#Please enter a commit message to explain why this merge is ne>
#especially if it merges an updated upstream into a topic bran>
#...
#Lines starting with '#' will be ignored, and an empty message>
#the commit.
```
it's due to other remote push for other device or online
## Solution
This is a **`non-fast-forward`** error, meaning your local branch is "behind" the remote branch. This happens when new commits have been pushed to the remote repository that you don't have locally. Git rejects your push to prevent you from overwriting this new work.

Here's a breakdown of what to do, based on your previous aversion to `git pull`:

***

### 1. The Standard Fix (Using `git pull`)

The safest and most common way to resolve this is to **pull** the new changes from the remote repository. This fetches the remote changes and automatically merges them with your local commits.

1.  **Pull the remote changes**:
    `git pull origin master`
    This command fetches the latest commits from the `master` branch on the `origin` remote and attempts to merge them with your local `master` branch.
2.  **Resolve any merge conflicts**:
    If both you and the remote repository have changed the same lines of code, Git will pause the merge and ask you to fix the conflicts. Open the affected files, edit them to combine the correct changes, and then `git add` and `git commit` to finalize the merge.
3.  **Push your changes**:
    `git push origin master`
    Since your local branch is now up-to-date with the remote, the push will succeed.

***

### 2. The Alternative Fix (Using `git fetch` and `git rebase`)

If you prefer a cleaner, more linear history without a "merge commit," this is the best alternative to `git pull`.

1.  **Fetch the remote changes**:
    `git fetch origin master`
    This downloads the remote commits but does not merge them.
2.  **Rebase your changes**:
    `git rebase origin/master`
    This command "replays" your local commits on top of the latest commit from the remote branch, creating a cleaner history. 
3.  **Push your changes**:
    `git push origin master`
    Your push will now be a "fast-forward" and will be accepted.

***

### 3. The Risky Option (Using `git push --force`)

This is highly discouraged for shared repositories. This command will **overwrite** the remote branch with your local branch, permanently deleting any commits that are only on the remote. **You should only use this if you are absolutely sure no one else has pushed to the repository.**

`git push --force`

To use a slightly safer version:

`git push --force-with-lease`

This will only force the push if the remote branch hasn't been updated since you last fetched it. This prevents you from accidentally overwriting someone else's work.
