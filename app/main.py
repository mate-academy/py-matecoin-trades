import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    total_earned = Decimal("0.0")
    matecoin_balance = Decimal("0.0")

    for trade in trades:
        bought = Decimal(trade["bought"] or "0.0")
        sold = Decimal(trade["sold"] or "0.0")
        price = Decimal(trade["matecoin_price"])

        matecoin_balance += bought - sold
        total_earned += sold * price - bought * price

    profit_info = {
        "earned_money": str(total_earned),
        "matecoin_account": str(matecoin_balance)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_info, file, indent=2)
