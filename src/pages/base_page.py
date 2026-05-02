import streamlit as st
import polars as pl
from abc import abstractmethod
from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
)
from src.components import (
    Card,
    BarChart,
    PieChart,
)


class BasePage:
    def __init__(
        self,
        container_top_px: int = 0,
        chart_layout_height_px: int = 300,
        bar_layout_margin: dict[str, float] = {},
        pie_layout_margin: dict[str, float] = {},
    ):
        self._CONTAINER_TOP_PX = container_top_px
        self._CHART_LAYOUT_HEIGHT_PX = chart_layout_height_px
        self._BAR_LAYOUT_MARGIN = bar_layout_margin
        self._PIE_LAYOUT_MARGIN = pie_layout_margin
    @abstractmethod
    def render(self):
        pass

    def _render_bar_chart(
        self,
        title: str,
        df: pl.DataFrame,
        angle: int = 0,
        orientation: str = "v",
    ) -> None:
        with st.container(border=True):
            self._block_spacer_px(self._CONTAINER_TOP_PX)
            BarChart(
                title=title,
                df=df,
                layout_height=self._CHART_LAYOUT_HEIGHT_PX,
                layout_margin=self._BAR_LAYOUT_MARGIN,
                angle=angle,
                orientation=orientation,
            ).render()

    def _render_pie_chart(
        self,
        title: str,
        df: pl.DataFrame,
    ) -> None:
        with st.container(border=True):
            self._block_spacer_px(self._CONTAINER_TOP_PX)
            PieChart(
                title=title,
                df=df,
                layout_height=self._CHART_LAYOUT_HEIGHT_PX,
                layout_margin=self._PIE_LAYOUT_MARGIN,
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

    def fetch_all(
        self,
        tasks: dict,
    ):
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = {executor.submit(func): key for key, func in tasks.items()}
            results = {}
            for future in as_completed(futures):
                key = futures[future]
                try:
                    results[key] = future.result()
                except Exception as e:
                    results[key] = None
                    print(f"Erro ao buscar {key}: {e}")
        return results

    def _block_spacer_px(self, height_px: int):
        st.markdown(
            f"""
            <div style="
                display: block;
                height: {height_px}px;
            ">
            """,
            unsafe_allow_html=True,
        )
