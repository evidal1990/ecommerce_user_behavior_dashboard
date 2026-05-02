import streamlit as st
import polars as pl
import plotly.express as px
from plotly.graph_objects import Figure
from src.components.plotly_config import PLOTLY_STREAMLIT_CONFIG

_LAYOUT_MARGIN = dict(l=20, r=20, t=80, b=40)
DTYPES = (
    pl.Int8,
    pl.Int16,
    pl.Int32,
    pl.Int64,
    pl.UInt8,
    pl.UInt16,
    pl.UInt32,
    pl.UInt64,
    pl.Float32,
    pl.Float64,
)


class BarChart:
    def __init__(
        self,
        title: str,
        df: pl.DataFrame,
        x: str = "dimension",
        y: str = "value",
        group: bool = False,
        layout_height: int | None = None,
        layout_margin: dict[str, float] | None = None,
        angle: int = 0,
        orientation: str = "v",
    ):
        self.title = title
        self.df = df
        self.x = x
        self.y = y
        self.group = group
        self.height = layout_height
        self.margin = layout_margin or _LAYOUT_MARGIN
        self.angle = angle
        self.orientation = orientation

    # -------- PUBLIC --------
    def render(self) -> None:
        fig = self._build_figure()
        self._apply_layout(fig)

        if not self.df.is_empty():
            max_total = self._compute_max_total()
            self._apply_axes(fig, max_total)
            self._apply_numeric_range(fig)
            self._apply_traces(fig)

        st.plotly_chart(
            fig,
            width="stretch",
            config=PLOTLY_STREAMLIT_CONFIG,
        )

    # -------- BUILD --------
    def _build_figure(self):
        x_axis, y_axis = self._resolve_axes()

        return px.bar(
            self.df,
            x=x_axis,
            y=y_axis,
            color="category" if self.group else None,
            barmode="stack",
            orientation=self.orientation,
        )

    def _resolve_axes(self):
        is_horizontal = self._is_horizontal()
        return (self.y, self.x) if is_horizontal else (self.x, self.y)

    # -------- LAYOUT --------
    def _apply_layout(self, fig):
        layout = {
            "title": self.title,
            "title_font_size": 18,
            "template": "plotly_white",
            "height": self.height,
            "margin": self.margin,
            "showlegend": self.group,
        }
        fig.update_layout(**layout)

    # -------- DATA --------
    def _compute_max_total(self):
        return (
            self.df.group_by(self.x)
            .agg(pl.col(self.y).sum())
            .select(pl.col(self.y).max())
            .item()
        )

    # -------- AXES --------
    def _apply_axes(
        self,
        fig: Figure,
        max_total: float,
    ):
        if self._is_horizontal():
            x_axes = {
                "range": [0, max_total * 1.1],
                "title": "",
                "tickfont_size": 14,
                "automargin": False,
            }
            y_axes = {
                "title": "",
                "tickfont_size": 14,
            }
        else:
            x_axes = {
                "tickangle": self.angle,
                "title": "",
                "tickfont_size": 14,
                "automargin": False,
            }
            y_axes = {
                "range": [0, max_total * 1.1],
                "title": "",
                "tickfont_size": 14,
            }
        fig.update_xaxes(**x_axes)
        fig.update_yaxes(**y_axes)

    def _apply_numeric_range(
        self,
        fig: Figure,
    ):
        numeric_col = self.y if self._is_horizontal() else self.x
        dtype = self.df.schema[numeric_col]

        if dtype in DTYPES:
            fig.update_xaxes(range=[0, self.df[numeric_col].max()])

    # -------- TRACES --------
    def _apply_traces(
        self,
        fig: Figure,
    ):
        fig.update_traces(
            texttemplate="<b>%{x}</b>" if self._is_horizontal() else "<b>%{y}</b>",
            textposition="auto",
        )

    # -------- HELPERS --------
    def _is_horizontal(self):
        return self.orientation == "h"
