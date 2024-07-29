import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:

    with open(filename, "r") as f:
        trades_data = json.load(f)

        bought = Decimal("0")
        sold = Decimal("0")
        matecoin_account = Decimal("0")

        for trade in trades_data:
            if trade["bought"]:
                bought += Decimal(trade["bought"]) * Decimal(
                    trade["matecoin_price"]
                )
                matecoin_account += Decimal(trade["bought"])
            if trade["sold"]:
                sold += Decimal(trade["sold"]) * Decimal(
                    trade["matecoin_price"]
                )
                matecoin_account -= Decimal(trade["sold"])

    profit = {
        "earned_money": str(sold - bought),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
