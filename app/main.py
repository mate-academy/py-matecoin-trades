import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    money = Decimal("0")
    coins = Decimal("0")

    with open(trades_file) as trades_json:
        trades = json.load(trades_json)

    for trade in trades:
        if trade["bought"] is not None:
            money -= (
                    Decimal(trade["bought"]) *
                    Decimal(trade["matecoin_price"])
            )
            coins += Decimal(trade["bought"])

        if trade["sold"] is not None:
            money += (
                    Decimal(trade["sold"]) *
                    Decimal(trade["matecoin_price"])
            )
            coins -= Decimal(trade["sold"])

    with open("profit.json", "w") as profit_json:
        json.dump(
            {"earned_money": str(money), "matecoin_account": str(coins)},
            profit_json,
            indent=2,
        )
