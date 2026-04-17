import os

import requests

from src.config import load_project_env
from src.services.kpi_config import KPI_CONFIG


def _api_base_url() -> str:
    base = (os.getenv("API_URL") or os.getenv("BASE_URL") or "").strip().rstrip("/")
    if not base:
        try:
            import streamlit as st

            sec = getattr(st, "secrets", None)
            if sec is not None:
                base = (
                    str(sec.get("API_URL", "") or sec.get("BASE_URL", "") or "")
                    .strip()
                    .rstrip("/")
                )
        except Exception:
            pass
    if not base:
        raise RuntimeError(
            "API_URL (ou BASE_URL) não definido. Crie .env na raiz com API_URL=https://... "
            "(ou use Secrets no Streamlit Cloud)."
        )
    return base


def get_kpi(
    kpi_name: str,
    kpi_type: str,
    param_type: str,
    param_value: str,
) -> list[dict]:
    config = KPI_CONFIG[kpi_name]
    raw_data = fetch_from_source(
        kpi_type=kpi_type,
        param_type=param_type,
        param_value=param_value,
    )

    if config.get("type") == "aggregate":
        return normalize_kpi(raw_data)

    return normalize_kpi(
        raw_data,
        dimension=config["dimension"],
        value_field=config["value"],
    )


def fetch_from_source(
    kpi_type: str,
    param_type: str,
    param_value: str,
) -> list[dict]:
    headers: dict[str, str] = {}
    load_project_env()
    api_key = os.getenv("API_KEY")
    if not api_key:
        try:
            import streamlit as st

            sec = getattr(st, "secrets", None)
            if sec is not None:
                api_key = str(sec.get("API_KEY", "") or "") or None
        except Exception:
            pass
    if api_key:
        headers["x-api-key"] = api_key

    response = requests.get(
        f"{_api_base_url()}/{kpi_type}",
        params={
            param_type: param_value,
        },
        headers=headers,
    )
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from API: {response.status_code}")
    return response.json()


def normalize_kpi(
    data: list,
    dimension: str | None = None,
    value_field: str | None = None,
) -> list[dict]:
    """
    Normaliza qualquer retorno de KPI para:
    [{"dimension": ..., "value": ...}]

    - dimension=None: KPI agregado (usa a primeira chave de cada linha como valor).
    - dimension=str: nome do campo da dimensão; o valor vem de value_field ou "value",
    ou da primeira chave que não seja a dimensão.
    """
    normalized: list[dict] = []

    for row in data:
        if dimension is None:
            key = list(row.keys())[0]
            normalized.append(
                {
                    "dimension": "total",
                    "value": row[key],
                }
            )
        else:
            vkey = value_field if value_field else "value"
            if vkey not in row:
                others = [k for k in row if k != dimension]
                vkey = others[0] if others else list(row.keys())[0]
            normalized.append(
                {
                    "dimension": row[dimension],
                    "value": row[vkey],
                }
            )

    return normalized
