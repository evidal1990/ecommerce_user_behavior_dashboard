# ecommerce_user_behavior_dashboard

## Estrutura da pasta `src`

O código da aplicação vive em **`src/`**: configuração e utilitários na raiz do pacote; **páginas** em `src/pages/`; **componentes** reutilizáveis em `src/components/`.

```
ecommerce_user_behavior_dashboard/
├── main.py                 # Entrada: config da página, orquestração (estilos → sidebar → URL → conteúdo)
├── src/
│   ├── __init__.py
│   ├── config.py           # Constantes: caminhos, título, tipografia, navegação, slugs (?page=…), segmentação
│   ├── assets.py           # Recursos estáticos (ex.: ícone do header em base64)
│   ├── styles.py           # CSS global e barra superior fixa (st.html)
│   ├── navigation.py       # Query params da URL, índice default do menu, sincronização após navegação
│   ├── components/
│   │   ├── __init__.py
│   │   └── sidebar.py      # Menu lateral (streamlit_option_menu) e select “Segmentar por”
│   └── pages/
│       ├── __init__.py
│       └── content.py      # Área principal da app (conteúdo por página / rota)
└── …
```

| Módulo | Função |
|--------|--------|
| `src/config.py` | Centraliza constantes e mapeamentos (`NAV_LABELS`, `PAGE_SLUGS`, `SEGMENT_OPTIONS`, etc.). |
| `src/assets.py` | Geração de HTML para ícones/recursos locais. |
| `src/styles.py` | Estilos injectados e cabeçalho vermelho fixo. |
| `src/navigation.py` | Rotas via `?page=<slug>` e alinhamento com o menu. |
| `src/components/sidebar.py` | Navegação e controlos da barra lateral. |
| `src/pages/content.py` | Renderização do corpo da dashboard por rota/página. |
