import json
from decimal import Decimal


def calculate_profit(name: str) -> None:

    with open(name, "r") as trades, open("profit.json", "a") as profit:
        profit_dict = {
            "earned_money": Decimal(0), "matecoin_account": Decimal(0)
        }
        for operation in json.load(trades):
            bought = (Decimal(operation.get("bought"))
                      if operation.get("bought") is not None else 0)
            sold = (
                Decimal(operation.get("sold"))
                if operation.get("sold") is not None else 0
            )
            price = (
                Decimal(operation.get("matecoin_price"))
                if operation.get("matecoin_price") is not None else 0
            )
            profit_dict["matecoin_account"] += bought - sold
            profit_dict["earned_money"] += (sold - bought) * price

        profit_dict["matecoin_account"] = (
            str(profit_dict.get("matecoin_account"))
        )
        profit_dict["earned_money"] = str(profit_dict.get("earned_money"))

        json.dump(profit_dict, profit, indent=2)
        print(profit)
