import json

import decimal


def calculate_profit(filename):
    with open(filename, "r") as f:
        trades = json.load(f)

    profit = {"earned_money": 0, "matecoin_account": 0}

    for trade in trades:
        matecoin_price = decimal.Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought = decimal.Decimal(trade["bought"])
            profit["matecoin_account"] += bought
            profit["earned_money"] -= bought * matecoin_price
        if trade["sold"] is not None:
            sold = decimal.Decimal(trade["sold"])
            profit["matecoin_account"] -= sold
            profit["earned_money"] += sold * matecoin_price
    for item in profit:
        profit[item] = str(profit[item])

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)

if __name__ == "__main__":
    calculate_profit("trades.json")