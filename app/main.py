from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    earned_money = 0
    coins = 0

    with open(file_name, "r") as trades_json:
        trades = json.load(trades_json)

    for trade in trades:

        if trade["bought"]:
            earned_money -= (
                Decimal(trade["bought"])
                * Decimal(trade["matecoin_price"])
            )
            coins += Decimal(trade["bought"])

        if trade["sold"]:
            earned_money += (
                Decimal(trade["sold"])
                * Decimal(trade["matecoin_price"])
            )
            coins -= Decimal(trade["sold"])

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(coins)
    }
    with open("profit.json", "w") as profit_json:
        json.dump(result, profit_json, indent=2)
