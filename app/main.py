from decimal import Decimal
import json


def calculate_profit(name_file):
    with open(name_file, "r") as trades_file,\
         open("profit.json", "w") as profit_file:
        trades = json.load(trades_file)
        profit = {"earned_money": "0", "matecoin_account": "0"}
        for trade in trades:
            if trade["bought"] is not None:
                coin = str(Decimal(profit["matecoin_account"]) + Decimal(trade["bought"]))
                profit["matecoin_account"] = coin
                money = str(Decimal(profit["earned_money"]) - Decimal(trade["matecoin_price"]) * Decimal(trade["bought"]))
                profit["earned_money"] = money
            if trade["sold"] is not None:
                profit["matecoin_account"] = str(Decimal(profit["matecoin_account"]) - Decimal(trade["sold"]))
                profit["earned_money"] = str(Decimal(profit["earned_money"]) + Decimal(trade["matecoin_price"]) * Decimal(trade["sold"]))
        json.dump(profit, profit_file, indent=2)
