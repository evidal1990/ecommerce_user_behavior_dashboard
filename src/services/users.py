from src.services.api import get_kpi
from src.services.kpi_config import KPI_CONFIG

USERS_KPI_TYPE = "users"


def _fetch_users_grouped(kpi_name: str) -> list[dict]:
    dimension = KPI_CONFIG[kpi_name]["dimension"]
    return get_kpi(
        kpi_name=kpi_name,
        kpi_type=USERS_KPI_TYPE,
        param_type="group_by",
        param_value=dimension,
    )


def fetch_users_by_age_group() -> list[dict]:
    return _fetch_users_grouped("users_by_age_group")


def fetch_users_by_annual_income() -> list[dict]:
    return _fetch_users_grouped("users_by_annual_income")
