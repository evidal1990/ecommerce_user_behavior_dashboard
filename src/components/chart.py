import streamlit as st
import polars as pl
import plotly.express as px
from plotly.graph_objects import Figure


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

    def plot(
        self,
        fig: Figure,
    ) -> None:
        fig.update_layout(
            dragmode=False,
            title=self.title,
            xaxis_title=self.x,
            yaxis_title=self.y,
            template="plotly_white",
            xaxis_tickangle=-45,
        )
        max_total = self.df.group_by(self.x).agg(pl.col(self.y).sum()).max()[self.y]
        fig.update_yaxes(range=[0, max_total * 1.1])
        fig.update_xaxes(range=[0, self.df[self.x].max()])
        fig.update_traces(
            hovertemplate="%{x}: %{y}<extra></extra>",
            texttemplate="%{y}",
            textposition="auto",
            textfont_size=12,
            textfont_weight="bold",
        )
        st.plotly_chart(fig, use_container_width=True)
