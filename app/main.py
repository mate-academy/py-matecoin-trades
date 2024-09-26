import json
from decimal import Decimal


def calculate_profit(file_name):
    earned_money = 0
    matecoins = 0
    with open(file_name) as f:
        trades = json.load(f)
    for trade in trades:
        price = Decimal(trade['matecoin_price'])
        if trade["bought"]:
            earned_money -= Decimal(trade["bought"]) * price
            matecoins += Decimal(trade["bought"])
        if trade["sold"]:
            earned_money += Decimal(trade["sold"]) * price
            matecoins -= Decimal(trade["sold"])
    profit = {
        "earned_money": f"{earned_money}",
        "matecoin_account": f"{matecoins}"
    }
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
