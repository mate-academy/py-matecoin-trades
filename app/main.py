import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as file_obj:
        trades = json.load(file_obj)

    earned_money = Decimal("0")
    matecoin_in_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"] if trade["bought"] else "0")
        sold = Decimal(trade["sold"] if trade["sold"] else "0")
        matecoin_price = Decimal(trade["matecoin_price"])

        earned_money += (sold - bought) * matecoin_price
        matecoin_in_account += bought - sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_in_account)
    }

    with open("profit.json", "w") as file_obj:
        json.dump(result, file_obj, indent=2)
