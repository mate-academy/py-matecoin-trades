from decimal import Decimal
import json


def calculate_profit(trade_info: str) -> None:
    profit = {"earned_money": 0, "matecoin_account": 0}
    with open(trade_info, "r") as info_file:
        trades = json.load(info_file)
    for trade in trades:
        if trade["bought"]:
            profit["earned_money"] -= (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
            profit["matecoin_account"] += Decimal(trade["bought"])
        if trade["sold"]:
            profit["earned_money"] += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )
            profit["matecoin_account"] -= Decimal(trade["sold"])
    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])
    with open("profit.json", "w") as profit_info:
        json.dump(profit, profit_info, indent=2)
