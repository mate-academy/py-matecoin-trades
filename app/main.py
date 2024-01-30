import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as read_file:
        trades = json.load(read_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        matecoin_price = Decimal(trade["matecoin_price"])

        profit = (sold - bought) * matecoin_price
        earned_money += profit
        matecoin_account -= sold - bought

    profit_result = {"earned_money": str(earned_money),
                     "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as transparent_file:
        json.dump(profit_result, transparent_file, indent=2)
