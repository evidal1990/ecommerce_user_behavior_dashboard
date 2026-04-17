"""Ponto de entrada: configuração da página e orquestração da UI."""

import streamlit as st

from src.assets import header_icon_img_html
from src.components.sidebar import render_sidebar
from src.config import HEADER_ICON, NAV_LABELS, PAGE_TITLE
from src.navigation import default_menu_index, sync_page_query_param
from src.pages.content import Page, render_main
from src.styles import inject_layout_styles_and_header

st.set_page_config(
    page_title=PAGE_TITLE,
    layout="wide",
    initial_sidebar_state="expanded",
)

if "page" not in st.session_state:
    st.session_state.page = NAV_LABELS[0]

inject_layout_styles_and_header(header_icon_img_html(HEADER_ICON))

default_idx = default_menu_index()
page, segment = render_sidebar(default_idx)
sync_page_query_param(page)

render_main(Page(page))
