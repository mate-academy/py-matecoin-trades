import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    with open(file_name, "r") as source:
        trade_info = json.load(source)

    for info in trade_info:
        matecoin_price = Decimal(info["matecoin_price"])
        if bought := info["bought"]:
            profit["earned_money"] -= matecoin_price * Decimal(bought)
            profit["matecoin_account"] += Decimal(bought)

        if sold := info["sold"]:
            profit["earned_money"] += matecoin_price * Decimal(sold)
            profit["matecoin_account"] -= Decimal(sold)

    with open("profit.json", "w") as profit_file:
        json.dump(
            {key: str(value) for key, value in profit.items()},
            profit_file,
            indent=2
        )
