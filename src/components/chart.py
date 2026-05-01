import streamlit as st
import polars as pl
from plotly.graph_objects import Figure

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


class Chart:
    def __init__(
        self,
        title: str,
        df: pl.DataFrame,
        x: str = "dimension",
        y: str = "value",
        *,
        layout_height: int | None = None,
        layout_margin: dict[str, float] | None = None,
    ) -> None:
        self.x = x
        self.y = y
        self.title = title
        self.df = df
        self.layout_height = layout_height
        self.layout_margin = layout_margin

    def plot(
        self,
        fig: Figure,
    ) -> None:
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
            "legend": _LEGEND,
            "showlegend": True,
        }
        if self.layout_height is not None:
            layout["height"] = self.layout_height
        fig.update_layout(**layout)
        max_total = self.df.group_by(self.x).agg(pl.col(self.y).sum()).max()[self.y]
        fig.update_yaxes(range=[0, max_total * 1.1])
        fig.update_xaxes(range=[0, self.df[self.x].max()])
        fig.update_traces(
            hovertemplate="%{x}: %{y}<extra></extra>",
            texttemplate="%{y}",
            textposition="auto",
            textfont_size=14,
            textfont_color="white",
            textfont_weight="bold",
        )
        st.plotly_chart(fig, width="stretch")
