import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    sum_of_bought = 0
    sum_of_sold = 0
    earned_money = 0

    for trade in trades:
        trade_bought = Decimal(trade["bought"] or 0)
        trade_sold = Decimal(trade["sold"] or 0)
        matecoin_price = Decimal(trade["matecoin_price"] or 0)

        sum_of_bought += trade_bought
        sum_of_sold += trade_sold

        earned_money += (trade_sold * matecoin_price
                         - trade_bought * matecoin_price)

    matecoin_account = sum_of_bought - sum_of_sold
    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
