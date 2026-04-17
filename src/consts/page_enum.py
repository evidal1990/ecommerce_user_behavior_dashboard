from enum import Enum


class Page(str, Enum):
    """Valores iguais aos rótulos do menu (NAV_LABELS) para permitir Page(rótulo)."""

    VISAO_GERAL = "Visão Geral"
    KPIS_DESCRITIVOS = "KPIs Descritivos"
    KPIS_COMPORTAMENTAIS = "KPIs Comportamentais"
    KPIS_OPERACIONAIS = "KPIs Operacionais"
    KPIS_ESTRATEGICOS = "KPIs Estratégicos"
    ASSISTENTE_ANALISE = "Assistente de Análise"
