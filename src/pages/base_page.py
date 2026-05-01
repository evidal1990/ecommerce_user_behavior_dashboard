import streamlit as st
from abc import abstractmethod
from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
)


class BasePage:
    def __init__(self):
        pass

    @abstractmethod
    def render(self):
        pass

    def fetch_all(
        self,
        tasks: dict,
    ):
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = {executor.submit(func): key for key, func in tasks.items()}
            results = {}
            for future in as_completed(futures):
                key = futures[future]
                try:
                    results[key] = future.result()
                except Exception as e:
                    results[key] = None
                    print(f"Erro ao buscar {key}: {e}")
        return results

    def _block_spacer_px(self, height_px: int):
        st.markdown(
            f"""
            <div style="
                display: block;
                height: {height_px}px;
            ">
            """,
            unsafe_allow_html=True,
        )
