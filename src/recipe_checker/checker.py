from pathlib import Path
from tempfile import NamedTemporaryFile
from typing import List, Tuple

from requests import Session
from sparseml.optim.helpers import (
    evaluate_recipe_yaml_str_equations,
    load_recipe_yaml_str,
)
from sparsezoo.model import Model
from sparsezoo.utils.authentication import get_auth_header


__CLIENT = Session()
__CLIENT.headers.update(get_auth_header())


def load_recipe_text(text: str, name: str) -> str:
    with NamedTemporaryFile("w+", suffix=name, delete=False) as f:
        f.write(text)
        f.seek(0)
        loaded = load_recipe_yaml_str(f.name)
    Path(f.name).unlink()
    return loaded


def evaluate_recipe_text(text: str) -> str:
    return evaluate_recipe_yaml_str_equations(text)


def find_recipes(stub: str) -> List[Tuple[str, str]]:
    model = Model(stub)
    return [(f.name, f.url) for f in model.recipes.files]


def get_recipe_file_text(url: str) -> str:
    response = __CLIENT.get(url)
    response.raise_for_status()
    return response.content.decode("utf-8")
