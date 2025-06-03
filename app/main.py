import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    total_profit = Decimal("0.0")
    matecoin_balance = Decimal("0.0")

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = Decimal(trade["matecoin_price"])

        if bought is not None:
            bought_amount = Decimal(bought)
            matecoin_balance += bought_amount
            total_profit -= bought_amount * price

        if sold is not None:
            sold_amount = Decimal(sold)
            matecoin_balance -= sold_amount
            total_profit += sold_amount * price

    result = {
        "earned_money": str(total_profit),
        "matecoin_account": str(matecoin_balance)
    }

    with open("profit.json", "w") as outfile:
        json.dump(result, outfile)
