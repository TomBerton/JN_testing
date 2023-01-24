# Jupyter Notebook Testing CLI Tool

## Install

First, make sure that there isn't a previous install in the "jn_test" folder.

```shell
rm -rf __pycache__ *egg*
```

Next, install the dependencies.

```shell
pip install -e .
```

## Usage

For help type the following:

```shell
jntest --help
```

To test your Jupyter notebooks, change the path on the command line to the desired directory and type the following:

```shell
jntest test
```
