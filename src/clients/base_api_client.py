import os
import requests
import streamlit as st
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

from src.config import load_project_env


def _requests_verify() -> bool:
    return os.getenv("REQUESTS_VERIFY", "true").lower() in (
        "1",
        "true",
        "yes",
    )


def _params_key(params: dict | None) -> tuple[tuple[str, str], ...]:
    if not params:
        return ()
    return tuple(sorted((str(k), str(v)) for k, v in params.items()))


_CACHE_TTL_SECONDS = int(os.getenv("API_CACHE_TTL_SECONDS", "600"))
_HTTP_POOL_SIZE = int(os.getenv("API_HTTP_POOL_SIZE", "32"))
_HTTP_CONNECT_TIMEOUT_SECONDS = float(os.getenv("API_HTTP_CONNECT_TIMEOUT", "5"))
_HTTP_READ_TIMEOUT_SECONDS = float(os.getenv("API_HTTP_READ_TIMEOUT", "20"))
_HTTP_TOTAL_RETRIES = int(os.getenv("API_HTTP_TOTAL_RETRIES", "3"))
_HTTP_BACKOFF_FACTOR = float(os.getenv("API_HTTP_BACKOFF_FACTOR", "0.5"))


@st.cache_resource
def _http_session() -> requests.Session:
    """Shared HTTP session with connection pooling across reruns."""
    session = requests.Session()
    retry = Retry(
        total=_HTTP_TOTAL_RETRIES,
        connect=_HTTP_TOTAL_RETRIES,
        read=_HTTP_TOTAL_RETRIES,
        status=_HTTP_TOTAL_RETRIES,
        allowed_methods=frozenset({"GET"}),
        status_forcelist=(429, 500, 502, 503, 504),
        backoff_factor=_HTTP_BACKOFF_FACTOR,
        raise_on_status=False,
    )
    adapter = HTTPAdapter(
        pool_connections=_HTTP_POOL_SIZE,
        pool_maxsize=_HTTP_POOL_SIZE,
        max_retries=retry,
    )
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


@st.cache_data(ttl=_CACHE_TTL_SECONDS)
def _cached_api_get(
    api_base_url: str,
    api_key: str,
    endpoint: str,
    params_key: tuple[tuple[str, str], ...],
    verify: bool,
) -> list[dict]:
    params = dict(params_key) if params_key else {}
    segment = endpoint.strip().strip("/")
    base = api_base_url.rstrip("/")
    session = _http_session()
    response = session.get(
        f"{base}/{segment}",
        params=params,
        headers={"x-api-key": api_key},
        verify=verify,
        timeout=(_HTTP_CONNECT_TIMEOUT_SECONDS, _HTTP_READ_TIMEOUT_SECONDS),
    )
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from API: {response.status_code}")
    return response.json()


class BaseApiClient:
    """Cliente HTTP base para o backend de KPIs. Herde para expor métodos por domínio."""

    def __init__(self) -> None:
        self.api_base_url = self._api_base_url()
        self.api_key = self._api_key()
        self.headers = {
            "x-api-key": self.api_key,
        }

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
        return _cached_api_get(
            self.api_base_url,
            self.api_key,
            endpoint,
            _params_key(params),
            _requests_verify(),
        )
