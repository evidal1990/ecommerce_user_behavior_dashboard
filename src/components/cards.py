import streamlit as st


def format_val(value: float) -> str:
    return f"{value:.1f}".rstrip("0").rstrip(".")


SUFFIXES = [
    (1_000_000_000, "B"),
    (1_000_000, "M"),
    (1_000, "K"),
]


def format_number(value: int) -> str:
    for threshold, suffix in SUFFIXES:
        if value >= threshold:
            return f"{format_val(value / threshold)}{suffix}"
    return str(value)


class Card:
    def __init__(
        self,
        title: str,
        value: int,
        background_color: str = "white",
        margin_left: str = "-1.0rem",
        margin_right: str = "0.0rem",
        margin_bottom: str = "0.0rem",
        margin_top: str = "0.0rem",
        padding: str = "20px",
        padding_top: str = "0.0rem",
    ):
        self.title = title
        self.value = value
        self.background_color = background_color
        self.margin_left = margin_left
        self.margin_right = margin_right
        self.margin_bottom = margin_bottom
        self.margin_top = margin_top
        self.padding = padding
        self.padding_top = padding_top

    def render(self) -> None:
        st.markdown(
            f"""
            <div style="
                padding:{self.padding};
                padding-top:{self.padding_top};
                border-radius:10px;
                border:1px solid #e0e0e0;
                background-color:{self.background_color};
                text-align:left;
                margin-left:{self.margin_left};
                margin-right:{self.margin_right};
                margin-bottom:{self.margin_bottom};
                margin-top:{self.margin_top};
                max-width:220px;
            ">
            <div style="
                font-size:18px;
                font-weight:500;
                color:gray;
                text-align:center;
                margin-bottom:10px;
            ">{self.title}</div>
            <div style="
                font-size:44px;
                font-weight:bold;
                text-align:center;
                margin-bottom:10px;
            ">{format_number(self.value)}</div>
        </div>
        """,
            unsafe_allow_html=True,
        )
