import streamlit as st
from src.services.users import fetch_users_by_age_group


def render() -> None:
    st.markdown(
        '<h1 style="margin-top: -3.50rem; margin-bottom: 0.5rem;">KPIs Descritivos</h1>',
        unsafe_allow_html=True,
    )
    st.write(fetch_users_by_age_group())
