import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file_name:
        trades = json.load(file_name)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            earned_money -= (Decimal(trade["bought"]) * Decimal(
                trade["matecoin_price"]))
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"] is not None:
            earned_money += (Decimal(trade["sold"]) * Decimal(
                trade["matecoin_price"]))
            matecoin_account -= Decimal(trade["sold"])

    trades_result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file_name:
        json.dump(trades_result, file_name, indent=2)
