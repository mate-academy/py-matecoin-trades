import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(file_name, "r") as json_file:
        data = json.load(json_file)

    for trade in data:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_volume = Decimal(trade["bought"])
            matecoin_account += bought_volume
            earned_money -= bought_volume * price

        if trade["sold"] is not None:
            sold_volume = Decimal(trade["sold"])
            matecoin_account -= sold_volume
            earned_money += sold_volume * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as json_file:
        json.dump(result, json_file, indent=2)
