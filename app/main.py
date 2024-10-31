# write your code here
import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(file_name, "r") as file:
        trades = json.load(file)

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_volume = Decimal(trade["bought"])
            matecoin_account += bought_volume
            earned_money -= bought_volume * matecoin_price

        if trade["sold"] is not None:
            sold_volume = Decimal(trade["sold"])
            matecoin_account -= sold_volume
            earned_money += sold_volume * matecoin_price

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
