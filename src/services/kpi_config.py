"""Configuração por nome de KPI (agregado vs dimensão + campo de valor)."""

KPI_CONFIG = {
    "avg_app_usage_frequency": {
        "type": "aggregate",
    },
    "avg_brand_loyalty_score": {
        "type": "aggregate",
    },
    "avg_coupon_usage_per_user": {
        "type": "aggregate",
    },
    "avg_cart_abandonment_rate": {
        "type": "aggregate",
    },
    "avg_daily_session_time": {
        "type": "aggregate",
    },
    "avg_product_views_per_day": {
        "type": "aggregate",
    },
    "avg_purchase_conversion_rate": {
        "type": "aggregate",
    },
    "avg_referral_count": {
        "type": "aggregate",
    },
    "churn_rate": {
        "type": "aggregate",
    },
    "net_promoter_score": {
        "type": "aggregate",
    },
    "total_users": {
        "type": "aggregate",
    },
    "users_by_age_group": {
        "dimension": "age_group",
        "value": "total_users",
    },
    "users_by_annual_income": {
        "dimension": "annual_income",
        "value": "total_users",
    },
    "users_by_brand_loyalty_score": {
        "dimension": "brand_loyalty_score",
        "value": "total_users",
    },
    "users_by_browse_to_buy_ratio": {
        "dimension": "browse_to_buy_ratio",
        "value": "total_users",
    },
    "users_by_cart_abandonment_rate": {
        "dimension": "cart_abandonment_rate",
        "value": "total_users",
    },
    "users_by_country": {
        "dimension": "country",
        "value": "total_users",
    },
    "users_by_device_type": {
        "dimension": "device_type",
        "value": "total_users",
    },
    "users_by_education_level": {
        "dimension": "education_level",
        "value": "total_users",
    },
    "users_by_employment_status": {
        "dimension": "employment_status",
        "value": "total_users",
    },
    "users_by_gender": {
        "dimension": "gender",
        "value": "total_users",
    },
    "users_by_has_children": {
        "dimension": "has_children",
        "value": "total_users",
    },
    "users_by_household_size": {
        "dimension": "household_size",
        "value": "total_users",
    },
    "users_by_impulse_buying_score": {
        "dimension": "impulse_buying_score",
        "value": "total_users",
    },
    "users_by_prefered_payment_method": {
        "dimension": "prefered_payment_method",
        "value": "total_users",
    },
    "users_by_preferred_payment_method_and_country": {
        "dimension": "preferred_payment_method_by_country",
        "value": "total_users",
    },
    "users_by_preferred_payment_method_and_age_group": {
        "dimension": "preferred_payment_method_by_age_group",
        "value": "total_users",
    },
    "users_by_preferred_payment_method_and_annual_income": {
        "dimension": "preferred_payment_method_by_annual_income",
        "value": "total_users",
    },
    "users_by_product_category_preference": {
        "dimension": "product_category_preference",
        "value": "total_users",
    },
    "users_by_product_category_preference_and_country": {
        "dimension": "product_category_preference_by_country",
        "value": "total_users",
    },
    "users_by_product_category_preference_and_age_group": {
        "dimension": "product_category_preference_by_age_group",
        "value": "total_users",
    },
    "users_by_product_category_preference_and_annual_income": {
        "dimension": "product_category_preference_by_annual_income",
        "value": "total_users",
    },
    "users_by_premium_adoption": {
        "dimension": "premium_adoption",
        "value": "total_users",
    },
    "users_by_premium_adoption_and_country": {
        "dimension": "premium_adoption_by_country",
        "value": "total_users",
    },
    "users_by_premium_adoption_and_age_group": {
        "dimension": "premium_adoption_by_age_group",
        "value": "total_users",
    },
    "users_by_premium_adoption_and_annual_income": {
        "dimension": "premium_adoption_by_annual_income",
        "value": "total_users",
    },
    "users_by_neighborhood": {
        "dimension": "neighborhood",
        "value": "total_users",
    },
    "users_by_referral_count": {
        "dimension": "referral_count",
        "value": "total_users",
    },
    "users_by_return_rate": {
        "dimension": "return_rate",
        "value": "total_users",
    },
    "users_by_stress_from_financial_decisions": {
        "dimension": "stress_from_financial_decisions_level",
        "value": "total_users",
    },
    "users_by_sharing_frequency": {
        "dimension": "sharing_frequency",
        "value": "total_users",
    },
}
