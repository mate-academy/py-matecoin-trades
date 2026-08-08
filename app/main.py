import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    with open(trades_file, "r") as file:
        trades = json.load(file)

    for trade in trades:
        bought = Decimal(trade["bought"]) \
            if trade["bought"] is not None else Decimal("0")
        sold = Decimal(trade["sold"]) \
            if trade["sold"] is not None else Decimal("0")
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought:
            matecoin_account += bought
            earned_money -= bought * matecoin_price
        if sold:
            matecoin_account -= sold
            earned_money += sold * matecoin_price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as outfile:
        json.dump(result, outfile, indent=2)
