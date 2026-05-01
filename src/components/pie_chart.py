import polars as pl
import plotly.express as px
import streamlit as st
from plotly.graph_objects import Figure

_PIE_MARGIN_FALLBACK = {"l": 12.0, "r": 12.0, "t": 44.0, "b": 40.0}


class PieChart():
    def __init__(
        self,
        title: str,
        df: pl.DataFrame | None = None,
        x: str = "dimension",
        y: str = "value",
        layout_height: int | None = None,
        layout_margin: dict[str, float] | None = None,
    ):
        self.title = title
        self.df = df if df is not None else pl.DataFrame()
        self.x = x
        self.y = y
        self.layout_height = layout_height
        self.layout_margin = layout_margin

    def render(self) -> None:
        fig = px.pie(
            self.df,
            values=self.y,
            names=self.x,
            hole=0.6,
        )
        margin = (
            self.layout_margin
            if self.layout_margin is not None
            else _PIE_MARGIN_FALLBACK
        )
        layout: dict = {
            "dragmode": False,
            "template": "plotly_white",
            "showlegend": True,
            "title": dict(
                text=self.title,
                font=dict(size=18),
                pad=dict(b=44),
                x=0,
                xanchor="left",
            ),
            "legend": dict(
                title_text="",
                orientation="h",
                yanchor="bottom",
                y=0.02,
                xanchor="center",
                x=0.5,
                xref="paper",
                yref="paper",
                font=dict(size=14),
            ),
            "margin": margin,
        }
        if self.layout_height is not None:
            layout["height"] = self.layout_height
        fig.update_layout(**layout)
        fig.update_traces(
            domain=dict(x=[0.02, 0.98], y=[0.28, 0.92]),
            textinfo="percent",
            hovertemplate="%{label}: %{value} (%{percent})<extra></extra>",
            insidetextfont=dict(
                family="Arial",
                color="white",
                size=14,
            ),
            outsidetextfont=dict(
                color="#333333",
                size=14,
            ),
        )
        st.plotly_chart(
            fig,
            width="stretch",
            height="stretch",
        )
