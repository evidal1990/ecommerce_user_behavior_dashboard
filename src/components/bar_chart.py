import streamlit as st
import polars as pl
import plotly.express as px
from polars.datatypes.classes import NumericType

from src.components.plotly_config import PLOTLY_STREAMLIT_CONFIG


_LAYOUT_MARGIN = dict(l=52, r=28, t=102, b=120)
_AXIS_TICK_FONT = dict(size=14)
_XAXIS = dict(title="", tickfont=_AXIS_TICK_FONT, tickangle=0)
_YAXIS = dict(title="", tickfont=_AXIS_TICK_FONT)
_LEGEND = dict(
    title_text="",
    orientation="v",
    yanchor="bottom",
    y=1.02,
    xanchor="center",
    x=0.5,
    font_size=14,
)


class BarChart():
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
        self.group = group
        self.title = title
        self.df = df if df is not None else pl.DataFrame()
        self.x = x
        self.y = y
        self.layout_height = layout_height
        self.layout_margin = layout_margin

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

        margin = (
            self.layout_margin if self.layout_margin is not None else _LAYOUT_MARGIN
        )
        layout: dict = {
            "dragmode": False,
            "title": dict(
                text=self.title,
                font=dict(size=18),
                pad=dict(b=24),
            ),
            "margin": margin,
            "xaxis": _XAXIS,
            "yaxis": _YAXIS,
            "template": "plotly_white",
            "showlegend": True,
        }
        layout["legend"] = _LEGEND
        if self.layout_height is not None:
            layout["height"] = self.layout_height
        fig.update_layout(
            dragmode=False,
            title=dict(
                text=self.title,
                font=dict(size=18),
                pad=dict(b=24),
            ),
            margin=margin,
            xaxis=_XAXIS,
            yaxis=_YAXIS,
            template="plotly_white",
            showlegend=self.group,
            legend=_LEGEND,
            height=self.layout_height,
        )
        max_total = self.df.group_by(self.x).agg(pl.col(self.y).sum()).max()[self.y]
        fig.update_yaxes(
            range=[0, max_total * 1.1],
            automargin=True,
        )
        if isinstance(self.df.schema[self.x], NumericType):
            fig.update_xaxes(range=[0, self.df[self.x].max()])
        fig.update_xaxes(
            automargin=False,
        )
        fig.update_traces(
            hovertemplate="%{x}: %{y}<extra></extra>",
            texttemplate="%{y}",
            textposition="auto",
            textfont_size=14,
            textfont_color="white",
            textfont_weight="bold",
        )
        st.plotly_chart(
            fig,
            width="stretch",
            height="stretch",
            config=PLOTLY_STREAMLIT_CONFIG,
        )
