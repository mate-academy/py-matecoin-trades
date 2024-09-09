import json
from decimal import Decimal
import os


def calculate_profit(file_name: str) -> None:
    profit = {"earned_money": 0, "matecoin_account": 0}
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)

    with open(file_path, "r") as f:
        trades = json.load(f)
    for act in trades:
        if act["sold"] and act["bought"]:
            profit["earned_money"] -= Decimal(
                act["bought"]) * Decimal(act["matecoin_price"])
            profit["matecoin_account"] += Decimal(act["bought"])
            profit["earned_money"] += Decimal(
                act["sold"]) * Decimal(act["matecoin_price"])
            profit["matecoin_account"] -= Decimal(act["sold"])
        if act["bought"] and not act["sold"]:
            profit["earned_money"] -= Decimal(
                act["bought"]) * Decimal(act["matecoin_price"])
            profit["matecoin_account"] += Decimal(act["bought"])
        if act["sold"] and not act["bought"]:
            profit["earned_money"] += Decimal(
                act["sold"]) * Decimal(act["matecoin_price"])
            profit["matecoin_account"] -= Decimal(act["sold"])
    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])
    with open("profit.json", "+a") as result_file:
        json.dump(profit, result_file, indent=2)


calculate_profit("trades.json")
