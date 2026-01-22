from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        if trade["bought"]:
            earned_money -= Decimal(trade["bought"]) * Decimal(
                trade["matecoin_price"])
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"]:
            earned_money += Decimal(trade["sold"]) * Decimal(
                trade["matecoin_price"])
            matecoin_account -= Decimal(trade["sold"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
