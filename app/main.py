import json
from decimal import Decimal
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
PROFIT = f"{BASE_DIR}/profit.json"


def calculate_profit(name_of_file: str) -> None:
    with open(name_of_file, "r") as file:
        trades = json.load(file)
    profit = {"earned_money": 0, "matecoin_account": 0}
    for trade in trades:
        if trade.get("bought", False):
            profit["matecoin_account"] += Decimal(trade["bought"])
            profit["earned_money"] -= Decimal(
                trade["bought"]
            ) * Decimal(trade["matecoin_price"])
        if trade.get("sold", False):
            profit["earned_money"] += Decimal(
                trade["sold"]
            ) * Decimal(trade["matecoin_price"])
            profit["matecoin_account"] -= Decimal(trade["sold"])
    profit["earned_money"], profit["matecoin_account"] = str(
        profit["earned_money"]
    ), str(profit["matecoin_account"])
    with open(PROFIT, "w") as file:
        json.dump(profit, file, indent=2)
