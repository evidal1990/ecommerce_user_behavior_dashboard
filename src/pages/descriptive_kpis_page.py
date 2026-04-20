import streamlit as st
from src.clients.user_api_client import UsersApiClient


def render() -> None:
    st.markdown(
        '<h1 style="margin-top: -3.50rem; margin-bottom: 0.5rem;">KPIs Descritivos</h1>',
        unsafe_allow_html=True,
    )
    st.write(UsersApiClient().fetch_users_by_age_group())
