import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        trades_data: list[dict] = json.load(f)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trades_data:
        if trade["bought"]:
            bought_amount = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money -= bought_amount * matecoin_price
            matecoin_account += bought_amount
        if trade["sold"]:
            sold_amount = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money += sold_amount * matecoin_price
            matecoin_account -= sold_amount

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
