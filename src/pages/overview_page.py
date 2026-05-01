from src.components import (
    MetricsApiClient,
    UserApiClient,
    OverviewCardsSection,
    OverviewGraphSection,
)


class OverviewPage:
    def __init__(self):
        self.metrics_api_client = MetricsApiClient()
        self.user_api_client = UserApiClient()

    def render(self) -> None:
        self._render_overview_cards_section()
        self._render_overview_graph_section()

    def _render_overview_cards_section(self) -> None:
        OverviewCardsSection(
            total_users_value=self.metrics_api_client.fetch_total_users(),
            conversion_rate_value=self.metrics_api_client.fetch_avg_purchase_conversion_rate(),
            churn_rate_value=self.metrics_api_client.fetch_churn_rate(),
            dau_value=self.metrics_api_client.fetch_avg_daily_session_time(),
        ).render()

    def _render_overview_graph_section(self) -> None:
        OverviewGraphSection(
            top_countries=self.user_api_client.fetch_top_countries(),
            top_product_categories=self.user_api_client.fetch_top_product_categories(),
            premium_adoption=self.user_api_client.fetch_users_by_premium_adoption(),
        ).render()
