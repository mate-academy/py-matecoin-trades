import decimal
from decimal import Decimal
import json


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as f:
        trades_list = json.load(f)

    earned_money = decimal.Decimal(0)
    matecoin_account = decimal.Decimal(0)

    for trade in trades_list:
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
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
