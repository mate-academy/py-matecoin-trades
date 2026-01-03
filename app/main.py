from decimal import Decimal
import json


def calculate_profit(trade_info_file_name: str) -> None:
    with open(trade_info_file_name, "r") as trade_info_file:
        trades = json.load(trade_info_file)
    calculated_profit = {"earned_money": 0, "matecoin_account": 0}
    for trade in trades:
        if trade["bought"]:
            calculated_profit["matecoin_account"] += Decimal(trade["bought"])
            calculated_profit["earned_money"] -= (
                Decimal(trade["bought"])
                * Decimal(trade["matecoin_price"])
            )
        if trade["sold"]:
            calculated_profit["matecoin_account"] -= Decimal(trade["sold"])
            calculated_profit["earned_money"] += (
                Decimal(trade["sold"])
                * Decimal(trade["matecoin_price"])
            )
    for key, value in calculated_profit.items():
        calculated_profit[key] = str(value)
    with open("profit.json", "w") as profit_file:
        json.dump(calculated_profit, profit_file, indent=2)
