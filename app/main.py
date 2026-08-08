import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit_dict = {"earned_money": 0, "matecoin_account": 0}
    with open(file_name, "r") as f:
        trades = json.load(f)

    for trade in trades:

        if trade["bought"]:
            profit_dict["earned_money"] -= Decimal(trade["bought"]) * Decimal(
                trade["matecoin_price"]
            )
            profit_dict["matecoin_account"] += Decimal(trade["bought"])
        if trade["sold"]:
            profit_dict["earned_money"] += Decimal(trade["sold"]) * Decimal(
                trade["matecoin_price"]
            )
            profit_dict["matecoin_account"] -= Decimal(trade["sold"])
    profit_dict = {k: str(v) for k, v in profit_dict.items()}
    with open("profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2, default=str)
