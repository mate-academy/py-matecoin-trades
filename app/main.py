import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")
    for trade in trades:
        if bought := trade["bought"]:
            matecoin_account += Decimal(bought)
            earned_money -= Decimal(bought) * Decimal(trade["matecoin_price"])
        if sold := trade["sold"]:
            matecoin_account -= Decimal(sold)
            earned_money += Decimal(sold) * Decimal(trade["matecoin_price"])

    with open("profit.json", "w") as file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            file,
            indent=2
        )
