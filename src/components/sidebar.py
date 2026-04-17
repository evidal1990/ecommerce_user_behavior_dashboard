"""Menu lateral (option_menu) e segmentação."""

import streamlit as st
from streamlit_option_menu import option_menu

from src.config import (
    NAV_ICONS,
    NAV_LABELS,
    SEGMENT_OPTIONS,
    SIDEBAR_FS_BODY,
    SIDEBAR_FS_TITLE,
)


def _option_menu_styles() -> dict:
    return {
        "container": {
            "padding": "0!important",
            "background-color": "transparent",
            "width": "100%",
        },
        "icon": {"color": "#1d2939", "font-size": "1.1rem"},
        "nav-link": {
            "font-size": SIDEBAR_FS_BODY,
            "text-align": "left",
            "margin": "0.15rem 0",
            "padding": "0.45rem 0.55rem",
            "border-radius": "8px",
            "color": "#1d2939",
            "--hover-color": "#f0f2f6",
        },
        "nav-link-selected": {
            "background-color": "#e8eaf6",
            "color": "#1d2939",
            "font-weight": "500",
            "border": "1px solid #d1d5f0",
            "border-radius": "8px",
        },
    }


def _normalize_segment_state() -> None:
    if "segment" not in st.session_state:
        st.session_state.segment = SEGMENT_OPTIONS[0]
    seg = st.session_state.segment
    if isinstance(seg, list):
        st.session_state.segment = seg[0] if seg else SEGMENT_OPTIONS[0]
    elif seg not in SEGMENT_OPTIONS:
        st.session_state.segment = SEGMENT_OPTIONS[0]


def render_sidebar(default_index: int) -> tuple[str, str]:
    """Desenha navegação + segmentação; devolve (página_atual, segmento)."""
    with st.sidebar:
        st.markdown(
            f"<p style='font-weight:700;margin:0 0 1.75rem 0;margin-top: -2.75rem;font-size:{SIDEBAR_FS_TITLE};line-height:1.35;'>Menu</p>",
            unsafe_allow_html=True,
        )
        selected_page = option_menu(
            "",
            NAV_LABELS,
            icons=NAV_ICONS,
            menu_icon=None,
            default_index=default_index,
            orientation="vertical",
            styles=_option_menu_styles(),
            key="kpi_option_menu",
        )

    st.session_state.page = selected_page

    st.sidebar.markdown(
        f"<p style='font-weight:700;margin:1.25rem 0 1.25rem 0;font-size:{SIDEBAR_FS_TITLE};'>Segmentar por</p>",
        unsafe_allow_html=True,
    )
    _normalize_segment_state()

    segment = st.sidebar.selectbox(
        "segmentar_por",
        SEGMENT_OPTIONS,
        key="segment",
        label_visibility="collapsed",
    )
    return selected_page, segment
