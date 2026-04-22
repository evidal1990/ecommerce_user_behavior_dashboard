import streamlit as st

from src.components.bar_chart import BarChart
from src.services.transform import process_kpi

# Espaço entre os cards e esta secção (move os gráficos para baixo).
_SECTION_TOP_PX = 40
# Espaço no topo *dentro* do container com borda, antes do gráfico.
_CONTAINER_TOP_PX = 8
# Altura total da figura (limita o container; menor que o auto do Plotly).
_CHART_LAYOUT_HEIGHT_PX = 300
# Margens mais compactas que o default do Chart → mais área útil para as barras.
_CHART_LAYOUT_MARGIN = {"l": 48.0, "r": 24.0, "t": 26.0, "b": 0.0}


def _block_spacer_px(height_px: int) -> None:
    """Altura fixa + zero-width space: div vazio com só padding costuma colapsar no Streamlit."""
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

    def render(self) -> None:
        _block_spacer_px(_SECTION_TOP_PX)
        col1, col2 = st.columns(2, gap="small")
        with col1:
            with st.container(border=True):
                _block_spacer_px(_CONTAINER_TOP_PX)
                BarChart(
                    title="Top 3 Países com Maior Volume de Usuários",
                    df=self.top_countries_df,
                    layout_height=_CHART_LAYOUT_HEIGHT_PX,
                    layout_margin=_CHART_LAYOUT_MARGIN,
                ).render()
        with col2:
            with st.container(border=True):
                _block_spacer_px(_CONTAINER_TOP_PX)
                BarChart(
                    title="Top 3 Categorias de Produtos Preferidas",
                    df=self.top_product_categories_df,
                    layout_height=_CHART_LAYOUT_HEIGHT_PX,
                    layout_margin=_CHART_LAYOUT_MARGIN,
                ).render()
