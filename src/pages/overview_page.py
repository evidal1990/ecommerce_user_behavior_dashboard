import streamlit as st
from src.components.cards import Card


def render() -> None:
    st.markdown(
        '<h1 style="margin-top: -3.50rem; margin-bottom: 0.5rem;">Visão Geral</h1>',
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
