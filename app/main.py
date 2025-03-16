from decimal import Decimal

import json


def calculate_profit(trades_info_filename: str) -> None:
    profit = {
        "earned_money": Decimal("0.0"),
        "matecoin_account": Decimal("0.0")
    }
    with open(trades_info_filename) as file:
        trades_info_list = json.load(file)
    for trade in trades_info_list:
        if trade.get("bought"):
            profit["earned_money"] -= (
                Decimal(trade.get("bought"))
                * Decimal(trade.get("matecoin_price"))
            )
            profit["matecoin_account"] += Decimal(trade.get("bought"))
        if trade.get("sold"):
            profit["earned_money"] += (
                Decimal(trade.get("sold"))
                * Decimal(trade.get("matecoin_price"))
            )
            profit["matecoin_account"] -= Decimal(trade.get("sold"))
    profit["earned_money"] = str(profit.get("earned_money"))
    profit["matecoin_account"] = str(profit.get("matecoin_account"))
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
