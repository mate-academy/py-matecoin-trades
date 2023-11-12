import json
from decimal import Decimal


def calculate_profit(file_name: str):
    with open(file_name, "r") as trades:
        trades_data = json.load(trades)
        matecoin_account = 0
        earned_money = 0
        for trade_data in trades_data:
            if trade_data["bought"] is not None:
                matecoin_account += Decimal(trade_data["bought"])
                earned_money -= Decimal(trade_data["bought"]) * Decimal(trade_data["matecoin_price"])
            if trade_data["sold"] is not None:
                matecoin_account -= Decimal(trade_data["sold"])
                earned_money += Decimal(trade_data["sold"]) * Decimal(trade_data["matecoin_price"])
        profit = {"earned_money": str(earned_money), "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
