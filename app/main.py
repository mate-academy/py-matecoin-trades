import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as file:
        trades = json.load(file)

    profit = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    for trade in trades:
        print(trade)
        if trade["bought"]:
            profit["earned_money"] -= (Decimal(trade["matecoin_price"])
                                       * Decimal(trade["bought"]))

            profit["matecoin_account"] += Decimal(trade["bought"])
        if trade["sold"]:
            profit["earned_money"] += (Decimal(trade["matecoin_price"])
                                       * Decimal(trade["sold"]))

            profit["matecoin_account"] -= Decimal(trade["sold"])

    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])
    print(profit)

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
