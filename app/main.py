import json
import os
from decimal import Decimal


def calculate_profit(trade: str) -> None:
    profit: dict[str, int | str] = {"earned_money": Decimal(0),
                                    "matecoin_account": Decimal(0)}
    with open(trade, "r") as file:
        load_trades = json.load(file)
        for trade in load_trades:
            if trade.get("bought"):
                profit["earned_money"] -= Decimal(
                    trade.get("bought")) * Decimal(trade.get("matecoin_price"))
                profit["matecoin_account"] += Decimal(trade.get("bought"))
            if trade.get("sold"):
                profit["earned_money"] += Decimal(trade.get("sold")) * Decimal(
                    trade.get("matecoin_price"))
                profit["matecoin_account"] -= Decimal(trade.get("sold"))
    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])
    current_directory = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(current_directory, "profit.json")
    with open(file_path, "w") as file:
        json.dump(profit, file, indent=2)
