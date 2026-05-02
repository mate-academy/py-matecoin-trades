import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0.00")
    matecoin_account = Decimal("0.00")

    for trade in trades:
        if trade["bought"] is not None:
            matecoin_account += Decimal(str(trade["bought"]))
            earned_money -= (
                Decimal(str(trade["bought"]))
                * Decimal(str(trade["matecoin_price"]))
            )
        if trade["sold"] is not None:
            matecoin_account -= Decimal(str(trade["sold"]))
            earned_money += (
                Decimal(str(trade["sold"]))
                * Decimal(str(trade["matecoin_price"]))
            )

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
