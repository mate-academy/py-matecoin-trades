import json
from decimal import Decimal


def calculate_profit(trades_file: json) -> None:
    earn = 0
    matecoin_account = 0

    with open(trades_file, "r") as file:
        trades = json.load(file)
    profit_dict = {"earned_money": 0, "matecoin_account": 0}
    for trade in trades:
        if trade["bought"] is not None:
            earn -= Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            matecoin_account += Decimal(trade["bought"])

        if trade["sold"] is not None:
            earn += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            matecoin_account -= Decimal(trade["sold"])

    profit_dict["earned_money"] = str(earn)
    profit_dict["matecoin_account"] = str(matecoin_account)

    with open("profit.json", "w") as profit:
        json.dump(profit_dict, profit, indent=2)
