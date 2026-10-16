import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as read_file:
        trades = json.load(read_file)
    earned_money = Decimal("0")
    account_matecoin = Decimal("0")
    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            earned_money -= amount * price
            account_matecoin += amount
        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            earned_money += amount * price
            account_matecoin -= amount
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(account_matecoin)
    }

    with open("profit.json", "w") as write_file:
        json.dump(result, write_file, indent=2)
