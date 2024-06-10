import json
from decimal import Decimal


def calculate_profit(path: str) -> None:
    with open(path, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = Decimal(trade["matecoin_price"])

        if bought:
            bought = Decimal(bought)
            matecoin_account += bought
            earned_money -= bought * price
        if sold:
            sold = Decimal(sold)
            matecoin_account -= sold
            earned_money += sold * price

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=4)


# Example usage:
calculate_profit("trades.json")
