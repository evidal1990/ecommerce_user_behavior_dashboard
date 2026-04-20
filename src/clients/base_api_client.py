import os
import requests
from src.config import load_project_env


class BaseApiClient:
    """Cliente HTTP base para o backend de KPIs. Herde para expor métodos por domínio."""

    def __init__(self) -> None:
        self.api_base_url = self._api_base_url()
        self.api_key = self._api_key()
        self.headers = {
            "x-api-key": self.api_key,
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.session.verify = os.getenv("REQUESTS_VERIFY", "true").lower() in (
            "1",
            "true",
            "yes",
        )

    def _api_key(self) -> str:
        load_project_env()
        api_key = os.getenv("API_KEY")
        if not api_key:
            try:
                import streamlit as st

                sec = getattr(st, "secrets", None)
                if sec is not None:
                    api_key = str(sec.get("API_KEY", "") or "") or None
            except Exception:
                pass
        if not api_key:
            raise RuntimeError(
                "API_KEY não definido. Crie .env na raiz com API_KEY=..."
            )
        return api_key

    def _api_base_url(self) -> str:
        base = (os.getenv("API_URL") or os.getenv("BASE_URL") or "").strip().rstrip("/")
        if not base:
            try:
                import streamlit as st

                sec = getattr(st, "secrets", None)
                if sec is not None:
                    base = (
                        str(sec.get("API_URL", "") or sec.get("BASE_URL", "") or "")
                        .strip()
                        .rstrip("/")
                    )
            except Exception:
                pass
        if not base:
            raise RuntimeError(
                "API_URL (ou BASE_URL) não definido. Crie .env na raiz com API_URL=https://... "
                "(ou use Secrets no Streamlit Cloud)."
            )
        return base

    def fetch_data(self, endpoint: str, params: dict | None = None) -> list[dict]:
        segment = endpoint.strip().strip("/")
        response = self.session.get(
            f"{self.api_base_url}/{segment}",
            params=params or {},
            headers=self.headers,
        )
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from API: {response.status_code}")
        return response.json()
