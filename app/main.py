import json
from decimal import Decimal as dc


def calculate_profit():
    with open("trades.json") as f:
        trades = json.load(f)
        buy = dc("0")
        sell = dc("0")
        buy_profit = dc("0")
        sell_profit = dc("0")

        for trade in trades:
            if trade["sold"]:
                sell += dc(trade["sold"])
                sell_profit += dc(trade["matecoin_price"]) * dc(trade["sold"])
            if trade["bought"]:
                buy += dc(trade["bought"])
                buy_profit += dc(trade["matecoin_price"]) * dc(trade["bought"])

        profit = {
            "earned_money": str(sell_profit - buy_profit),
            "matecoin_account": str(buy - sell)
        }

    with open("profit.json", 'w') as f:
        json.dump(profit, f, indent=2)
