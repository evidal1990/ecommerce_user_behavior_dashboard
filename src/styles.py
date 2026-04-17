"""CSS global e barra superior fixa."""

import streamlit as st

from src.config import KPI_HEADER_HEIGHT, PAGE_TITLE, SIDEBAR_FS_BODY


def inject_layout_styles_and_header(icon_html: str) -> None:
    st.html(
        f"""
<style>
    [data-testid="stSidebarCollapseButton"],
    [data-testid="collapsedControl"] {{
        display: none !important;
    }}
    [data-testid="stAppViewContainer"] {{
        padding-top: {KPI_HEADER_HEIGHT} !important;
    }}
    section[data-testid="stSidebar"] .block-container {{
        padding-top: 0.75rem !important;
        padding-bottom: 0.75rem !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {{
        gap: 0.25rem !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {{
        line-height: 1.3 !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] {{
        --primary-color: #94a3b8;
    }}
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] label,
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] [data-baseweb="select"] {{
        font-size: {SIDEBAR_FS_BODY} !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] > div {{
        font-size: {SIDEBAR_FS_BODY} !important;
        min-height: 2.5rem !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"],
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] > div {{
        cursor: pointer !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] > div:first-child {{
        transition: background-color 0.15s ease, border-color 0.15s ease, box-shadow 0.15s ease;
        border-radius: 8px;
        border-color: #e8eaed !important;
        box-shadow: none !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] > div:first-child:focus,
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] > div:first-child:focus-within {{
        border-color: #d1d5db !important;
        box-shadow: 0 0 0 1px #d1d5db !important;
        outline: none !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stSelectbox"]:hover div[data-baseweb="select"] > div:first-child {{
        background-color: #f0f2f6 !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] svg {{
        transition: transform 0.15s ease, opacity 0.15s ease;
        opacity: 0.55;
    }}
    section[data-testid="stSidebar"] [data-testid="stSelectbox"]:hover div[data-baseweb="select"] svg {{
        opacity: 1;
        transform: translateY(2px);
    }}
</style>
<div style="
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    width: 100%;
    z-index: 1000020;
    box-sizing: border-box;
    background-color: #E14D55;
    color: #ffffff;
    padding: 14px 20px;
    font-size: 1.35rem;
    font-weight: 600;
    line-height: 1.4;
    min-height: {KPI_HEADER_HEIGHT};
    display: flex;
    align-items: center;
    gap: 10px;
">
    {icon_html}
    <span>{PAGE_TITLE}</span>
</div>
""",
        unsafe_allow_javascript=True,
    )
