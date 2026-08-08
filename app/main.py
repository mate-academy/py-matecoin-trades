import json
from decimal import Decimal


def calculate_profit(trades_json: str) -> None:
    with open(trades_json, "r") as data:
        trades = json.load(data)

    result = {"earned_money": Decimal("0"),
              "matecoin_account": Decimal("0")}

    for transaction in trades:
        price = Decimal(transaction["matecoin_price"])
        if transaction["bought"]:
            bought = Decimal(transaction["bought"])
            result["earned_money"] -= bought * price
            result["matecoin_account"] += bought
        if transaction["sold"]:
            sold = Decimal(transaction["sold"])
            result["earned_money"] += sold * price
            result["matecoin_account"] -= sold

    result["earned_money"] = str(result["earned_money"])
    result["matecoin_account"] = str(result["matecoin_account"])

    with open("profit.json", "w") as data:
        json.dump(result, data, indent=2)
