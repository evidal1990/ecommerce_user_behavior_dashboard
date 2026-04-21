import streamlit as st
import polars as pl
import plotly.express as px
from src.components.chart import Chart


class LineChart(Chart):
    def __init__(
        self,
        title: str = "",
        df: pl.DataFrame | None = None,
        x: str = "dimension",
        y: str = "value",
    ):
        super().__init__(
            title=title,
            df=df if df is not None else pl.DataFrame(),
            x=x,
            y=y,
        )

    def render(self) -> None:
        fig = px.line(self.df, x=self.x, y=self.y)
        fig.update_traces(line_shape="spline", mode="lines+markers")
        super().plot(fig)
