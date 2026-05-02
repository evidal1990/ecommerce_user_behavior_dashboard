from typing import cast

import polars as pl
import plotly.express as px
from plotly.graph_objects import Figure
import streamlit as st

_PIE_MARGIN_FALLBACK = {"l": 12.0, "r": 12.0, "t": 44.0, "b": 40.0}


class PieChart:
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
        self.height = layout_height
        self.margin = layout_margin or _PIE_MARGIN_FALLBACK

    # -------- PUBLIC --------
    def render(self) -> None:
        fig = self._build_figure()
        self._apply_layout(fig)
        self._apply_traces(fig)

        st.plotly_chart(
            fig,
            width="stretch",
            height="stretch",
        )

    # -------- BUILD --------
    def _build_figure(self):
        return px.pie(
            self.df,
            values=self.y,
            names=self.x,
            hole=0.7,
        )

    def _calculate_annotations(self):
        annotations: list[dict[str, object]] = []
        if self.df.is_empty():
            return annotations

        max_row = self.df.sort(
            by=[self.y, self.x],
            descending=[True, False],
        ).row(0, named=True)
        max_val = cast(float, max_row[self.y])
        sum_scalar = self.df[self.y].cast(pl.Float64).sum()
        total = cast(float, sum_scalar) if sum_scalar is not None else 0.0
        pct = 100.0 * max_val / total if total else 0.0

        label = max_row[self.x]
        annotations.append(
            dict(
                text=f"{pct:.2f}%<br>{label}",
                x=0.5,
                y=0.6,
                font_size=14,
                showarrow=False,
                xanchor="center",
            )
        )

        return annotations

    # -------- LAYOUT --------
    def _apply_layout(
        self,
        fig: Figure,
    ):
        annotations = self._calculate_annotations()
        layout = {
            "dragmode": False,
            "template": "plotly_white",
            "showlegend": True,
            "title": {
                "text": self.title,
                "font": {"size": 18},
                "pad": {"b": 44},
                "x": 0,
                "xanchor": "left",
            },
            "legend": {
                "title_text": "",
                "orientation": "h",
                "yanchor": "bottom",
                "y": 0.02,
                "xanchor": "center",
                "x": 0.5,
                "xref": "paper",
                "yref": "paper",
                "font": {"size": 14},
            },
            "margin": self.margin,
            "annotations": annotations,
        }

        if self.height is not None:
            layout["height"] = self.height

        fig.update_layout(**layout)

    # -------- TRACES --------
    def _apply_traces(self, fig):
        # Fatias: d3-format; `.1%` = percentual com 1 casa (Plotly sobrescreve textinfo).
        _pct_one_dec = "%{percent:.2%}"
        fig.update_traces(
            domain={"x": [0.02, 0.98], "y": [0.28, 0.92]},
            texttemplate=_pct_one_dec,
            hovertemplate=f"%{{label}}: %{{value}} ({_pct_one_dec})<extra></extra>",
            insidetextfont={
                "family": "Arial",
                "color": "white",
                "size": 13,
                "weight": "bold",
            },
            outsidetextfont={
                "color": "#333333",
                "size": 14,
            },
        )
