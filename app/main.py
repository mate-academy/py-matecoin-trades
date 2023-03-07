from decimal import Decimal
import json


def calculate_profit(trades_json: str) -> json:
    with open(trades_json, "r") as file:
        trades = json.load(file)
    profit_data = {"earned_money": 0, "matecoin_account": 0}
    for trade in trades:
        if trade.get("bought"):
            profit_data["earned_money"] -= (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"]))
            profit_data["matecoin_account"] += Decimal(trade["bought"])
        if trade.get("sold"):
            profit_data["earned_money"] += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"]))
            profit_data["matecoin_account"] -= Decimal(trade["sold"])
    profit_data = {key: str(value) for key, value in profit_data.items()}
    with open("profit.json", "w") as new_file:
        json.dump(profit_data, new_file, indent=2)
