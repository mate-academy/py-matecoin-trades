import json
from decimal import Decimal


def calculate_profit(trades_path: str) -> None:
    with open(trades_path, "r") as file:
        trades_data = json.load(file)

    matecoin_account = (
        sum(Decimal(trade["bought"] or 0)
            + -1 * Decimal(trade["sold"] or 0)
            for trade in trades_data)
    )

    earned_money = (
        sum((-1 * Decimal(trade["bought"] or 0)
             + Decimal(trade["sold"] or 0))
            * Decimal(trade["matecoin_price"])
            for trade in trades_data)
    )

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
