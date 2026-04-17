import base64
from pathlib import Path

import streamlit as st
from streamlit_option_menu import option_menu

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
icon_html_header = _header_icon_img_html()

# Navegação: ícones Bootstrap Icons (streamlit_option_menu)
_NAV_LABELS: list[str] = [
    "Visão Geral",
    "KPIs Descritivos",
    "KPIs Comportamentais",
    "KPIs Operacionais",
    "KPIs Estratégicos",
    "Assistente de Análise",
]
_NAV_ICONS: list[str] = [
    "house",
    "file-earmark-text",
    "diagram-3",
    "table",
    "award",
    "robot",
]

# Rotas na URL via query string: ?page=kpis-descritivos (Streamlit não usa path /kpis... num único ficheiro)
_PAGE_SLUGS: dict[str, str] = {
    "Visão Geral": "visao-geral",
    "KPIs Descritivos": "kpis-descritivos",
    "KPIs Comportamentais": "kpis-comportamentais",
    "KPIs Operacionais": "kpis-operacionais",
    "KPIs Estratégicos": "kpis-estrategicos",
    "Assistente de Análise": "assistente-analise",
}
_SLUG_TO_LABEL: dict[str, str] = {s: t for t, s in _PAGE_SLUGS.items()}


def _query_param_page_slug() -> str | None:
    v = st.query_params.get("page")
    if not v:
        return None
    return v[0] if isinstance(v, list) else str(v)


def _option_menu_styles() -> dict:
    return {
        "container": {
            "padding": "0!important",
            "background-color": "transparent",
            "width": "100%",
        },
        "icon": {"color": "#1d2939", "font-size": "1.1rem"},
        "nav-link": {
            "font-size": _SIDEBAR_FS_BODY,
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


_SEGMENT_OPTIONS: tuple[str, ...] = (
    "País",
    "Faixa Etária",
    "Faixa de Renda",
)

if "page" not in st.session_state:
    st.session_state.page = _NAV_LABELS[0]

st.html(
    f"""
<style>
    /* Sidebar fixa: sem colapsar pela barra lateral nem pelo controlo do cabeçalho da app */
    [data-testid="stSidebarCollapseButton"],
    [data-testid="collapsedControl"] {{
        display: none !important;
    }}
    [data-testid="stAppViewContainer"] {{
        padding-top: {_KPI_HEADER_HEIGHT} !important;
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
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] label,
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] [data-baseweb="select"] {{
        font-size: {_SIDEBAR_FS_BODY} !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] > div {{
        font-size: {_SIDEBAR_FS_BODY} !important;
        min-height: 2.5rem !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"],
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] > div {{
        cursor: pointer !important;
    }}
    /* Segmentar por: seta (chevron) mais visível ao hover */
    section[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] > div:first-child {{
        transition: background-color 0.15s ease, border-color 0.15s ease;
        border-radius: 8px;
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

slug = _query_param_page_slug()
if slug and slug in _SLUG_TO_LABEL:
    _nav_for_index = _SLUG_TO_LABEL[slug]
else:
    _nav_for_index = (
        st.session_state.page
        if st.session_state.page in _NAV_LABELS
        else _NAV_LABELS[0]
    )
_default_nav = _NAV_LABELS.index(_nav_for_index)

with st.sidebar:
    st.markdown(
        f"<p style='font-weight:700;margin:0 0 1.75rem 0;margin-top: -2.75rem;font-size:{_SIDEBAR_FS_TITLE};line-height:1.35;'>Menu</p>",
        unsafe_allow_html=True,
    )
    selected_page = option_menu(
        "",
        _NAV_LABELS,
        icons=_NAV_ICONS,
        menu_icon=None,
        default_index=_default_nav,
        orientation="vertical",
        styles=_option_menu_styles(),
        key="kpi_option_menu",
    )
st.session_state.page = selected_page
st.query_params["page"] = _PAGE_SLUGS[selected_page]
page = st.session_state.page

st.sidebar.markdown(
    f"<p style='font-weight:700;margin:1.25rem 0 1.25rem 0;font-size:{_SIDEBAR_FS_TITLE};'>Segmentar por</p>",
    unsafe_allow_html=True,
)
if "segment" not in st.session_state:
    st.session_state.segment = _SEGMENT_OPTIONS[0]
_seg = st.session_state.segment
if isinstance(_seg, list):
    st.session_state.segment = _seg[0] if _seg else _SEGMENT_OPTIONS[0]
elif _seg not in _SEGMENT_OPTIONS:
    st.session_state.segment = _SEGMENT_OPTIONS[0]

segment = st.sidebar.selectbox(
    "segmentar_por",
    _SEGMENT_OPTIONS,
    key="segment",
    label_visibility="collapsed",
)
