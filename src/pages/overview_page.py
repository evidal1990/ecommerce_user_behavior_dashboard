import streamlit as st
import polars as pl
from typing import Callable, Any
from src.services.transform import process_kpi
from src.clients import (
    MetricsApiClient,
    UserApiClient,
)
from src.pages.base_page import BasePage


_SECTION_TOP_PX = 40


metrics_api_client = MetricsApiClient()
user_api_client = UserApiClient()


class OverviewPage(BasePage):
    def __init__(self):
        super().__init__(
            container_top_px=8,
            chart_layout_height_px=300,
            bar_layout_margin={
                "l": 0.0,
                "r": 10.0,
                "t": 26.0,
                "b": 0.0,
            },
            pie_layout_margin={
                "l": 12.0,
                "r": 12.0,
                "t": 26.0,
                "b": 17.0,
            },
        )

    def render(self) -> None:
        data = self._fetch_data()

        self._render_title("Principais Indicadores")
        self._render_cards(data)
        self._render_graphs(data)


    def _fetch_data(self) -> dict[str, int]:
        metrics: dict[str, Callable[[], int]] = {
            "total_users": metrics_api_client.fetch_total_users,
            "avg_purchase_conversion_rate": metrics_api_client.fetch_avg_purchase_conversion_rate,
            "churn_rate": metrics_api_client.fetch_churn_rate,
            "avg_daily_session_time": metrics_api_client.fetch_avg_daily_session_time,
        }
        users: dict[str, Callable[[], list[dict[str, Any]]]] = {
            "users_by_premium_adoption": user_api_client.fetch_users_by_premium_adoption,
            "top_countries": user_api_client.fetch_top_countries,
            "top_product_categories": user_api_client.fetch_top_product_categories,
            "users_by_device_type": user_api_client.fetch_users_by_device_type,
        }
        return self.fetch_all({**metrics, **users})

    def _render_cards(
        self,
        data: dict[str, int],
    ) -> None:
        col_card1, col_card2, col_card3, col_card4 = st.columns(
            4,
            gap="small",
        )
        with col_card1:
            self._render_card(
                title="Total de Usuários",
                value=data["total_users"],
                color1=180,
                color2="#3A0CA3",
                color3="#7209B7",
            )
        with col_card2:
            self._render_card(
                title="Taxa de Conversão Média",
                value=data["avg_purchase_conversion_rate"],
                color1=180,
                color2="#3E8E41",
                color3="#256D2A",
            )
        with col_card3:
            self._render_card(
                title="Taxa de Churn Média",
                value=data["churn_rate"],
                color1=135,
                color2="#E63946",
                color3="#9B2226",
            )
        with col_card4:
            self._render_card(
                title="Tempo Médio de Sessão",
                value=data["avg_daily_session_time"],
                color1=180,
                color2="#3B82F6",
                color3="#1E40AF",
            )

    def _render_graphs(
        self,
        data: dict[str, int],
    ) -> None:
        self._block_spacer_px(_SECTION_TOP_PX)
        row_graph1_col1, row_graph1_col2 = st.columns(
            2,
            gap="small",
        )
        with row_graph1_col1:
            self._render_pie_chart(
                title="Adesão ao Plano Premium",
                df=process_kpi(data["users_by_premium_adoption"]),
            )
        with row_graph1_col2:
            self._render_bar_chart(
                title="Top Países Com Mais Usuários",
                df=process_kpi(data["top_countries"]),
            )
        row_graph2_col1, row_graph2_col2 = st.columns(
            2,
            gap="small",
        )
        with row_graph2_col1:
            self._render_bar_chart(
                title="Top Categorias de Produtos Preferidas",
                df=process_kpi(data["top_product_categories"]),
            )
        with row_graph2_col2:
            self._render_pie_chart(
                title="Distribuição de Usuários por Dispositivo",
                df=process_kpi(data["users_by_device_type"]),
            )
