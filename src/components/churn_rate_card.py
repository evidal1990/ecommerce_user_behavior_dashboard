from src.components.cards import Card


class ChurnRateCard(Card):
    def __init__(
        self,
        churn_rate_value: int,
    ) -> None:
        super().__init__(
            title="Taxa de Churn Média",
            value=churn_rate_value,
            background=("linear-gradient(135deg, #E63946 0%, #9B2226 100%);"),
        )
