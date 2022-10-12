import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as file:
        list_trades = json.load(file)

    bought = Decimal("0.0")
    sold = Decimal("0.0")
    amount = Decimal("0.0")

    for item in list_trades:
        if item["bought"] is not None:
            amount += Decimal(item["bought"])
            bought += Decimal(
                Decimal(item["bought"]) * Decimal(item["matecoin_price"])
            )

        if item["sold"] is not None:
            amount -= Decimal(item["sold"])
            sold += Decimal(
                Decimal(item["sold"]) * Decimal(item["matecoin_price"])
            )

    result = {
        "earned_money": str(sold - bought),
        "matecoin_account": str(amount)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
