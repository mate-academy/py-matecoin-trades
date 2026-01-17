from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    if not filename.endswith(".json"):
        raise Exception(f"File {filename} does not end with .json")

    data = []

    with open(filename, encoding="utf-8") as f:
        data = json.load(f)

    result = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    for trade in data:
        price = Decimal(trade["matecoin_price"])

        if trade.get("bought"):
            bought = Decimal(trade["bought"])
            result["earned_money"] -= bought * price
            result["matecoin_account"] += bought

        if trade.get("sold"):
            sold = Decimal(trade["sold"])
            result["earned_money"] += sold * price
            result["matecoin_account"] -= sold

    output = {
        "earned_money": str(result["earned_money"]),
        "matecoin_account": str(result["matecoin_account"])
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
