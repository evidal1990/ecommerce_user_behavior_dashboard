from typing import Any

# Cartesian traces show Plotly’s 2D mode bar (zoom/pan/lasso…); remove extras for Streamlit.
PLOTLY_STREAMLIT_CONFIG: dict[str, Any] = {
    "displaylogo": False,
    "scrollZoom": False,
    "modeBarButtonsToRemove": [
        "zoom2d",
        "pan2d",
        "select2d",
        "lasso2d",
        "zoomIn2d",
        "zoomOut2d",
        "autoScale2d",
        "resetScale2d",
        "toggleSpikelines",
        "hoverClosestCartesian",
        "hoverCompareCartesian",
        "hoverClosestPie",
        "v1hovermode",
        "sendDataToCloud",
    ],
}
