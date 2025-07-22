import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(f"{file_name}", "r") as file:
        all_trades = json.load(file)
    my_money = Decimal("0")
    coins_left = Decimal("0")

    for trade in all_trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            my_money -= bought * price
            coins_left += bought

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            my_money += sold * price
            coins_left -= sold

    result = {
        "earned_money": str(my_money.normalize()),
        "matecoin_account": str(coins_left.normalize())
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
