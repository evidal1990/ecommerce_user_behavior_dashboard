import streamlit as st

from src.services.transform import process_kpi
from src.services.cached_page_payloads import load_descriptive_kpis_data
from src.pages.base_page import BasePage


_SECTION_TOP_PX = 0


class DescriptiveKpisPage(BasePage):
    def __init__(self):
        super().__init__(
            container_top_px=8,
            chart_layout_height_px=350,
            bar_layout_margin={
                "l": 36.0,
                "r": 20.0,
                "t": 26.0,
                "b": 36.0,
            },
            pie_layout_margin={
                "l": 12.0,
                "r": 12.0,
                "t": 26.0,
                "b": 0.0,
            },
        )

    def render(self) -> None:
        data = load_descriptive_kpis_data()
        self._render_title("Características dos Usuários")
        self._render_personal_kpis(data)
        self._render_professional_kpis(data)
        self._render_family_kpis(data)
        self._render_housing_kpis(data)

    def _render_personal_kpis(
        self,
        data: dict[str, int],
    ) -> None:
        self._render_subtitle("Pessoais")
        self._block_spacer_px(_SECTION_TOP_PX)
        row_graph2_col1, row_graph2_col2 = st.columns(
            2,
            gap="small",
        )
        with row_graph2_col1:
            self._render_pie_chart(
                title="Distribuição de Usuários por Faixa Etária",
                df=process_kpi(data["users_by_age_group"]),
            )
        with row_graph2_col2:
            self._render_pie_chart(
                title="Distribuição de Usuários por Gênero",
                df=process_kpi(data["users_by_gender"]),
            )

    def _render_professional_kpis(
        self,
        data: dict[str, int],
    ) -> None:
        self._render_subtitle("Profissionais")
        self._block_spacer_px(_SECTION_TOP_PX)
        row_graph2_col1, row_graph2_col2 = st.columns(
            2,
            gap="small",
        )
        with row_graph2_col1:
            self._render_pie_chart(
                title="Distribuição de Usuários por Status de Emprego",
                df=process_kpi(data["users_by_employment_status"]),
            )
        with row_graph2_col2:
            self._render_pie_chart(
                title="Distribuição de Usuários por Nível de Escolaridade",
                df=process_kpi(data["users_by_education_level"]),
            )

    def _render_family_kpis(
        self,
        data: dict[str, int],
    ) -> None:
        self._render_subtitle("Familiares")
        self._block_spacer_px(_SECTION_TOP_PX)
        row_graph2_col1, row_graph2_col2 = st.columns(
            2,
            gap="small",
        )
        with row_graph2_col1:
            self._render_pie_chart(
                title="Distribuição de Usuários por Presença de Filhos",
                df=process_kpi(data["users_by_has_children"]),
            )
        with row_graph2_col2:
            self._render_pie_chart(
                title="Distribuição de Usuários por Status de Relacionamento",
                df=process_kpi(data["users_by_relationship_status"]),
            )

    def _render_housing_kpis(
        self,
        data: dict[str, int],
    ) -> None:
        self._render_subtitle("Relacionadas à Moradia")
        self._block_spacer_px(_SECTION_TOP_PX)
        row_graph2_col1, row_graph2_col2 = st.columns(
            2,
            gap="small",
        )
        with row_graph2_col1:
            self._render_pie_chart(
                title="Distribuição de Usuários por Localização Geográfica",
                df=process_kpi(data["users_by_neighborhood"]),
            )
        with row_graph2_col2:
            self._render_pie_chart(
                title="Distribuição de Usuários por Tamanho da Família",
                df=process_kpi(data["users_by_household_size"]),
            )
