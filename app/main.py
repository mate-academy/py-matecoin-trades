import json
from decimal import Decimal


def calculate_profit(name_of_the_file: str) -> None:

    with open(name_of_the_file, "r") as file:
        trades = json.load(file)

    profit = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    for trade in trades:
        if trade.get("bought") is not None:
            profit["earned_money"] -= (Decimal(trade["bought"])
                                       * Decimal(trade.get("matecoin_price")))

            profit["matecoin_account"] += Decimal(trade["bought"])

        if trade.get("sold") is not None:
            profit["earned_money"] += (Decimal(trade["sold"])
                                       * Decimal(trade.get("matecoin_price")))

            profit["matecoin_account"] -= Decimal(trade["sold"])

    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
