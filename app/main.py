import json
from decimal import Decimal


def calculate_profit(json_file):
    with open("app/trades.json", "r") as f:
        trades = json.load(f)
    matecoin_account = Decimal(0)
    earned_money = Decimal(0)
    for trade in trades:
        if trade["bought"] is not None:
            bought = \
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            earned_money -= Decimal(bought)
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"] is not None:
            sold = Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            earned_money += Decimal(sold)
            matecoin_account -= Decimal(trade["sold"])
    profit_dict = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}
    with open('profit.json', 'w') as json_file:
        json.dump(profit_dict, json_file, indent=2)
