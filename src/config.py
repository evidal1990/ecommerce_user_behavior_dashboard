"""Constantes e mapeamentos da aplicação."""

import os
from pathlib import Path

BASE_DIR: Path = Path(__file__).resolve().parent.parent


def load_project_env() -> None:
    """Carrega o primeiro .env encontrado (raiz do projeto ou cwd)."""
    for path in (BASE_DIR / ".env", Path.cwd() / ".env"):
        if not path.is_file():
            continue
        try:
            raw = path.read_text(encoding="utf-8-sig")
        except OSError:
            continue
        for line in raw.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" not in line:
                continue
            key, _, val = line.partition("=")
            key = key.strip()
            val = val.strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in "\"'":
                val = val[1:-1]
            if key:
                os.environ[key] = val
        return


load_project_env()
HEADER_ICON: Path = BASE_DIR / "icons" / "header-bar-icon.png"

PAGE_TITLE = "Dashboard de KPIs de Usuários de E-commerce"
KPI_HEADER_HEIGHT = "3.5rem"
SIDEBAR_FS_TITLE = "1.125rem"
SIDEBAR_FS_BODY = "1rem"

NAV_LABELS: list[str] = [
    "Visão Geral",
    "KPIs Descritivos",
    "KPIs Comportamentais",
    "KPIs Operacionais",
    "KPIs Estratégicos",
    "Assistente de Análise",
]

NAV_ICONS: list[str] = [
    "house",
    "file-earmark-text",
    "diagram-3",
    "table",
    "award",
    "robot",
]

# Rotas na URL: ?page=kpis-descritivos
PAGE_SLUGS: dict[str, str] = {
    "Visão Geral": "visao-geral",
    "KPIs Descritivos": "kpis-descritivos",
    "KPIs Comportamentais": "kpis-comportamentais",
    "KPIs Operacionais": "kpis-operacionais",
    "KPIs Estratégicos": "kpis-estrategicos",
    "Assistente de Análise": "assistente-analise",
}
SLUG_TO_LABEL: dict[str, str] = {s: t for t, s in PAGE_SLUGS.items()}

SEGMENT_OPTIONS: tuple[str, ...] = (
    "País",
    "Faixa Etária",
    "Faixa de Renda",
)
