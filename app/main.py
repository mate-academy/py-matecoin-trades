import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_accout = Decimal("0")

    for trade in trades:
        if trade["bought"]:
            bought_volume = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            matecoin_accout += bought_volume
            earned_money -= bought_volume * price

        if trade["sold"]:
            sold_volume = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            matecoin_accout -= sold_volume
            earned_money += sold_volume * price

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_accout),
        }

        with open("profit.json", "w") as file:
            json.dump(result, file, indent=2)
