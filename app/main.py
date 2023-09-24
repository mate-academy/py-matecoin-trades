import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades = json.load(f)

    earned_money = 0
    matecoin_account = 0

    for trade in trades:
        if trade["bought"]:
            earned_money -= Decimal(trade["matecoin_price"]) * Decimal(
                trade["bought"])
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"]:
            earned_money += Decimal(trade["matecoin_price"]) * Decimal(
                trade["sold"])
            matecoin_account -= Decimal(trade["sold"])

    profit_report = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit_report, f, indent=2)
