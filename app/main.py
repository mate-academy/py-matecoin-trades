import json
import os
from pathlib import Path
from decimal import Decimal

BASE_DIR = Path(__file__).resolve().parent.parent


def calculate_profit(file_name: str) -> None:

    with open(os.path.join(BASE_DIR, file_name), "r") as file:
        trades = json.load(file)

    account = Decimal("0")
    value = Decimal("0")

    for trans in trades:

        price = Decimal(trans["matecoin_price"])

        if trans["bought"]:
            bought = Decimal(trans["bought"])
            account += bought
            value -= bought * price

        if trans["sold"]:
            sold = Decimal(trans["sold"])
            account -= sold
            value += sold * price

    with open(os.path.join(BASE_DIR, "profit.json"), "w") as file:
        json.dump({
            "earned_money": f"{value}",
            "matecoin_account": f"{account}"
        }, file, indent=2)
