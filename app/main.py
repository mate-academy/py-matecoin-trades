import json
from decimal import Decimal


def calculate_profit(file_with_trades: str) -> None:
    with open(file_with_trades, "r") as file:
        trades = json.load(file)
    profit = Decimal()
    currency = Decimal()
    for operation in trades:
        if operation["sold"]:
            profit += (
                Decimal(operation["sold"])
                * Decimal(operation["matecoin_price"])
            )
            currency -= Decimal(operation["sold"])
        if operation["bought"]:
            profit -= (
                Decimal(operation["bought"])
                * Decimal(operation["matecoin_price"])
            )
            currency += Decimal(operation["bought"])
    with open("profit.json", "w") as file:
        json.dump(
            {
                "earned_money": str(profit),
                "matecoin_account": str(currency)
            },
            file,
            indent=2
        )
