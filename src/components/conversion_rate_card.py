from src.components.cards import Card


class ConversionRateCard(Card):
    def __init__(
        self,
        conversion_rate_value: int,
    ) -> None:
        super().__init__(
            title="Taxa de Conversão Média",
            value=conversion_rate_value,
            background=("linear-gradient(180deg, #3E8E41 0%, #256D2A 100%);"),
        )
