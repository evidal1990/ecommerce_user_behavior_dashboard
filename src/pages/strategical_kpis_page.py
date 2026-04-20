import streamlit as st
from src.clients.metrics_api_client import MetricsApiClient
from src.services.transform import process_kpi


def render() -> None:
    metrics_api_client = MetricsApiClient()

    st.markdown(
        '<h1 style="margin-top: -3.50rem; margin-bottom: 0.5rem;">KPIs Estratégicos</h1>',
        unsafe_allow_html=True,
    )

    avg_app_usage_frequency = metrics_api_client.fetch_avg_app_usage_frequency()
    avg_app_usage_frequency_df = process_kpi(avg_app_usage_frequency)
    st.write(avg_app_usage_frequency_df)
