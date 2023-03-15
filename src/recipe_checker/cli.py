import argparse
import os
from tempfile import TemporaryDirectory

import sparsezoo

from recipe_checker import _CONSOLE, __version__
from recipe_checker.checker import (
    evaluate_recipe_text,
    find_recipes,
    get_recipe_file_text,
    load_recipe_text,
)
from recipe_checker.logger import _LOGGER


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="recipe_checker",
        description="A CLI tool to validate recipes for a SparseZoo stub",
    )
    parser.add_argument(
        "ZOO_STUBS",
        nargs="+",
        help="one or more zoo stubs to check (separated by a space)",
    )
    parser.add_argument(
        "-V", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    return parser.parse_args()


def entrypoint():
    args = parse_args()
    _LOGGER.debug(args)

    temp_dir = TemporaryDirectory()
    _LOGGER.debug(f"setting model dir to temp dir '{temp_dir.name}'")
    os.putenv("SPARSEZOO_MODELS_PATH", temp_dir.name)
    sparsezoo.model.SAVE_DIR = temp_dir.name

    for zoo_stub in args.ZOO_STUBS:
        _CONSOLE.print(f"finding recipes for [yellow]{zoo_stub}[yellow]")
        recipes = find_recipes(zoo_stub)
        failures = []
        for name, url in recipes:
            _CONSOLE.print(f"    checking recipe [yellow]{name}[white]...[/] ", end="")
            try:
                content = get_recipe_file_text(url)
                recipe_data = load_recipe_text(content, name)
                _ = evaluate_recipe_text(recipe_data)
                result = "[green]PASS[/green]"
            except Exception as e:
                result = "[red]FAIL[/red]"
                failures.append((name, e))
            _CONSOLE.print(result)

            for name, error in failures:
                _CONSOLE.print(f"Error for {name}:")
                _CONSOLE.print(error)
