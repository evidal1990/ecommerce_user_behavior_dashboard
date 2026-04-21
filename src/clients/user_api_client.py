from src.clients.base_api_client import BaseApiClient
from src.services.kpi_definitions import KPI_DEFINITIONS

USERS_KPI_TYPE = "users"


class UserApiClient(BaseApiClient):
    def fetch_users_by_age_group(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_age_group"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_annual_income(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_annual_income"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_brand_loyalty_score(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_brand_loyalty_score"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_browse_to_buy_ratio(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_browse_to_buy_ratio"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_cart_abandonment_rate(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_cart_abandonment_rate"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_country(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_country"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_device_type(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_device_type"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_education_level(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_education_level"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_employment_status(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_employment_status"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_gender(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_gender"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_has_children(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_has_children"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_household_size(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_household_size"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_impulse_buying_score(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_impulse_buying_score"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_preferred_payment_method(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_preferred_payment_method"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_preferred_payment_method_by_country(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_preferred_payment_method_by_country"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_preferred_payment_method_by_age_group(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_preferred_payment_method_by_age_group"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_preferred_payment_method_by_annual_income(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_preferred_payment_method_by_annual_income"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_product_category_preference(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_product_category_preference"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_product_category_preference_by_country(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_product_category_preference_by_country"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_product_category_preference_by_age_group(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_product_category_preference_by_age_group"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_product_category_preference_by_annual_income(self) -> list[dict]:
        config = KPI_DEFINITIONS[
            "users_by_product_category_preference_by_annual_income"
        ]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_premium_adoption(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_premium_adoption"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_premium_adoption_by_country(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_premium_adoption_by_country"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_premium_adoption_by_age_group(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_premium_adoption_by_age_group"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_premium_adoption_by_annual_income(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_premium_adoption_by_annual_income"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_neighborhood(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_neighborhood"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_referral_count(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_referral_count"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_return_rate(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_return_rate"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_social_media_influence_score(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_social_media_influence_score"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_stress_from_financial_decisions_level(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_stress_from_financial_decisions_level"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )

    def fetch_users_by_social_sharing_frequency(self) -> list[dict]:
        config = KPI_DEFINITIONS["users_by_social_sharing_frequency"]
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": config["dimension"]},
        )
