from decimal import Decimal
import json


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as f:
        trades = json.load(f)

    money = Decimal("0")
    coins = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            coins += amount
            money -= price * amount

        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            coins -= amount
            money += price * amount

    result = {
        "earned_money": str(money),
        "matecoin_account": str(coins)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
