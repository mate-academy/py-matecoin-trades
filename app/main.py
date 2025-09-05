import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        print(trade)
        if trade["bought"] is not None:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"]))
        if trade["sold"] is not None:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"]))

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    BASE_DIR = Path(__file__).resolve().parent.parent

    with open(f"{BASE_DIR}/profit.json", "w") as f:
        json.dump(result, f, indent=2)
