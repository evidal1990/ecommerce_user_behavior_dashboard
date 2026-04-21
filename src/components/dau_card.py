from src.components.cards import Card


class DAUCard(Card):
    def __init__(
        self,
        dau_value: int,
    ) -> None:
        super().__init__(
            title="DAU Médio (em minutos)",
            value=dau_value,
            background=("linear-gradient(180deg, #3B82F6 0%, #1E40AF 100%);"),
        )
