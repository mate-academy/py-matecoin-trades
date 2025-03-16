import json
import os.path
from decimal import Decimal
from pathlib import Path


def calculate_profit(filename: str) -> None:
    profit = {
        "earned_money": Decimal("0.0"),
        "matecoin_account": Decimal("0.0"),
    }

    with open(filename, "r") as file:
        trades = json.load(file)
        for trade in trades:
            if "bought" in trade and trade["bought"]:
                profit["matecoin_account"] += Decimal(trade["bought"])
                profit["earned_money"] -= Decimal(trade["bought"]) * Decimal(
                    trade["matecoin_price"])
            if "sold" in trade and trade["sold"]:
                profit["matecoin_account"] -= Decimal(trade["sold"])
                profit["earned_money"] += Decimal(trade["sold"]) * Decimal(
                    trade["matecoin_price"])

    profit_serializable = {
        key: (str(value) if isinstance(value, Decimal) else value)
        for key, value in profit.items()
    }

    base_dir = Path(__file__).parent.parent
    with open(os.path.join(base_dir, "profit.json"), "w") as profit_file:
        json.dump(profit_serializable, profit_file, indent=2)
