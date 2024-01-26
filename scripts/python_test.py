"""
This Python script will run and test all the Python files any folder in a given directory.
"""

import os
import subprocess
import sys


def get_folders():
    """ This function gets all the folders in the current working directory."""
    all_folders = [x[0] for x in  os.walk(os.getcwd())]
    return all_folders


def run_python_files():
    """ This function sorts all the folders in the directory, then searches for all the .py files
    in any subfolder, i.e., Solved, Unsolved in the directory.
    Then, it runs the files."""
    # Sort the folders or lessons (01-, 02- etc.)
    folders = get_folders()
    folders.sort()
    for subfolder in folders:
        os.chdir(subfolder)
        # Iterate through the files in the folder.
        for file in os.listdir():
            if file.endswith(".py"):
                print(f"Running Python file: {file}")
            else:
                continue
            try:
                # Run the Python file using subprocess
                subprocess.run(f'python {file}', check=False, shell=True)
            except subprocess.CalledProcessError as e:
                print(f"Error running {file}: {e}")


run_python_files()
