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
        sold = Decimal(item["sold"] or "0.0")
        bought = Decimal(item["bought"] or "0.0")
        difference = sold - bought
        profit["earned_money"] += difference * Decimal(item["matecoin_price"])
        profit["matecoin_account"] += bought - sold
    for key, value in profit.items():
        profit[key] = str(value)
    with open("profit.json", "w") as profit_json:
        json.dump(profit, profit_json, indent=2)
