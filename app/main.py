import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with (open(trades, "r") as trade,
          open("py-matecoin-trades/profit.json", "w") as profit):
        coins_list = json.load(trade)
        profit_dict = {
            "earned_money": 0,
            "matecoin_account": 0,
        }
        for obj in coins_list:
            if obj["bought"]:
                profit_dict["earned_money"] -= (
                    Decimal(obj["bought"]) * Decimal(obj["matecoin_price"])
                )
                profit_dict["matecoin_account"] += Decimal(obj["bought"])
            if obj["sold"]:
                profit_dict["earned_money"] += (
                    Decimal(obj["sold"]) * Decimal(obj["matecoin_price"])
                )
                profit_dict["matecoin_account"] -= Decimal(obj["sold"])

        profit_dict["earned_money"] = str(profit_dict["earned_money"])
        profit_dict["matecoin_account"] = str(profit_dict["matecoin_account"])

        json.dump(profit_dict, profit, indent=2)
