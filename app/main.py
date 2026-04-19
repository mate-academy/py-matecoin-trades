from decimal import Decimal
import json


def calculate_profit(trades_file: str) -> None:
    with open(trades_file) as file:
        trades_data = json.load(file)

    profit_json = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    for operation in trades_data:
        price = Decimal(operation.get("matecoin_price"))

        if operation.get("bought"):
            count = Decimal(operation.get("bought"))
            profit_json["earned_money"] -= count * price
            profit_json["matecoin_account"] += count

        if operation.get("sold"):
            count = Decimal(operation.get("sold"))
            profit_json["earned_money"] += count * price
            profit_json["matecoin_account"] -= count

    for key in profit_json:
        profit_json[key] = str(profit_json[key])

    with open("profit.json", "w") as file:
        json.dump(profit_json, file, indent=2)
