import os.path
from dataclasses import dataclass
from decimal import Decimal
import json


@dataclass
class Profit:
    earned_money: Decimal | str
    matecoin_account: Decimal | str


def calculate_profit(trade_file: str) -> None:
    with open(trade_file, "rb") as handle:
        trade_data: list = json.load(handle)

    profit = Profit(Decimal(0.0), Decimal(0.0))
    for trade in trade_data:
        matecoin_price = Decimal(trade["matecoin_price"])

        bought = (
            Decimal(trade["bought"])
            if trade["bought"] is not None
            else Decimal(0)
        )
        sold = (
            Decimal(trade["sold"])
            if trade["sold"] is not None
            else Decimal(0)
        )

        profit.matecoin_account += bought - sold
        profit.earned_money -= matecoin_price * bought
        profit.earned_money += matecoin_price * sold

    profit.earned_money = str(profit.earned_money)
    profit.matecoin_account = str(profit.matecoin_account)
    path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "profit.json"
    )
    with open(path, "w") as handle:
        json.dump(profit.__dict__, handle, indent=2)
