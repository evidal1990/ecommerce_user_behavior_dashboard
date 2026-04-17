"""Leitura de recursos estáticos (ícones, etc.)."""

import base64
from pathlib import Path


def header_icon_img_html(icon_path: Path) -> str:
    if not icon_path.is_file():
        return ""
    b64 = base64.b64encode(icon_path.read_bytes()).decode("ascii")
    return (
        f'<img src="data:image/png;base64,{b64}" alt="" '
        'style="height:1.75rem;width:auto;flex-shrink:0;display:block;object-fit:contain;" />'
    )
