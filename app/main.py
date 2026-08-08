import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    account = Decimal("0")
    earned_money = Decimal("0")
    with open(trades) as f:
        trades_file = json.load(f)
    for trade in trades_file:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            sold_bought = Decimal(trade["bought"])
            account += sold_bought
            earned_money -= sold_bought * price
        if trade["sold"]:
            sold_amount = Decimal(trade["sold"])
            account -= sold_amount
            earned_money += sold_amount * price

    final_result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(account)
    }

    with open("profit.json", "w") as file:
        json.dump(final_result, file, indent=2)
