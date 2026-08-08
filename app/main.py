import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as source_file:
        trades = json.load(source_file)

    balance_in_usd = Decimal("0")
    balance_in_coins = Decimal("0")

    for trade in trades:
        if trade["bought"]:
            balance_in_coins += Decimal(trade["bought"])
            balance_in_usd -= (Decimal(trade["bought"])
                               * Decimal(trade["matecoin_price"]))
        if trade["sold"]:
            balance_in_coins -= Decimal(trade["sold"])
            balance_in_usd += (Decimal(trade["sold"])
                               * Decimal(trade["matecoin_price"]))

    profit = {
        "earned_money": str(balance_in_usd),
        "matecoin_account": str(balance_in_coins),
    }

    with open("profit.json", "w") as destination_file:
        json.dump(profit, destination_file, indent=2)
