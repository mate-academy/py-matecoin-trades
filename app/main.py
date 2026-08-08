import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as trades, open("profit.json", "w") as profit:
        trades_data = json.load(trades)
        earned_money = 0
        matecoin_account = 0
        for trade in trades_data:
            if trade["bought"]:
                matecoin_account += Decimal(trade["bought"])
                earned_money -= (
                    Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
                )
            if trade["sold"]:
                matecoin_account -= Decimal(trade["sold"])
                earned_money += (
                    Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
                )
        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(result, profit, indent=2)
