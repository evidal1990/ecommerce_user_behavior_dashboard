from src.components.cards import Card


class TotalUsersCard(Card):
    def __init__(
        self,
        total_users_value: int,
    ) -> None:
        super().__init__(
            title="Total de Usuários",
            value=total_users_value,
            background=(
                "linear-gradient(180deg, #3A0CA3 0%, #7209B7 100%);"
            ),
        )
