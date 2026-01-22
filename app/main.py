import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade.get("bought") is not None:
            amount = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account += amount
            earned_money -= (amount * price)
        if trade.get("sold") is not None:
            amount = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account -= amount
            earned_money += (amount * price)
        with open("profit.json", "w") as profit_file:
            json.dump(
                {
                    "earned_money": str(earned_money),
                    "matecoin_account": str(matecoin_account)
                },
                profit_file,
                indent=2
            )
