import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades) as file:
        profit_trades = json.load(file)

        earned_money = Decimal(0)
        spent_money = Decimal(0)
        matecoin_account = Decimal(0)

        for trade in profit_trades:
            price = Decimal(trade["matecoin_price"])
            if trade["bought"] is not None:
                amount = Decimal(trade["bought"])
                matecoin_account += amount
                spent_money += amount * price
            if trade["sold"] is not None:
                amount = Decimal(trade["sold"])
                matecoin_account -= amount
                earned_money += amount * price
    result = {
        "earned_money": str(earned_money - spent_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
