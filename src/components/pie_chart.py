import polars as pl
import plotly.express as px
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

    # -------- LAYOUT --------
    def _apply_layout(self, fig):
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
        }

        if self.height is not None:
            layout["height"] = self.height

        fig.update_layout(**layout)

    # -------- TRACES --------
    def _apply_traces(self, fig):
        fig.update_traces(
            domain={"x": [0.02, 0.98], "y": [0.28, 0.92]},
            textinfo="percent",
            hovertemplate="%{label}: %{value} (%{percent})<extra></extra>",
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
