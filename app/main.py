import json
from decimal import Decimal
from os import path
from pathlib import Path


def calculate_profit(trade_info: str) -> None:
    profit_path = path.join(Path(__file__).resolve().parent.parent,
                            "profit.json")
    with (open(trade_info, "r") as trade_file,
          open(profit_path, "w") as profit_file):
        earned_money = Decimal("0.0")
        matecoin_account = Decimal("0.0")
        for trade in json.load(trade_file):
            if trade["bought"]:
                earned_money -= (Decimal(trade["bought"])
                                 * Decimal(trade["matecoin_price"]))
                matecoin_account += Decimal(trade["bought"])
            if trade["sold"]:
                earned_money += (Decimal(trade["sold"])
                                 * Decimal(trade["matecoin_price"]))
                matecoin_account -= Decimal(trade["sold"])

        profits = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        json.dump(profits, profit_file, indent=2)
