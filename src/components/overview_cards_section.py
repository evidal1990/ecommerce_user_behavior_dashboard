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

    def _render_card(
        self,
        title: str,
        value: int,
        color1: int,
        color2: str,
        color3: str,
    ) -> None:
        Card(
            title=title,
            value=value,
            background=(f"linear-gradient({color1}deg, {color2} 0%, {color3} 100%);"),
        ).render()

    def render(self) -> None:
        col1, col2, col3, col4 = st.columns(4, gap="small")
        with col1:
            self._render_card(
                title="Total de Usuários",
                value=self.total_users_value,
                color1=180,
                color2="#3A0CA3",
                color3="#7209B7",
            )
        with col2:
            self._render_card(
                title="Taxa de Conversão Média",
                value=self.conversion_rate_value,
                color1=180,
                color2="#3E8E41",
                color3="#256D2A",
            )
        with col3:
            self._render_card(
                title="Taxa de Churn Média",
                value=self.churn_rate_value,
                color1=135,
                color2="#E63946",
                color3="#9B2226",
            )
        with col4:
            self._render_card(
                title="Tempo Médio de Sessão",
                value=self.dau_value,
                color1=180,
                color2="#3B82F6",
                color3="#1E40AF",
            )
