import streamlit as st
import polars as pl
from src.services.transform import process_kpi
from src.clients import (
    MetricsApiClient,
    UserApiClient,
)
from src.components import (
    Card,
    BarChart,
    PieChart,
)


_SECTION_TOP_PX = 40
_CONTAINER_TOP_PX = 8
_CHART_LAYOUT_HEIGHT_PX = 300
_BAR_LAYOUT_MARGIN = {"l": 36.0, "r": 20.0, "t": 26.0, "b": 36.0}
_PIE_LAYOUT_MARGIN = {"l": 12.0, "r": 12.0, "t": 26.0, "b": 0.0}


def _block_spacer_px(height_px: int) -> None:
    st.markdown(
        f"""
            <div style="
                display: block;
                height: {height_px}px;
                width: 100%;
                line-height: 0;
                font-size: 0;
            ">&#8203;</div>
            """,
        unsafe_allow_html=True,
    )


class OverviewPage:
    def __init__(self):
        self.metrics_api_client = MetricsApiClient()
        self.user_api_client = UserApiClient()

    def _render_bar_chart(
        self,
        title: str,
        df: pl.DataFrame,
    ) -> None:
        with st.container(border=True):
            _block_spacer_px(_CONTAINER_TOP_PX)
            BarChart(
                title=title,
                df=df,
                layout_height=_CHART_LAYOUT_HEIGHT_PX,
                layout_margin=_BAR_LAYOUT_MARGIN,
            ).render()

    def _render_pie_chart(
        self,
        title: str,
        df: pl.DataFrame,
    ) -> None:
        with st.container(border=True):
            _block_spacer_px(_CONTAINER_TOP_PX)
            PieChart(
                title=title,
                df=df,
                layout_height=_CHART_LAYOUT_HEIGHT_PX,
                layout_margin=_PIE_LAYOUT_MARGIN,
            ).render()

    def _render_card(
        self,
        title: str,
        value: int,
        color1: int,
        color2: str,
        color3: str,
    ) -> None:
        Card(
            title=title,
            value=value,
            background=(f"linear-gradient({color1}deg, {color2} 0%, {color3} 100%);"),
        ).render()

    def render(self) -> None:
        # Cards
        col_card1, col_card2, col_card3, col_card4 = st.columns(4, gap="small")
        with col_card1:
            self._render_card(
                title="Total de Usuários",
                value=self.metrics_api_client.fetch_total_users(),
                color1=180,
                color2="#3A0CA3",
                color3="#7209B7",
            )
        with col_card2:
            self._render_card(
                title="Taxa de Conversão Média",
                value=self.metrics_api_client.fetch_avg_purchase_conversion_rate(),
                color1=180,
                color2="#3E8E41",
                color3="#256D2A",
            )
        with col_card3:
            self._render_card(
                title="Taxa de Churn Média",
                value=self.metrics_api_client.fetch_churn_rate(),
                color1=135,
                color2="#E63946",
                color3="#9B2226",
            )
        with col_card4:
            self._render_card(
                title="Tempo Médio de Sessão",
                value=self.metrics_api_client.fetch_avg_daily_session_time(),
                color1=180,
                color2="#3B82F6",
                color3="#1E40AF",
            )

        # Graphs
        _block_spacer_px(_SECTION_TOP_PX)
        row_graph1_col1, row_graph1_col2 = st.columns(2, gap="small")
        with row_graph1_col1:
            self._render_pie_chart(
                title="Adesão ao Plano Premium",
                df=process_kpi(self.user_api_client.fetch_users_by_premium_adoption()),
            )
        with row_graph1_col2:
            self._render_bar_chart(
                title="Top Países Com Mais Usuários",
                df=process_kpi(self.user_api_client.fetch_top_countries()),
            )
        row_graph2_col1, row_graph2_col2 = st.columns(2, gap="small")
        with row_graph2_col1:
            self._render_bar_chart(
                title="Top Categorias de Produtos Preferidas",
                df=process_kpi(self.user_api_client.fetch_top_product_categories()),
            )
        with row_graph2_col2:
            self._render_pie_chart(
                title="Distribuição de Usuários por Adesão ao Plano Premium",
                df=process_kpi(self.user_api_client.fetch_users_by_premium_adoption()),
            )
