import html
import streamlit as st

# Dimensões partilhadas por todos os cards.
_CARD_WIDTH = "420px"
_CARD_MIN_HEIGHT = "160px"


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
        color: str = "white",
        background: str = "black",
        margin_left: str = "-1.0rem",
        margin_right: str = "0.0rem",
        margin_bottom: str = "0.0rem",
        margin_top: str = "0.0rem",
        padding: str = "20px",
        padding_top: str = "0.0rem",
    ):
        self.title = title
        self.value = value
        self.background = background
        self.color = color
        self.margin_left = margin_left
        self.margin_right = margin_right
        self.margin_bottom = margin_bottom
        self.margin_top = margin_top
        self.padding = padding
        self.padding_top = padding_top

    def render(self) -> None:
        # Em st.columns(N) a coluna é ~1/N da página. width fixo = _CARD_WIDTH não “cresce”
        # acima da coluna; min(100%, _CARD_WIDTH) usa até _CARD_WIDTH quando a coluna é larga.
        st.markdown(
            f"""
            <div style="
                display: flex;
                justify-content: center;
            ">
                <div style="
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    text-align: center;
                    width: min(100%, {_CARD_WIDTH});
                    max-width: {_CARD_WIDTH};
                    min-width: 0;
                    min-height: {_CARD_MIN_HEIGHT};
                    background: {self.background};
                    border-radius: 10px;
                    border: 1px solid #e0e0e0;
                    padding: {self.padding};
                    padding-top: {self.padding_top};
                    margin-left: auto;
                    margin-right: auto;
                    margin-bottom: "0.0rem";
                    margin-top: "0.0rem";
                    box-sizing: border-box;
                    overflow: hidden;
                    word-break: break-word;
                ">
                    <div style="
                        font-size: 18px;
                        font-weight: 500;
                        color: {self.color};
                        text-align: center;
                        margin-bottom: 10px;
                    ">{html.escape(self.title)}</div>
                    <div style="
                        font-size: 44px;
                        color: {self.color};
                        font-weight: bold;
                        text-align: center;
                    ">{format_number(self.value)}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
