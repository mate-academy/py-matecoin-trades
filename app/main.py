import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as json_file:
        data = json.load(json_file)

    total_money = Decimal("0")
    total_coins = Decimal("0")

    for trade in data:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])

            total_money -= bought * price
            total_coins += bought

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])

            total_money += sold * price
            total_coins -= sold

    result = {
        "earned_money": str(total_money),
        "matecoin_account": str(total_coins)
    }

    with open("profit.json", "w") as exit_file:
        json.dump(result, exit_file, indent=2)
