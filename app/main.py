import json
from decimal import Decimal


def calculate_profit(path_to_trades: str) -> None  :
    with open(path_to_trades, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = Decimal(trade["matecoin_price"])

        if bought:
            amount = Decimal(bought)
            matecoin_account += amount
            earned_money -= amount * price

        if sold:
            amount = Decimal(sold)
            matecoin_account -= amount
            earned_money += amount * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
