#!/usr/bin/env python3
#the !/usr/ is magic line to run as excutable
#this file is to record all print in log file
import sys
import os
import logging
class Logger(object):
    """
    A class to log console output to a file while also
    printing it to the terminal.
    """
    def __init__(self, filename="training.log"):
        # Keep a reference to the original standard output
        self.terminal = sys.stdout
        # Open the log file in append mode ('a')
        self.log = open(filename, "a")

    def write(self, message):
        """
        Writes a message to both the terminal and the log file.
        """
        self.terminal.write(message)
        self.log.write(message)

    def flush(self, *args, **kwargs):
        """
        Flushes the write buffers for both the terminal and the file.
        """
        self.terminal.flush()
        self.log.flush()
# ... your other imports and code ...

# Get the base name of the script file (e.g., "my_script.py")
script_name = os.path.basename(__file__)

# Remove the file extension (e.g., "my_script")
file_name_without_ext = os.path.splitext(script_name)[0]

# Construct the dynamic log file name
log_file_name = f"log_{file_name_without_ext}.log"
sys.stdout = Logger(log_file_name)
print(f"Logger activated. All console output from here will be saved to {log_file_name}")
print("-" * 50)