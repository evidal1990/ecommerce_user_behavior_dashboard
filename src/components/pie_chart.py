import streamlit as st
import polars as pl
import plotly.express as px
from src.components.chart import Chart


class PieChart(Chart):
    def __init__(
        self,
        title: str,
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
        fig = px.pie(self.df, values=self.y, names=self.x, hole=0.4)
        fig.update_traces(textinfo="percent+label")
        super().plot(fig)
