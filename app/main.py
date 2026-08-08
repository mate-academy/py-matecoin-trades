import json
from decimal import Decimal


def calculate_profit(trades: json) -> None:
    profit = 0
    wallet = 0

    with open(f"{trades}", "r") as file:
        trades = json.load(file)

        for i in range(len(trades)):

            if trades[i]["bought"]:
                profit -= Decimal(trades[i]["bought"]) * (
                    Decimal(trades[i]["matecoin_price"])
                )
                wallet += Decimal(trades[i]["bought"])

            if trades[i]["sold"]:
                profit += Decimal(trades[i]["sold"]) * (
                    Decimal(trades[i]["matecoin_price"])
                )
                wallet -= Decimal(trades[i]["sold"])

    with open("profit.json", "w") as user_wallet:
        json.dump(
            {"earned_money": str(profit), "matecoin_account": str(wallet)},
            user_wallet,
            indent=2
        )
