import json
from decimal import Decimal


def calculate_profit(trades_json: str) -> None:
    with open(trades_json, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * matecoin_price


            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * matecoin_price

    with open("profit.json", "w") as f:
        json.dump({
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        },
            f,
            indent=2
        )
