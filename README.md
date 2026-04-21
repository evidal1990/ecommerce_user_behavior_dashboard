# ecommerce_user_behavior_dashboard

Dashboard Streamlit de KPIs de comportamento de utilizadores de e-commerce: dados via API, segmentação na barra lateral e várias páginas por categoria de indicadores.

## Como executar

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run main.py
```

## Configuração (`.env`)

Na **raiz do projeto** (ou no diretório de trabalho atual), pode existir um ficheiro `.env`, carregado ao arranque por `src/config.py`. Para as chamadas HTTP aos endpoints de dados, o cliente base (`src/clients/base_api_client.py`) usa variáveis de ambiente; em alternativa, no **Streamlit Cloud** pode definir as mesmas chaves em **Secrets** (`API_KEY`, `API_URL` ou `BASE_URL`).

| Variável | Descrição |
|----------|-----------|
| `API_KEY` | Chave enviada no header `x-api-key`. |
| `API_URL` ou `BASE_URL` | URL base da API (sem barra final). |
| `API_CACHE_TTL_SECONDS` | Opcional; TTL do cache Streamlit em segundos (predefinição: `600`). |
| `REQUESTS_VERIFY` | Opcional; `true`/`false` para verificação TLS com `requests` (predefinição: `true`). |

## Estrutura da pasta `src`

O código da aplicação vive em **`src/`**: configuração na raiz do pacote; **páginas** em `src/pages/` (uma por rota); **componentes** em `src/components/`; **clientes HTTP** em `src/clients/`; **lógica de KPIs e transformações** em `src/services/`; **assistente** em `src/assistant/`; utilitários em `src/utils/`; constantes partilhadas em `src/consts/`.

```
ecommerce_user_behavior_dashboard/
├── main.py                 # Entrada: config da página, orquestração (estilos → sidebar → URL → conteúdo)
├── requirements.txt
├── icons/                  # Ícones da UI (ex.: barra de cabeçalho)
├── src/
│   ├── __init__.py
│   ├── config.py           # Caminhos, título, navegação, slugs (?page=…), segmentação, carregamento de .env
│   ├── assets.py           # Recursos estáticos (ex.: ícone do header em base64)
│   ├── styles.py           # CSS global e barra superior fixa (st.html)
│   ├── navigation.py       # Query params da URL, índice default do menu, sincronização após navegação
│   ├── consts/
│   │   └── page_enum.py    # Enum `Page` alinhado com os rótulos do menu
│   ├── components/
│   │   ├── __init__.py
│   │   └── sidebar.py      # Menu lateral e select “Segmentar por”
│   ├── pages/
│   │   ├── __init__.py
│   │   ├── content.py      # Despacho: qual página renderizar consoante `Page`
│   │   ├── overview_page.py
│   │   ├── descriptive_kpis_page.py
│   │   ├── behavioral_kpis_page.py
│   │   ├── operational_kpis_page.py
│   │   ├── strategical_kpis_page.py
│   │   └── assistant_analysis_page.py
│   ├── clients/
│   │   ├── base_api_client.py
│   │   ├── user_api_client.py
│   │   └── metrics_api_client.py
│   ├── services/
│   │   ├── kpi_definitions.py
│   │   └── transform.py
│   ├── assistant/
│   │   ├── chat.py
│   │   └── prompts.py
│   └── utils/
│       └── dataframe.py
└── …
```

| Módulo / pasta | Função |
|----------------|--------|
| `src/config.py` | Constantes, `NAV_LABELS`, `PAGE_SLUGS`, `SEGMENT_OPTIONS`, carregamento de `.env`. |
| `src/assets.py` | HTML para ícones/recursos locais. |
| `src/styles.py` | Estilos injectados e cabeçalho fixo. |
| `src/navigation.py` | Rotas via `?page=<slug>` e alinhamento com o menu. |
| `src/consts/page_enum.py` | Tipo `Page` usado pelo despacho em `content.py`. |
| `src/components/sidebar.py` | Navegação lateral e segmentação. |
| `src/pages/content.py` | Encaminha para a página concreta (`overview_page`, `*_kpis_page`, etc.). |
| `src/pages/*_page.py` | Corpo de cada secção da dashboard. |
| `src/clients/` | Chamadas à API (utilizadores vs métricas) com cache e autenticação. |
| `src/services/` | Definições de KPIs e transformação de dados para gráficos/tabelas. |
| `src/assistant/` | Recursos do assistente de análise (em evolução). |
| `src/utils/` | Helpers partilhados (ex.: manipulação de DataFrames). |
