import streamlit as st
import polars as pl
from src.components.cards import Card
from src.components.bar_chart import BarChart


def render() -> None:
    st.markdown(
        f"""<h1 style="
        margin-top: -3.50rem;
        margin-bottom: 0.5rem;
        text-align: center;
        ">Visão Geral</h1>""",
        unsafe_allow_html=True,
    )

    card = Card(
        title="Total de usuários",
        value=1000000,
        margin_left="0.0rem",
        margin_right="0.0rem",
        margin_bottom="0.0rem",
        margin_top="0.0rem",
    )
    card.render()

    data = [
        {
            "dimension": "Brasil",
            "category": "Credit Card",
            "value": 120,
        },
        {
            "dimension": "Brasil",
            "category": "Debit Card",
            "value": 80,
        },
        {
            "dimension": "Brasil",
            "category": "PayPal",
            "value": 150,
        },
        {"dimension": "EUA", "category": "Credit Card", "value": 200},
        {
            "dimension": "EUA",
            "category": "Debit Card",
            "value": 100,
        },
        {"dimension": "EUA", "category": "PayPal", "value": 130},
        {
            "dimension": "UK",
            "category": "Credit Card",
            "value": 180,
        },
        {
            "dimension": "UK",
            "category": "Debit Card",
            "value": 90,
        },
        {
            "dimension": "UK",
            "category": "PayPal",
            "value": 110,
        },
    ]

    df = pl.DataFrame(data)
    chart = BarChart(
        title="Total de usuários", df=df, x="dimension", y="value", group=True
    )
    chart.render()
