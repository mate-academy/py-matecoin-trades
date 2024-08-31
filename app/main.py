import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    total_earned = Decimal("0")
    coin_amount = Decimal("0")
    with open(file_name, "r") as json_trades:
        trades = json.load(json_trades)

    for trade in trades:
        if trade["bought"]:
            total_earned -= (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
            coin_amount += Decimal(trade["bought"])
        if trade["sold"]:
            total_earned += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )
            coin_amount -= Decimal(trade["sold"])

    profit = {
        "earned_money": str(total_earned),
        "matecoin_account": str(coin_amount)
    }
    with open("profit.json", "w") as profit_json:
        json.dump(profit, profit_json, indent=2)
