"""
This Python script will run and test all the Jupyter notebooks any folder in a given directory.
Make sure you have created the PythonData Conda environment as in the course.
Then add that Conda environment to the Jupyter kernel.
"""

import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError

def test_notebooks(folders):
    """ This function sorts all the folders in the directory, then searches for all the .ipynb files
    in any subfolder, i.e., Solved, Unsolved, Resources, Images, etc, in the directory.
    Then, it runs the test on the .ipynb files using nbconvert."""
    # Sort the folders or lessons (01-, 02- etc.)
    sorted_folders = sorted(folders)
    for subfolder in sorted_folders:
        if subfolder.endswith(".ipynb_checkpoints"):
            continue
        os.chdir(subfolder)
        # Iterate through the files in the folder.
        for file in os.listdir():
            if file.endswith(".ipynb") and not file.endswith("_colab.ipynb"):
                with open(file, encoding="utf-8") as nb_file:
                    read_nb = nbformat.read(nb_file, as_version=4)
                    # Execute the Jupyter notebook with the Python 3 kernel.
                    execute_nb = ExecutePreprocessor(timeout=600, kernel_name='python3')
                    try:
                        output = execute_nb.preprocess(read_nb)
                        print(f"{subfolder}/{file} passed.")
                    except CellExecutionError as error:
                        output = None
                        print(f"There was an error executing {subfolder}/{file}.")
                        print(error)
