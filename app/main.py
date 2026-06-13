import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        info = json.load(file)

    total_spent = Decimal("0")
    total_earned = Decimal("0")
    coins_held = Decimal("0")

    for trade in info:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            total_spent += price * bought
            coins_held += bought
        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            total_earned += price * sold
            coins_held -= sold

    earned_money = total_earned - total_spent
    matecoin_account = coins_held

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
