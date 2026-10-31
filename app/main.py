import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r", encoding="utf-8") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = Decimal(trade["matecoin_price"])

        if bought is not None:
            bought_amount = Decimal(bought)
            matecoin_account += bought_amount
            earned_money -= bought_amount * price

        if sold is not None:
            sold_amount = Decimal(sold)
            matecoin_account -= sold_amount
            earned_money += sold_amount * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
