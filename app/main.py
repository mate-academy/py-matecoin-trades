import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = 0
    matecoin_profit = 0

    with open(file_name, "r") as file:
        trades_data = json.load(file)

    for trade in trades_data:
        if trade["bought"] is not None:
            earned_money = earned_money - (Decimal(
                trade["bought"]) * Decimal(trade["matecoin_price"]))
            matecoin_profit = matecoin_profit + Decimal(trade["bought"])
        if trade["sold"] is not None:
            earned_money = earned_money + (Decimal(
                trade["sold"]) * Decimal(trade["matecoin_price"]))
            matecoin_profit = matecoin_profit - Decimal(trade["sold"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_profit)
    }

    with open("profit.json", "w") as file:
        file.write(json.dumps(profit, indent=4))
