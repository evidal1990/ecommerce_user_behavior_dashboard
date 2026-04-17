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
# Espaço entre o título "Navegação" e o primeiro item do rádio
_NAV_TITLE_GAP_BELOW = "1.75rem"
icon_html_header = _header_icon_img_html()

# Navegação: lista de páginas (rótulo guardado em session_state)
_NAV_PAGES: tuple[tuple[str, str], ...] = (
    ("Visão Geral", ":material/home:"),
    ("KPIs Descritivos", ":material/description:"),
    ("KPIs Comportamentais", ":material/psychology:"),
    ("KPIs Operacionais", ":material/table_chart:"),
    ("KPIs Estratégicos", ":material/military_tech:"),
)
_NAV_LABELS: list[str] = [p[0] for p in _NAV_PAGES]
_NAV_EMOJI: dict[str, str] = {
    "Visão Geral": "🏠",
    "KPIs Descritivos": "📝",
    "KPIs Comportamentais": "🧠",
    "KPIs Operacionais": "📦",
    "KPIs Estratégicos": "🎖️",
}


def _format_nav_radio_label(option: str) -> str:
    em = _NAV_EMOJI.get(option, "•")
    return f"{em}  {option}"


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
    /* Navegação: pouco espaço entre blocos */
    section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] {{
        gap: 0.35rem !important;
    }}
    section[data-testid="stSidebar"] .element-container {{
        margin: 0 !important;
        padding: 0 !important;
    }}
    /*
      st.radio em vez de st.button: o hover em <label> é nativo do browser,
      por isso funciona logo — os botões Streamlit/Base Web costumam só reagir bem ao hover
      depois de o iframe/documento receber foco (1.º clique).
    */
    section[data-testid="stSidebar"] [data-testid="stRadio"] [role="radiogroup"] {{
        gap: 0.4rem !important;
        width: 100% !important;
        font-size: {_SIDEBAR_FS_BODY} !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"] {{
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: flex-start !important;
        width: 100% !important;
        box-sizing: border-box !important;
        padding: 0.45rem 0.55rem !important;
        margin: 0 !important;
        border-radius: 6px !important;
        border: 1px solid #e0e4ec !important;
        font-weight: 500 !important;
        font-size: {_SIDEBAR_FS_BODY} !important;
        line-height: 1.35 !important;
        color: #1e3a5f !important;
        cursor: pointer !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"]:hover {{
        background-color: #f0f2f6 !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked) {{
        background-color: #e8eaf6 !important;
        border-color: #d1d5f0 !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stRadio"] label[data-baseweb="radio"]:has(input:checked):hover {{
        background-color: #dde1f5 !important;
    }}
    /* Fallback: filhos diretos do radiogroup (estrutura Base Web) */
    section[data-testid="stSidebar"] [role="radiogroup"] > label {{
        display: flex !important;
        align-items: center !important;
        justify-content: flex-start !important;
        width: 100% !important;
        box-sizing: border-box !important;
        padding: 0.45rem 0.55rem !important;
        border-radius: 6px !important;
        border: 1px solid #e0e4ec !important;
        font-size: {_SIDEBAR_FS_BODY} !important;
        line-height: 1.35 !important;
        color: #1e3a5f !important;
    }}
    section[data-testid="stSidebar"] [role="radiogroup"] > label:hover {{
        background-color: #f0f2f6 !important;
    }}
    section[data-testid="stSidebar"] [role="radiogroup"] > label:has(input:checked) {{
        background-color: #e8eaf6 !important;
        border-color: #d1d5f0 !important;
    }}
    /* Títulos "Navegação" / "Segmentar por" */
    section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:nth-child(1) [data-testid="stMarkdownContainer"] p {{
        margin: 0 0 {_NAV_TITLE_GAP_BELOW} 0 !important;
        font-size: {_SIDEBAR_FS_TITLE} !important;
        line-height: 1.35 !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stVerticalBlock"] > div:nth-child(3) [data-testid="stMarkdownContainer"] p {{
        font-size: {_SIDEBAR_FS_TITLE} !important;
        line-height: 1.35 !important;
    }}
    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {{
        line-height: 1.3 !important;
    }}
    /* Select "Segmentar por": mesmo tamanho de texto que os rádios */
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
try:
    _nav_idx = _NAV_LABELS.index(st.session_state.page)
except ValueError:
    _nav_idx = 0

page = st.sidebar.radio(
    "kpi_nav_widget",
    _NAV_LABELS,
    index=_nav_idx,
    format_func=_format_nav_radio_label,
    label_visibility="collapsed",
    key="kpi_nav_radio",
    horizontal=False,
    width="stretch",
)
st.session_state.page = page

st.sidebar.markdown(
    f"<p style='font-weight:700;margin:1.25rem 0 1.25rem 0;font-size:{_SIDEBAR_FS_TITLE};'>Segmentar por</p>",
    unsafe_allow_html=True,
)
segment = st.sidebar.selectbox(
    "segmentar_por",
    [
        "País",
        "Faixa Etária",
        "Faixa de Renda",
    ],
    index=0,
    label_visibility="collapsed",
)

st.session_state.segment = segment
