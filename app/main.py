import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    account = Decimal("0")
    earned_money = Decimal("0")
    with open("trades") as f:
        trades_file = json.load(f)
    for trade in trades_file:
        bought_amount = Decimal(trade["bought"])
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            account += Decimal(trade["bought"])
            earned_money -= bought_amount * price
        if trade["sold"]:
            account -= Decimal(trade["sold"])
            earned_money += bought_amount * price

    final_result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(account)
    }

    with open("profit.json", "w") as file:
        json.dump(final_result, file, indent=2)
