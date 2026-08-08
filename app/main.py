import json
from decimal import Decimal


def calculate_profit(filename: str):
    earned_money = 0
    matecoin_account = 0
    with open(filename, "r") as f:
        trade_list = json.load(f)

    for trade in trade_list:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bougth = Decimal(trade["bought"])
            earned_money -= bougth * price
            matecoin_account += bougth
        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            earned_money += sold * price
            matecoin_account -= sold

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
