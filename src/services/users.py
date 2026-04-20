from src.services.api import BaseApiClient

USERS_KPI_TYPE = "users"


class UsersApiClient(BaseApiClient):
    def fetch_users_by_age_group(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "age_group"},
        )

    def fetch_users_by_annual_income(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "annual_income"},
        )

    def fetch_users_by_brand_loyalty_score(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "brand_loyalty_score"},
        )

    def fetch_users_by_coupon_usage(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "browse_to_buy_ratio"},
        )

    def fetch_users_by_cart_abandonment_rate(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "cart_abandonment_rate"},
        )

    def fetch_users_by_country(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "country"},
        )

    def fetch_users_by_device_type(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "device_type"},
        )

    def fetch_users_by_education_level(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "education_level"},
        )

    def fetch_users_by_employment_status(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "employment_status"},
        )

    def fetch_users_by_gender(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "gender"},
        )

    def fetch_users_by_has_children(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "has_children"},
        )

    def fetch_users_by_household_size(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "household_size"},
        )

    def fetch_users_by_impulse_buying_score(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "impulse_buying_score"},
        )

    def fetch_users_by_preferred_payment_method(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "preferred_payment_method"},
        )

    def fetch_users_by_preferred_payment_method_by_country(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "preferred_payment_method_by_country"},
        )

    def fetch_users_by_preferred_payment_method_by_age_group(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "preferred_payment_method_by_age_group"},
        )

    def fetch_users_by_preferred_payment_method_by_annual_income(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "preferred_payment_method_by_annual_income"},
        )

    def fetch_users_by_product_category_preference(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "product_category_preference"},
        )

    def fetch_users_by_product_category_preference_by_country(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "product_category_preference_by_country"},
        )

    def fetch_users_by_product_category_preference_by_age_group(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "product_category_preference_by_age_group"},
        )

    def fetch_users_by_product_category_preference_by_annual_income(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "product_category_preference_by_annual_income"},
        )

    def fetch_users_by_premium_adoption(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "premium_adoption"},
        )

    def fetch_users_by_premium_adoption_by_country(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "premium_adoption_by_country"},
        )

    def fetch_users_by_premium_adoption_by_age_group(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "premium_adoption_by_age_group"},
        )

    def fetch_users_by_premium_adoption_by_annual_income(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "premium_adoption_by_annual_income"},
        )

    def fetch_users_by_premium_adoption_by_neighborhood(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "neighborhood"},
        )

    def fetch_users_by_referral_count(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "referral_count"},
        )

    def fetch_users_by_return_rate(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "return_rate"},
        )

    def fetch_users_by_social_media_influence_score(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "social_media_influence_score"},
        )

    def fetch_users_by_stress_from_financial_decisions_level(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "stress_from_financial_decisions_level"},
        )

    def fetch_users_by_social_sharing_frequency(self) -> list[dict]:
        return self.fetch_data(
            USERS_KPI_TYPE,
            params={"group_by": "social_sharing_frequency"},
        )
