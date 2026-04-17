"""Conteúdo da área principal (por página)."""

import streamlit as st


def render_main(page: str, _segment: str) -> None:
    st.write(page)
