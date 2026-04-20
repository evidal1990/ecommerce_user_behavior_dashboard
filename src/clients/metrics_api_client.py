from src.clients.base_api_client import BaseApiClient

METRICS_KPI_TYPE = "metrics"


class MetricsApiClient(BaseApiClient):
    def fetch_avg_app_usage_frequency(self) -> list[dict]:
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": "avg_app_usage_frequency"},
        )

    def fetch_avg_brand_loyalty_score(self) -> list[dict]:
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": "avg_brand_loyalty_score"},
        )

    def fetch_avg_coupon_usage_per_user(self) -> list[dict]:
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": "avg_coupon_usage_per_user"},
        )

    def fetch_avg_cart_abandonment_rate(self) -> list[dict]:
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": "avg_cart_abandonment_rate"},
        )

    def fetch_avg_daily_session_time(self) -> list[dict]:
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": "avg_daily_session_time"},
        )

    def fetch_avg_product_views_per_day(self) -> list[dict]:
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": "avg_product_views_per_day"},
        )

    def fetch_avg_purchase_conversion_rate(self) -> list[dict]:
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": "avg_purchase_conversion_rate"},
        )

    def fetch_avg_referral_count(self) -> list[dict]:
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": "avg_referral_count"},
        )

    def fetch_churn_rate(self) -> list[dict]:
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": "churn_rate"},
        )

    def fetch_net_promoter_score(self) -> list[dict]:
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": "net_promoter_score"},
        )

    def fetch_total_users(self) -> list[dict]:
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": "total_users"},
        )
