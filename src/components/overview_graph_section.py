import streamlit as st
import polars as pl
from src.components.bar_chart import BarChart
from src.services.transform import process_kpi

_SECTION_TOP_PX = 40
_CONTAINER_TOP_PX = 8
_CHART_LAYOUT_HEIGHT_PX = 300
_CHART_LAYOUT_MARGIN = {"l": 48.0, "r": 24.0, "t": 26.0, "b": 0.0}


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


class OverviewGraphSection:
    def __init__(
        self,
        top_countries: list[dict],
        top_product_categories: list[dict],
    ):
        self.top_countries_df = process_kpi(top_countries)
        self.top_product_categories_df = process_kpi(top_product_categories)

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
                layout_margin=_CHART_LAYOUT_MARGIN,
            ).render()

    def render(self) -> None:
        _block_spacer_px(_SECTION_TOP_PX)
        col1, col2 = st.columns(2, gap="medium")
        with col1:
            self._render_bar_chart(
                title="Top 3 Países Mais Visitados",
                df=self.top_countries_df,
            )
        with col2:
            self._render_bar_chart(
                title="Top 3 Categorias de Produtos Preferidas",
                df=self.top_product_categories_df,
            )
