from __future__ import annotations

import json
from decimal import Decimal


class Trade:
    def __init__(
            self,
            matecoin_price: Decimal,
            bought: Decimal | None = None,
            sold: Decimal = None
    ) -> None:
        self.matecoint_price = matecoin_price
        self.bought = bought
        self.sold = sold

    @classmethod
    def from_dict(cls, trade_dict: dict[str, str | None]) -> Trade:
        return cls(
            matecoin_price=Decimal(trade_dict["matecoin_price"]),
            bought=trade_dict["bought"] and Decimal(trade_dict["bought"]),
            sold=trade_dict["sold"] and Decimal(trade_dict["sold"])
        )

    @classmethod
    def from_list(
            cls,
            trades_list: list[dict[str, str | None]]
    ) -> list[Trade]:
        return [cls.from_dict(trade_dict) for trade_dict in trades_list]


class MatecoinAccount:
    def __init__(
            self,
            balance: Decimal = Decimal("0"),
            profit: Decimal = Decimal("0")
    ) -> None:
        self.balance = balance
        self.profit = profit

    def bought(self, trade: Trade) -> None:
        self.balance += trade.bought
        self.profit -= trade.bought * trade.matecoint_price

    def sold(self, trade: Trade) -> None:
        self.balance -= trade.sold
        self.profit += trade.sold * trade.matecoint_price

    @staticmethod
    def to_json(matecoin_account: MatecoinAccount) -> dict[str, str]:
        return {
            "earned_money": str(matecoin_account.profit),
            "matecoin_account": str(matecoin_account.balance)
        }


def read_trades_file(file_name: str) -> dict[str, str | None]:
    with open(file_name) as f:
        return json.load(f)


def calculate_profit(file_name: str) -> None:
    trades_list = read_trades_file(file_name)

    trades = Trade.from_list(trades_list)
    matecoin_account = MatecoinAccount()

    for trade in trades:
        if trade.bought:
            matecoin_account.bought(trade)

        if trade.sold:
            matecoin_account.sold(trade)

    with open("profit.json", "w") as profit_file:
        json.dump(
            MatecoinAccount.to_json(matecoin_account),
            profit_file,
            indent=2,
        )


if __name__ == "__main__":
    calculate_profit("trades.json")
