from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:

    with open(filename, "r") as file:
        trades = json.load(file)

    earned_money: Decimal = Decimal("0")
    matecoin_account: Decimal = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            amount = Decimal(trade["bought"])
            matecoin_account += amount
            earned_money -= amount * price
        if trade["sold"]:
            amount = Decimal(trade["sold"])
            matecoin_account -= amount
            earned_money += amount * price

    result: dict[str, str] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as outfile:
        json.dump(result, outfile, indent=2)
