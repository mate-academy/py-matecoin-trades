import json
from decimal import Decimal


def calculate_profit(name_of_file: str) -> None:
    with open(name_of_file, "r") as file:
        trades = json.load(file)
    coin_value = Decimal("0.0")
    final_profit = Decimal("0.0")
    for transaction in trades:
        if transaction["bought"] is not None:
            price = Decimal(transaction["matecoin_price"])
            amount = Decimal(transaction["bought"])
            coin_value += amount
            final_profit -= amount * price
        if transaction["sold"] is not None:
            price = Decimal(transaction["matecoin_price"])
            amount = Decimal(transaction["sold"])
            coin_value -= amount
            final_profit += amount * price
    total_values = {
        "earned_money": str(final_profit),
        "matecoin_account": str(coin_value)
    }
    with open("profit.json", "w") as file:
        json.dump(total_values, file, indent=2)
