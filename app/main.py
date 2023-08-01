import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file) as f:
        trades_data = json.load(f)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        if trade["sold"] is not None:
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account -= Decimal(trade["sold"])
        if trade["bought"] is not None:
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account += Decimal(trade["bought"])

    profit = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
