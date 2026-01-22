import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as file:
        trades = json.load(file)
    matecoin_account = Decimal(0)
    earned_money = Decimal(0)

    for trade in trades:
        if trade["bought"] is not None:
            bought_amount = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money -= bought_amount * matecoin_price
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money += sold_amount * matecoin_price
            matecoin_account -= Decimal(trade["sold"])
    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
