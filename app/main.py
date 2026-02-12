import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade.get("bought") is not None:
            amount = Decimal(trade["bought"])
            matecoin_account += amount
            earned_money -= amount * price
        if trade.get("sold") is not None:
            amount = Decimal(trade["sold"])
            matecoin_account -= amount
            earned_money += amount * price

    profit = {
        "earned_money": str(earned_money.normalize()),
        "matecoin_account": str(matecoin_account.normalize())
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
