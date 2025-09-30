from decimal import Decimal
import json
import os


DEFAULT_PROFIT_FILE = os.path.join(os.path.dirname(__file__), "..", "profit.json")

def calculate_profit(trades_file: str, profit_file: str = DEFAULT_PROFIT_FILE) -> None:
    with open(trades_file, "r") as f:
        trades = json.load(f)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade.get("bought"):
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
        if trade.get("sold"):
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))

    profit_data = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}
    with open(profit_file, "w") as file:
        json.dump(profit_data, file, indent=2)
