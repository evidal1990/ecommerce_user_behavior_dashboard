"""Type stubs for streamlit-option-menu (PyPI: streamlit-option-menu)."""

from collections.abc import Callable, Sequence
from typing import Any

def option_menu(
    menu_title: str,
    options: Sequence[str],
    default_index: int = 0,
    menu_icon: str | None = None,
    icons: Sequence[str] | None = None,
    orientation: str = "vertical",
    styles: dict[str, Any] | None = None,
    manual_select: int | None = None,
    key: str | None = None,
    on_change: Callable[[str], Any] | None = None,
) -> str: ...
