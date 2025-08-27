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

Do you want me to also add a **section 4** on *using virtual environments or conda* inside Kubeflow JupyterLab, so dependencies don’t pollute the base environment?
```
