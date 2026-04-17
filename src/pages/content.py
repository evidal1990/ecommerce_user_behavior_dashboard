"""Conteúdo da área principal (por página)."""

import streamlit as st

from src.consts.page_enum import Page
from src.pages.overview_page import render as render_overview_page
from src.pages.descriptive_kpis_page import render as render_descriptive_kpis_page
from src.pages.behavioral_kpis_page import render as render_behavioral_kpis_page
from src.pages.operational_kpis_page import render as render_operational_kpis_page
from src.pages.strategical_kpis_page import render as render_strategical_kpis_page
from src.pages.assistant_analysis_page import render as render_assistant_analysis_page


def render_main(page: Page) -> None:
    if page == Page.VISAO_GERAL:
        render_overview_page()
    elif page == Page.KPIS_DESCRITIVOS:
        render_descriptive_kpis_page()
    elif page == Page.KPIS_COMPORTAMENTAIS:
        render_behavioral_kpis_page()
    elif page == Page.KPIS_OPERACIONAIS:
        render_operational_kpis_page()
    elif page == Page.KPIS_ESTRATEGICOS:
        render_strategical_kpis_page()
    elif page == Page.ASSISTENTE_ANALISE:
        render_assistant_analysis_page()
