import streamlit as st
from src.components.total_users_card import TotalUsersCard
from src.components.conversion_rate_card import ConversionRateCard
from src.components.churn_rate_card import ChurnRateCard
from src.components.dau_card import DAUCard


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
            TotalUsersCard(self.total_users_value).render()
        with col2:
            ConversionRateCard(self.conversion_rate_value).render()
        with col3:
            ChurnRateCard(self.churn_rate_value).render()
        with col4:
            DAUCard(self.dau_value).render()
