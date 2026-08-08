from decimal import Decimal
import json


def calculate_profit(file_name: str) -> dict:
    with open(f"{file_name}", "r") as f:
        trades = json.load(f)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * price
        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
