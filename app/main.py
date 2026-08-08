import json
from decimal import Decimal


def calculate_profit(trades_file_path: str) -> None:
    with open(trades_file_path) as f:
        data = json.load(f)

    earned_money = Decimal("0")
    coin_balance = Decimal("0")

    for trade in data:
        if trade["bought"]:
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            coin_balance += Decimal(trade["bought"])
        if trade["sold"]:
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            coin_balance -= Decimal(trade["sold"])

    with open("profit.json", "w") as f:
        json.dump({
            "earned_money": str(earned_money),
            "matecoin_account": str(coin_balance)
        }, f, indent=2)
