"""Sincronização do menu com query params (?page=slug)."""

import streamlit as st

from src.config import NAV_LABELS, PAGE_SLUGS, SLUG_TO_LABEL


def query_param_page_slug() -> str | None:
    v = st.query_params.get("page")
    if not v:
        return None
    return v[0] if isinstance(v, list) else str(v)


def default_menu_index() -> int:
    slug = query_param_page_slug()
    if slug and slug in SLUG_TO_LABEL:
        nav_for_index = SLUG_TO_LABEL[slug]
    else:
        nav_for_index = (
            st.session_state.page
            if st.session_state.page in NAV_LABELS
            else NAV_LABELS[0]
        )
    return NAV_LABELS.index(nav_for_index)


def sync_page_query_param(selected_page: str) -> None:
    st.query_params["page"] = PAGE_SLUGS[selected_page]
