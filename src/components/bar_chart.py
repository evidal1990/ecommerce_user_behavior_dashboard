import streamlit as st
import polars as pl
import plotly.express as px
from src.components.chart import Chart


class BarChart(Chart):
    def __init__(
        self,
        title: str,
        df: pl.DataFrame | None = None,
        x: str = "dimension",
        y: str = "value",
        group: bool = False,
        layout_height: int | None = None,
        layout_margin: dict[str, float] | None = None,
    ):
        super().__init__(
            title=title,
            df=df if df is not None else pl.DataFrame(),
            x=x,
            y=y,
            layout_height=layout_height,
            layout_margin=layout_margin,
        )
        self.group = group

    def render(self) -> None:
        if self.group:
            fig = px.bar(
                self.df,
                x=self.x,
                y=self.y,
                barmode="stack",
                color="category",
            )
        else:
            fig = px.bar(
                self.df,
                x=self.x,
                y=self.y,
                barmode="stack",
            )

        super().plot(fig)
