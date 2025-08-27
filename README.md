Getting Started: Using JupyterLab in a Kubeflow Solution

This guide provides best practices for running Python scripts and managing dependencies from a JupyterLab notebook within a Kubeflow environment. It's designed to help you efficiently set up your workspace and execute your code.

1. Running a Python Script in the Terminal

This is the most common way to execute your Python code.

    Create your Python file (e.g., main.py) inside your persistent volume.

    Open a new terminal from the JupyterLab interface. You can typically do this by clicking the "+" icon in the file browser and selecting "Terminal."

    Navigate to the directory where your file is saved.

    Execute the script using the following command:

Bash

python3 your_file_name.py

    Note: Kubeflow notebooks come pre-configured with python3 as the standard interpreter.

2. Making a Script Executable

For more advanced use cases, you can make your Python script directly executable, just like a shell command.

    Add a shebang line to the very top of your Python file. This line tells your system to use the python3 interpreter.

Python

#!/usr/bin/env python3

    In the terminal, grant the file executable permissions using the chmod command.

Bash

chmod +x your_file_name.py

    Now, you can run the script directly from the terminal.

Bash

./your_file_name.py

Practice: Try this method by running the log_run.py script from the example repository.

3. Installing Python Dependencies

To ensure your code runs without errors, you'll need to install any required libraries listed in the requirements.txt file.

    Open a terminal in the same directory where your requirements.txt file is located.

    Run the following command to install all the dependencies:

Bash

pip install -r requirements.txt

This command uses pip, Python's package installer, to read the list of libraries and install them into your JupyterLab environment.
