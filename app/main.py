import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trade_data = json.load(file)

        bought = Decimal("0")
        sold = Decimal("0")
        mate_account = Decimal("0")

        for trade in trade_data:
            if trade["bought"] is not None:
                bought += Decimal(trade["bought"]) * Decimal(
                    trade["matecoin_price"])
                mate_account += Decimal(trade["bought"])
            if trade["sold"] is not None:
                sold += Decimal(trade["sold"]) * Decimal(
                    trade["matecoin_price"])
                mate_account -= Decimal(trade["sold"])

    profit = {
        "earned_money": str(sold - bought),
        "matecoin_account": str(mate_account)
    }
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
