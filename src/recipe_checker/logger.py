import logging

from rich.logging import RichHandler


_LOGGER = logging.getLogger("recipe_checker")
_LOGGER.setLevel("DEBUG")
_LOGGER.addHandler(RichHandler())
