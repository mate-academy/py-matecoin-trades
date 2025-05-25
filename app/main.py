import json
from pathlib import Path
from decimal import Decimal

BASE_DIR = Path(__file__).resolve().parent.parent

PROFIT = f"{BASE_DIR}/profit.json"


def calculate_profit(trade_file: str) -> None:
    with (open(trade_file, "r") as f):
        trades = json.load(f)

        profit = Decimal("0.0")
        matecoin_account = Decimal("0.0")
        for trade in trades:
            if trade["bought"]:
                matecoin_account += Decimal(
                    trade["bought"]
                )
                profit -= (Decimal(trade["bought"])
                           * Decimal(trade["matecoin_price"]))
            if trade["sold"]:
                matecoin_account -= Decimal(trade["sold"])
                profit += (Decimal(trade["sold"])
                           * Decimal(trade["matecoin_price"]))

        report = {
            "earned_money": str(profit),
            "matecoin_account": str(matecoin_account)
        }

        with open(PROFIT, "w") as new_profit:
            json.dump(report, new_profit, indent=2)
