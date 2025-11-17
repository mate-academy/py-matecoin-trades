from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades_list = json.load(file)

    money = Decimal("0")
    coins = Decimal("0")

    for trade in trades_list:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        price = Decimal(trade["matecoin_price"])

        money -= bought * price
        coins += bought
        money += sold * price
        coins -= sold

    result = {
        "earned_money": str(money),
        "matecoin_account": str(coins)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
