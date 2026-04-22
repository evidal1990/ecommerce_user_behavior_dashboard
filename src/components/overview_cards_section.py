import streamlit as st
from src.components.cards import Card


class OverviewCardsSection:
    def __init__(
        self,
        total_users_value: int = 0,
        conversion_rate_value: int = 0,
        churn_rate_value: int = 0,
        dau_value: int = 0,
    ):
        self.total_users_value = total_users_value
        self.conversion_rate_value = conversion_rate_value
        self.churn_rate_value = churn_rate_value
        self.dau_value = dau_value

    def render(self) -> None:
        col1, col2, col3, col4 = st.columns(4, gap="small")
        with col1:
            Card(
                title="Total de Usuários",
                value=self.total_users_value,
                background=("linear-gradient(180deg, #3A0CA3 0%, #7209B7 100%);"),
            ).render()
        with col2:
            Card(
                title="Taxa de Conversão Média",
                value=self.conversion_rate_value,
                background=("linear-gradient(180deg, #3E8E41 0%, #256D2A 100%);"),
            ).render()
        with col3:
            Card(
                title="Taxa de Churn Média",
                value=self.churn_rate_value,
                background=("linear-gradient(135deg, #E63946 0%, #9B2226 100%);"),
            ).render()
        with col4:
            Card(
                title="Tempo Médio de Sessão",
                value=self.dau_value,
                background=("linear-gradient(180deg, #3B82F6 0%, #1E40AF 100%);"),
                value_suffix=" min",
            ).render()
