"""Execução paralela de chamáveis nomeados (uso em fetch de KPIs)."""

from concurrent.futures import (
    ThreadPoolExecutor,
    as_completed,
)
from typing import Any, Callable


def run_parallel_callables(
    tasks: dict[str, Callable[[], Any]],
    max_workers: int = 8,
) -> dict[str, Any]:
    if not tasks:
        return {}

    workers = max(1, min(max_workers, len(tasks)))

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(func): key for key, func in tasks.items()}
        results: dict[str, Any] = {}
        for future in as_completed(futures):
            key = futures[future]
            try:
                results[key] = future.result()
            except Exception as e:
                results[key] = None
                print(f"Erro ao buscar {key}: {e}")
        return results
