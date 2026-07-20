import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        data = json.load(f)

        balance_coins = Decimal("0")
        earned_coins = Decimal("0")

        for trade in data:
            coins_price = Decimal(trade["matecoin_price"])

            if trade["bought"] is not None:
                bought_coins = Decimal(trade["bought"])
                earned_coins -= bought_coins * coins_price
                balance_coins += bought_coins

            if trade["sold"] is not None:
                sold_coins = Decimal(trade["sold"])
                earned_coins += sold_coins * coins_price
                balance_coins -= sold_coins

    result = {
        "earned_money": str(earned_coins),
        "matecoin_account": str(balance_coins)
    }

    with open("profit.json", "w") as p:
        json.dump(result, p, indent=2)
