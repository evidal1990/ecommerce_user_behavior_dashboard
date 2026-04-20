import streamlit as st
from src.clients.metrics_api_client import MetricsApiClient

def render() -> None:
    st.markdown(
        '<h1 style="margin-top: -3.50rem; margin-bottom: 0.5rem;">KPIs Estratégicos</h1>',
        unsafe_allow_html=True,
    )

    metrics_api_client = MetricsApiClient()
    st.write(metrics_api_client.fetch_avg_app_usage_frequency())
