from src.services.kpi_config import KPI_CONFIG


def get_kpi(kpi_name: str) -> list[dict]:
    raw_data = fetch_from_source()

    config = KPI_CONFIG[kpi_name]

    if config.get("type") == "aggregate":
        return normalize_kpi(raw_data)

    return normalize_kpi(
        raw_data,
        dimension=config["dimension"],
        value_field=config["value"],
    )


def fetch_from_source() -> list[dict]:
    return [
        {"age_group": "Early Adopters", "total_users": 174451.0},
        {"avg_referral_count": 5.0},
    ]


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
