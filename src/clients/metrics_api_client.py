from src.clients.base_api_client import BaseApiClient
from src.services.kpi_definitions import KPI_DEFINITIONS

METRICS_KPI_TYPE = "metrics"


class MetricsApiClient(BaseApiClient):
    def fetch_avg_app_usage_frequency(self) -> list[dict]:
        config = KPI_DEFINITIONS["average_app_usage_frequency"]
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": config["dimension"]},
        )

    def fetch_avg_brand_loyalty_score(self) -> list[dict]:
        config = KPI_DEFINITIONS["average_brand_loyalty_score"]
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": config["dimension"]},
        )

    def fetch_avg_coupon_usage_per_user(self) -> list[dict]:
        config = KPI_DEFINITIONS["average_coupon_usage_per_user"]
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": config["dimension"]},
        )

    def fetch_avg_cart_abandonment_rate(self) -> list[dict]:
        config = KPI_DEFINITIONS["average_cart_abandonment_rate"]
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": config["dimension"]},
        )

    def fetch_avg_daily_session_time(self) -> list[dict]:
        config = KPI_DEFINITIONS["average_daily_session_time"]
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": config["dimension"]},
        )

    def fetch_avg_product_views_per_day(self) -> list[dict]:
        config = KPI_DEFINITIONS["average_product_views_per_day"]
        return self.fetch_data(METRICS_KPI_TYPE, params={"metric": config["dimension"]})

    def fetch_avg_purchase_conversion_rate(self) -> list[dict]:
        config = KPI_DEFINITIONS["average_purchase_conversion_rate"]
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": config["dimension"]},
        )

    def fetch_avg_referral_count(self) -> list[dict]:
        config = KPI_DEFINITIONS["average_referral_count"]
        return self.fetch_data(METRICS_KPI_TYPE, params={"metric": config["dimension"]})

    def fetch_churn_rate(self) -> list[dict]:
        config = KPI_DEFINITIONS["churn_rate"]
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": config["dimension"]},
        )

    def fetch_net_promoter_score(self) -> list[dict]:
        config = KPI_DEFINITIONS["net_promoter_score"]
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": config["dimension"]},
        )

    def fetch_total_users(self) -> list[dict]:
        config = KPI_DEFINITIONS["total_users"]
        return self.fetch_data(
            METRICS_KPI_TYPE,
            params={"metric": config["dimension"]},
        )
