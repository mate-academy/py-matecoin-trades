from decimal import Decimal
import json


def calculate_profit(trades_json: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(trades_json, "r") as file:
        trades = json.load(file)

    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        price = Decimal(trade["matecoin_price"])

        earned_money += (sold * price) - (bought * price)
        matecoin_account += bought - sold

    result = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as file_profit:
        json.dump(result, file_profit, indent=2)
