import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        trades = json.load(json_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        dec_bought = Decimal(trade["bought"]) if (
            trade)["bought"] else Decimal("0")
        dec_sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        price = Decimal(trade["matecoin_price"])

        matecoin_account += dec_bought
        matecoin_account -= dec_sold

        earned_money -= price * dec_bought
        earned_money += price * dec_sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as json_output:
        json.dump(result, json_output, indent=2)
