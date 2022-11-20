import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    profit = Decimal("0")
    coins = Decimal("0")
    with open(filename, "r") as fs_trades:
        for deal in json.load(fs_trades):
            if deal["bought"]:
                coins += Decimal(deal["bought"])
                profit -= Decimal(deal["bought"]) * Decimal(
                    deal["matecoin_price"]
                )
            if deal["sold"]:
                coins -= Decimal(deal["sold"])
                profit += Decimal(deal["sold"]) * Decimal(
                    deal["matecoin_price"]
                )
    with open("profit.json", "w") as fs_profit:
        json.dump(
            {
                "earned_money": str(profit),
                "matecoin_account": str(coins),
            },
            fs_profit,
            indent=2,
        )
