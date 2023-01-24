# Testing Jupyter Notebooks

## About

This repository will test Jupyter notebooks from the command line.

## Instructions

To get started, visit [https://www.anaconda.com/](https://www.anaconda.com/) and download the latest Anaconda distribution for your operating system. Conda is a part of the Anaconda distribution and will be installed with Anaconda.

Once conda is installed, you can run the following commands to ensure that you have the latest version of conda and anaconda. These commands can also be used to update an existing install to the latest stable version:

* `conda update conda`

* `conda update anaconda`

* `conda update -n base -c defaults conda`

Then, create a new Conda environment the following:

```shell
conda create -n <name> python=3.10 anaconda
```

Make sure you [keep your anaconda up to date](https://www.anaconda.com/blog/keeping-anaconda-date).

If you need to remove the environment, you can use `conda env remove -n <name> --all` and then revisit the steps above to reinstall.

Be sure to activate the environment using `conda activate <name>`.

## Testing Jupyter Notebooks

Follow these [instructions](utils/jn_test/README.md) to set up the testing environment.

* **Note:** The [Jupyter notebook test script](utils/jn_test/src/jntest/jn_testing.py) uses `nbformat`, which is install when you create the environment. And, it uses the default `python3` kernel to run the Jupyter notebooks.
