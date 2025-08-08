import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as json_file:
        data = json.load(json_file)
    profit = {
        "earned_money": Decimal("0.0"),
        "matecoin_account": Decimal("0.0")
    }
    for item in data:
        difference = Decimal(item["sold"] or "0.0") - Decimal(item["bought"] or "0.0")
        profit["earned_money"] += difference * Decimal(item["matecoin_price"])
        profit["matecoin_account"] += Decimal(item["bought"] or "0.0") - Decimal(item["sold"] or "0.0")
    for key, val in profit.items():
        profit[key] = str(val)
    with open("profit.json", "w") as profit_json:
        json.dump(profit, profit_json, indent=2)
