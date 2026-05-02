"""Carga paralela agregada com @st.cache_data (fora de `src.pages.*` por compatibilidade Streamlit)."""

from typing import Any, Callable

import streamlit as st

from src.config import API_CACHE_TTL_SECONDS
from src.clients import (
    MetricsApiClient,
    UserApiClient,
)
from src.services.parallel_tasks import run_parallel_callables


_metrics_api = MetricsApiClient()
_user_api = UserApiClient()


@st.cache_data(
    ttl=API_CACHE_TTL_SECONDS,
    show_spinner="Carregando indicadores…",
)
def load_overview_data() -> dict[str, Any]:
    metrics: dict[str, Callable[[], int]] = {
        "total_users": _metrics_api.fetch_total_users,
        "avg_purchase_conversion_rate": _metrics_api.fetch_avg_purchase_conversion_rate,
        "churn_rate": _metrics_api.fetch_churn_rate,
        "avg_daily_session_time": _metrics_api.fetch_avg_daily_session_time,
    }
    users: dict[str, Callable[[], list[dict[str, Any]]]] = {
        "users_by_premium_adoption": _user_api.fetch_users_by_premium_adoption,
        "top_countries": _user_api.fetch_top_countries,
        "top_product_categories": _user_api.fetch_top_product_categories,
        "users_by_device_type": _user_api.fetch_users_by_device_type,
    }
    return run_parallel_callables({**metrics, **users})


@st.cache_data(
    ttl=API_CACHE_TTL_SECONDS,
    show_spinner="Carregando KPIs descritivos…",
)
def load_descriptive_kpis_data() -> dict[str, Any]:
    users: dict[str, Callable[[], list[dict[str, Any]]]] = {
        "users_by_age_group": _user_api.fetch_users_by_age_group,
        "users_by_annual_income": _user_api.fetch_users_by_annual_income,
        "users_by_gender": _user_api.fetch_users_by_gender,
        "users_by_neighborhood": _user_api.fetch_users_by_neighborhood,
        "users_by_employment_status": _user_api.fetch_users_by_employment_status,
        "users_by_household_size": _user_api.fetch_users_by_household_size,
        "users_by_has_children": _user_api.fetch_users_by_has_children,
        "users_by_education_level": _user_api.fetch_users_by_education_level,
        "users_by_relationship_status": _user_api.fetch_users_by_relationship_status,
    }
    return run_parallel_callables(users)
