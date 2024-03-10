import json
from decimal import Decimal


def calculate_profit(trades_file):
    with open(trades_file, "r") as j_file:
        trades = json.load(j_file)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        if trade.get("bought") is not None:
            bought = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money -= bought * matecoin_price
            matecoin_account += bought
        if trade.get("sold") is not None:
            sold = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as j_file:
        json.dump(profit_data, j_file, indent=2)
