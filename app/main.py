import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    profit = 0
    account = 0
    with open(trades_file, "r") as trade:
        for amount in json.load(trade):
            if amount["bought"]:
                profit -= Decimal(amount["bought"]) * Decimal(
                    amount["matecoin_price"]
                )
                account += Decimal(amount["bought"])
            if amount["sold"]:
                profit += Decimal(amount["sold"]) * Decimal(
                    amount["matecoin_price"]
                )
                account -= Decimal(amount["sold"])
    with open(
        "C:\\Users\\Neo\\PycharmProjects\\py-matecoin-trades\\profit.json",
            "w"
    ) as profit_file:
        json.dump(
            {"earned_money": str(profit), "matecoin_account": str(account)},
            profit_file,
            indent=2,
        )
