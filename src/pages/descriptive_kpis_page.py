import streamlit as st
import polars as pl
from src.services.transform import process_kpi
from src.clients import (
    MetricsApiClient,
    UserApiClient,
)
from src.pages.base_page import BasePage


_SECTION_TOP_PX = 0

metrics_api_client = MetricsApiClient()
user_api_client = UserApiClient()


class DescriptiveKpisPage(BasePage):
    def __init__(self):
        super().__init__(
            container_top_px=8,
            chart_layout_height_px=300,
            bar_layout_margin={"l": 36.0, "r": 20.0, "t": 26.0, "b": 36.0},
            pie_layout_margin={"l": 12.0, "r": 12.0, "t": 26.0, "b": 0.0},
        )

    def render(self) -> None:
        st.markdown(
            '<h1 style="margin-top: -3.50rem; margin-bottom: 0.5rem;">KPIs Descritivos</h1>',
            unsafe_allow_html=True,
        )

        users = {
            "users_by_age_group": user_api_client.fetch_users_by_age_group,
        }
        data = self.fetch_all(users)

        row_graph1_col1 = st.columns(
            1, gap="small"
        )

        self._block_spacer_px(_SECTION_TOP_PX)
        self._render_pie_chart(
            title="Distribuição de Usuários por Faixa Etária",
            df=process_kpi(data["users_by_age_group"]),
        )
