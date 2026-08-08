import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit_dict = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    with open(file_name, "r", encoding="utf-8") as file:
        trades = json.load(file)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            profit_dict["earned_money"] -= amount * price
            profit_dict["matecoin_account"] += amount

        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            profit_dict["earned_money"] += amount * price
            profit_dict["matecoin_account"] -= amount

    profit_dict["earned_money"] = str(profit_dict["earned_money"])
    profit_dict["matecoin_account"] = str(profit_dict["matecoin_account"])

    with open("profit.json", "w", encoding="utf-8") as profit_file:
        json.dump(profit_dict, profit_file, indent=2)
