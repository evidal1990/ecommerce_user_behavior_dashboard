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
        overview_cards_section = OverviewCardsSection(
            total_users_value=self._fetch_total_users(),
            conversion_rate_value=self._fetch_conversion_rate(),
            churn_rate_value=self._fetch_churn_rate(),
            dau_value=self._fetch_dau(),
        )
        overview_graph_section = OverviewGraphSection(
            top_countries=self._fetch_top_countries(),
            top_product_categories=self._fetch_top_product_categories(),
        )
        overview_cards_section.render()
        overview_graph_section.render()

    def _fetch_total_users(self) -> int:
        total_users = self.metrics_api_client.fetch_total_users()
        return total_users[0]["value"] if total_users else 0

    def _fetch_conversion_rate(self) -> int:
        conversion_rate = self.metrics_api_client.fetch_avg_purchase_conversion_rate()
        return conversion_rate[0]["value"] if conversion_rate else 0

    def _fetch_churn_rate(self) -> int:
        churn_rate = self.metrics_api_client.fetch_churn_rate()
        return churn_rate[0]["value"] if churn_rate else 0

    def _fetch_dau(self) -> int:
        dau = self.metrics_api_client.fetch_avg_daily_session_time()
        return dau[0]["value"] if dau else 0

    def _fetch_top_countries(self) -> list[dict]:
        return self.user_api_client.fetch_top_countries() or []

    def _fetch_top_product_categories(self) -> list[dict]:
        return self.user_api_client.fetch_top_product_categories() or []
