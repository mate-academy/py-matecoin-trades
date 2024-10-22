import json
from decimal import Decimal


def calculate_profit(name: str) -> None:

    money_spend = 0
    money_earn = 0
    wallet = 0

    with open(name, "r") as file:
        content = json.load(file)

    for trade in content:
        if trade["bought"]:
            money_spend += (
                Decimal(trade["bought"])
                * Decimal(trade["matecoin_price"])
            )
            wallet += Decimal(trade["bought"])

        if trade["sold"]:
            money_earn += (
                Decimal(trade["sold"])
                * Decimal(trade["matecoin_price"])
            )
            wallet -= Decimal(trade["sold"])

    result = {
        "earned_money": str(Decimal(money_earn) - Decimal(money_spend)),
        "matecoin_account": str(Decimal(wallet))
    }

    content.append(result)

    with open(
            "profit.json",
            "w"
    ) as file:
        json.dump(result, file, indent=2)
