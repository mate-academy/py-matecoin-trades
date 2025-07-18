import json
from decimal import Decimal


def calculate_profit(trades_info: str) -> None:
    with open(trades_info, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        price = Decimal(trade["matecoin_price"])

        earned_money += (sold - bought) * price
        matecoin_account += bought - sold

    result = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
