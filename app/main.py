import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as source_file:
        trades = json.load(source_file)

    total_profit = Decimal("0")
    coin_balance = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            amount_bought = Decimal(trade["bought"])

            coin_balance += amount_bought
            total_profit -= price * amount_bought

        if trade["sold"] is not None:
            amount_sold = Decimal(trade["sold"])

            coin_balance -= amount_sold
            total_profit += price * amount_sold

    result = {
        "earned_money": str(total_profit),
        "matecoin_account": str(coin_balance)
    }

    with open("profit.json", "w") as output_file:
        json.dump(result, output_file, indent=2)
