import streamlit as st
import polars as pl
from plotly.graph_objects import Figure

_LAYOUT_MARGIN = dict[str, int](
    l=52,
    r=28,
    t=72,
    b=0,
)
_AXIS_TICK_FONT = dict[str, int](
    size=14,
)
_XAXIS = dict[str, str | dict[str, int] | int](
    title="",
    tickfont=_AXIS_TICK_FONT,
    tickangle=0,
)
_YAXIS = dict[str, str | dict[str, int]](
    title="",
    tickfont=_AXIS_TICK_FONT,
)
_LEGEND = dict[str, str | float](
    title_text="",
    orientation="h",
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
    ) -> None:
        self.x = x
        self.y = y
        self.title = title
        self.df = df

    def plot(self, fig: Figure) -> None:
        is_pie = bool(fig.data and getattr(fig.data[0], "type", None) == "pie")

        fig.update_layout(
            dragmode=False,
            title=self.title,
            title_font_size=18,
            margin=_LAYOUT_MARGIN,
            xaxis=_XAXIS,
            yaxis=_YAXIS,
            template="plotly_white",
            legend=_LEGEND,
            showlegend=True,
        )
        if not is_pie:
            fig.update_traces(
                hovertemplate="%{x}: %{y}<extra></extra>",
                texttemplate="%{y}",
                textposition="auto",
                textfont_size=14,
                textfont_color="white",
                textfont_weight="bold",
            )
            max_total = self.df.group_by(self.x).agg(pl.col(self.y).sum()).max()[self.y]
            fig.update_yaxes(range=[0, max_total * 1.1])
            fig.update_xaxes(range=[0, self.df[self.x].max()])
        else:
            fig.update_traces(
                textinfo="percent",
                hovertemplate="%{label}: %{value} (%{percent})<extra></extra>",
                textposition="auto",
                textfont_size=14,
                textfont_color="white",
                textfont_weight="bold",
            )
        st.plotly_chart(fig, use_container_width=True)
