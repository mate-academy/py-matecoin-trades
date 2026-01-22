from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0.00")
    matecoin_account = Decimal("0.00")

    for trade in trades:

        bought = Decimal(trade["bought"]) \
            if trade["bought"] else Decimal("0.00")

        sold = Decimal(trade["sold"]) \
            if trade["sold"] else Decimal("0.00")

        matecoin_price = Decimal(trade["matecoin_price"])

        earned_money += sold * matecoin_price - bought * matecoin_price
        matecoin_account += bought - sold

    data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(data, f, indent=2)
