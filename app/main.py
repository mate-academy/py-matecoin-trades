import json
from decimal import Decimal, getcontext


def calculate_profit(trades_file: str) -> None:
    """Calculate profit from Matecoin trades and save to profit.json."""
    getcontext().prec = 20  # Set precision for Decimal operations

    with open(trades_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = (
            Decimal(trade["bought"])
            if trade["bought"] is not None
            else Decimal("0")
        )
        sold = (
            Decimal(trade["sold"])
            if trade["sold"] is not None
            else Decimal("0")
        )
        price = Decimal(trade["matecoin_price"])

        matecoin_account += bought - sold
        earned_money -= bought * price
        earned_money += sold * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
