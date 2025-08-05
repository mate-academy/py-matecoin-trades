import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            earned_money -= amount * price
            matecoin_account += amount
        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            earned_money += amount * price
            matecoin_account -= amount
    earned_money_str = str(earned_money)
    matecoin_account_str = str(matecoin_account)
    with open("profit.json", "w") as f:
        result = {"earned_money": earned_money_str,
                  "matecoin_account": matecoin_account_str}
        json.dump(result, f, indent=2)
