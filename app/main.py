import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        bought = Decimal(trade["bought"] or "0")
        sold = Decimal(trade["sold"] or "0")

        matecoin_account += bought - sold
        earned_money += (sold - bought) * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as out_file:
        json.dump(result, out_file, indent=2)
