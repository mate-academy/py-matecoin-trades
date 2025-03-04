import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    amount, profit = Decimal("0.00"), Decimal("0.00")

    with open(file_name, "r") as file:
        trades = json.load(file)

    # making trades
    for deal in trades:
        if deal["sold"] is not None:
            amount -= Decimal(deal["sold"])
            profit += Decimal(deal["sold"]) * Decimal(deal["matecoin_price"])
        if deal["bought"] is not None:
            amount += Decimal(deal["bought"])
            profit -= Decimal(deal["bought"]) * Decimal(deal["matecoin_price"])
    result = {
        "earned_money": str(profit),
        "matecoin_account": str(amount)
    }

    # dump information
    with open("profit.json", "w") as output:
        json.dump(result, output, indent=2)

    return
