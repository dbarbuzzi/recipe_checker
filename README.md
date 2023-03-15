# recipe_checker

`recipe_checker` is a simple CLI tool to check the ability to load recipe(s) in SparseML for one or more zoo stubs.

## Setup

You can install `recipe_checker` from GitHub:

```shell
pip install git+https://github.com/dbarbuzzi/recipe_checker.git#egg=recipe_checker
```

## Usage

Once installed, you can invoke the CLI command via `python -m recipe_checker`. Alternatively, a CLI alias called `check-recipe` is installed, so either of these commands would work to show the help text/usage instructions:

```shell
python -m recipe_checker --help
check-recipe --help
```

## Functionality

Currently, only zoo stubs are supported and the behavior is to validate recipes for all available recipes for each given zoo stub.

In the future, changes may include specifying a file to check or only checking a specific recipe file.
