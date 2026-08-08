import decimal
import json


def calculate_profit(file_name: str) -> None:
    bought_coins = decimal.Decimal("0")
    sold_coins = decimal.Decimal("0")
    profit = decimal.Decimal("0")
    current_coins = decimal.Decimal("0")

    with open(file_name, "r") as file:
        data = json.load(file)

    for trade in data:
        if trade["bought"] is not None:
            bought_volume = decimal.Decimal(trade["bought"])
            bought_coins += bought_volume
            profit -= bought_volume * decimal.Decimal(trade["matecoin_price"])
            current_coins += bought_volume

        if trade["sold"] is not None:
            sold_volume = decimal.Decimal(trade["sold"])
            sold_coins += sold_volume
            profit += sold_volume * decimal.Decimal(trade["matecoin_price"])
            current_coins -= sold_volume

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(current_coins)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
