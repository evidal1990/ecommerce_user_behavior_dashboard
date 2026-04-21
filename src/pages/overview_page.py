import streamlit as st
import polars as pl
from src.components.cards import Card
from src.components.bar_chart import BarChart
from src.components.pie_chart import PieChart


def render() -> None:
    card = Card(
        title="Total de usuários",
        value=1000000,
        margin_left="0.0rem",
        margin_right="0.0rem",
        margin_bottom="1.0rem",
        margin_top="-1.8rem",
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

    with st.container(border=True):
        df = pl.DataFrame(data)
        bar_chart = BarChart(
            title="Total de usuários", df=df, x="dimension", y="value", group=True
        )
        bar_chart.render()

    with st.container(border=True):
        df = pl.DataFrame(
            [
                {
                    "dimension": "Brasil",
                    "value": 120,
                },
                {
                    "dimension": "EUA",
                    "value": 200,
                },
                {
                    "dimension": "UK",
                    "value": 180,
                },
            ]
        )
        pie_chart = PieChart(title="Total de usuários", df=df, x="dimension", y="value")
        pie_chart.render()
