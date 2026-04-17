import base64
from pathlib import Path

import streamlit as st

_BASE_DIR = Path(__file__).resolve().parent
_HEADER_ICON = _BASE_DIR / "icons" / "header-bar-icon.png"


def _header_icon_img_html() -> str:
    if not _HEADER_ICON.is_file():
        return ""
    b64 = base64.b64encode(_HEADER_ICON.read_bytes()).decode("ascii")
    return (
        f'<img src="data:image/png;base64,{b64}" alt="" '
        'style="height:1.75rem;width:auto;flex-shrink:0;display:block;object-fit:contain;" />'
    )


st.set_page_config(
    page_title="Dashboard de KPIs de Usuários de E-commerce",
    layout="wide",
    initial_sidebar_state="expanded",
)

_KPI_HEADER_HEIGHT = "3.5rem"
# Sidebar: títulos de secção um pouco maiores que o corpo (proporção ~1.125 : 1)
_SIDEBAR_FS_TITLE = "1.125rem"
_SIDEBAR_FS_BODY = "1rem"
# Espaço entre o título "Navegação" e o primeiro item do menu
_NAV_TITLE_GAP_BELOW = "1.75rem"
icon_html_header = _header_icon_img_html()

# Navegação: (rótulo, ícone Material)
_NAV_PAGES: tuple[tuple[str, str], ...] = (
    ("Visão Geral", ":material/home:"),
    ("KPIs Descritivos", ":material/description:"),
    ("KPIs Comportamentais", ":material/psychology:"),
    ("KPIs Operacionais", ":material/table_chart:"),
    ("KPIs Estratégicos", ":material/military_tech:"),
    ("Assistente de Análise", ":material/smart_toy:"),
)
_NAV_LABELS: list[str] = [p[0] for p in _NAV_PAGES]

if "page" not in st.session_state:
    st.session_state.page = _NAV_LABELS[0]

st.html(
    f"""
<style>
    [data-testid="stAppViewContainer"] {{
        padding-top: {_KPI_HEADER_HEIGHT} !important;
    }}
    section[data-testid="stSidebar"] .block-container {{
        padding-top: 0.75rem !important;
        padding-bottom: 0.75rem !important;
    }}
    /* Menu vertical: botões + ícones Material, alinhados à esquerda */
    section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {{
        gap: 0.25rem !important;
    }}
    section[data-testid="stSidebar"] .element-container {{
        margin: 0 !important;
        padding: 0 !important;
    }}
    section[data-testid="stSidebar"] .stButton > button {{
        justify-content: flex-start !important;
        align-items: center !important;
        text-align: left !important;
        font-weight: 500 !important;
        border-radius: 8px !important;
        min-height: 0 !important;
        height: auto !important;
        padding: 0.45rem 0.55rem !important;
        font-size: {_SIDEBAR_FS_BODY} !important;
        line-height: 1.35 !important;
        gap: 0.45rem !important;
        width: 100% !important;
    }}
    section[data-testid="stSidebar"] .stButton > button > div {{
        display: flex !important;
        justify-content: flex-start !important;
        align-items: center !important;
        width: 100% !important;
        flex-direction: row !important;
    }}
    section[data-testid="stSidebar"] .stButton > button p {{
        text-align: left !important;
        margin: 0 !important;
        color: #1d2939 !important;
    }}
    section[data-testid="stSidebar"] .stButton > button svg,
    section[data-testid="stSidebar"] .stButton > button [data-testid="stIconMaterial"] {{
        width: 1.15rem !important;
        height: 1.15rem !important;
        flex-shrink: 0 !important;
    }}
    section[data-testid="stSidebar"] .stButton > button[kind="secondary"],
    section[data-testid="stSidebar"] .stButton > button[data-testid="baseButton-secondary"] {{
        background-color: transparent !important;
        color: #1d2939 !important;
        border: 1px solid transparent !important;
    }}
    section[data-testid="stSidebar"] .stButton > button[kind="primary"],
    section[data-testid="stSidebar"] .stButton > button[data-testid="baseButton-primary"] {{
        background-color: #e8eaf6 !important;
        color: #1d2939 !important;
        border: 1px solid #d1d5f0 !important;
    }}
    section[data-testid="stSidebar"] .stButton > button[kind="primary"] p,
    section[data-testid="stSidebar"] .stButton > button[data-testid="baseButton-primary"] p {{
        color: #1d2939 !important;
    }}
    section[data-testid="stSidebar"] .stButton > button[kind="primary"] svg,
    section[data-testid="stSidebar"] .stButton > button[data-testid="baseButton-primary"] svg {{
        fill: #1d2939 !important;
        color: #1d2939 !important;
    }}
    section[data-testid="stSidebar"] .stButton:hover > button[kind="secondary"],
    section[data-testid="stSidebar"] .stButton > button[kind="secondary"]:hover,
    section[data-testid="stSidebar"] .stButton:hover > button[data-testid="baseButton-secondary"],
    section[data-testid="stSidebar"] .stButton > button[data-testid="baseButton-secondary"]:hover {{
        background-color: #f0f2f6 !important;
    }}
    section[data-testid="stSidebar"] .stButton:hover > button[kind="primary"],
    section[data-testid="stSidebar"] .stButton > button[kind="primary"]:hover,
    section[data-testid="stSidebar"] .stButton:hover > button[data-testid="baseButton-primary"],
    section[data-testid="stSidebar"] .stButton > button[data-testid="baseButton-primary"]:hover {{
        background-color: #dde1f5 !important;
    }}
    /* Separadores finos entre itens */
    section[data-testid="stSidebar"] hr {{
        margin: 0.15rem 0 !important;
        border: none !important;
        border-top: 1px solid #e8eaed !important;
    }}
    /* Títulos "Navegação" / "Segmentar por" */
    section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:nth-child(1) [data-testid="stMarkdownContainer"] p {{
        margin: 0 0 {_NAV_TITLE_GAP_BELOW} 0 !important;
        font-size: {_SIDEBAR_FS_TITLE} !important;
        line-height: 1.35 !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {{
        line-height: 1.3 !important;
    }}
    /* Select "Segmentar por": mesmo tamanho que o menu */
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] label,
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] [data-baseweb="select"] {{
        font-size: {_SIDEBAR_FS_BODY} !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] > div {{
        font-size: {_SIDEBAR_FS_BODY} !important;
        min-height: 2.5rem !important;
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
    min-height: {_KPI_HEADER_HEIGHT};
    display: flex;
    align-items: center;
    gap: 10px;
">
    {icon_html_header}
    <span>Dashboard de KPIs de Usuários de E-commerce</span>
</div>
""",
    unsafe_allow_javascript=True,
)

st.sidebar.markdown(
    f"<p style='font-weight:700;margin:0;font-size:{_SIDEBAR_FS_TITLE};'>Navegação</p>",
    unsafe_allow_html=True,
)
for i, (label, mat_icon) in enumerate(_NAV_PAGES):
    if i > 0:
        st.sidebar.divider()
    is_active = st.session_state.page == label
    if st.sidebar.button(
        label,
        key=f"kpi_nav_{i}",
        icon=mat_icon,
        use_container_width=True,
        type="primary" if is_active else "secondary",
    ):
        st.session_state.page = label

page = st.session_state.page

st.sidebar.markdown(
    f"<p style='font-weight:700;margin:1.25rem 0 1.25rem 0;font-size:{_SIDEBAR_FS_TITLE};'>Segmentar por</p>",
    unsafe_allow_html=True,
)
if "segment" not in st.session_state:
    st.session_state.segment = "País"
segment = st.sidebar.selectbox(
    "segmentar_por",
    [
        "País",
        "Faixa Etária",
        "Faixa de Renda",
    ],
    index=[
        "País",
        "Faixa Etária",
        "Faixa de Renda",
    ].index(st.session_state.segment),
    label_visibility="collapsed",
)

st.session_state.segment = segment
