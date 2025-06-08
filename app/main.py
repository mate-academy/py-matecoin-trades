from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    balance, coins = 0, 0
    with open(file_name, "r") as file:
        trades = json.load(file)
        for trade in trades:
            if trade["bought"] is not None:
                balance -= (Decimal(trade["bought"])
                            * Decimal(trade["matecoin_price"]))
                coins += Decimal(trade["bought"])
            if trade["sold"] is not None:
                balance += (Decimal(trade["sold"])
                            * Decimal(trade["matecoin_price"]))
                coins -= Decimal(trade["sold"])

    with open("profit.json", "w") as file:
        data = {
            "earned_money": str(balance),
            "matecoin_account": str(coins)
        }
        json.dump(data, file, indent=4)
