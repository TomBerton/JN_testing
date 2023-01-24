import os
import fire
import questionary
from jntest.jn_testing import test_notebooks

def test():
    """The script tests all Jupyter notebooks in the current working directory."""
    all_folders = [x[0] for x in os.walk(os.getcwd())]
    test_notebooks(all_folders)

def cli():
    fire.Fire({
         "test": test
        })
