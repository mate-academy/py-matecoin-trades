import json
from decimal import Decimal


def calculate_profit(file_json: str) -> None:
    with open(file_json, "rb") as file:
        information = json.load(file)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in information:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        matecoin_price = Decimal(trade["matecoin_price"])
        matecoin_account += bought
        matecoin_account -= sold
        earned_money -= bought * matecoin_price
        earned_money += sold * matecoin_price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    path = "/Users/khrypunov/PycharmProjects/py-matecoin-trades/profit.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
