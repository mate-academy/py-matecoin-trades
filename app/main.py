import json
import os
from decimal import Decimal


def calculate_profit(file_name: json) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)
    metacoins = Decimal("0")
    money = Decimal("0")
    for trade in trades:
        if trade["bought"] is not None:
            metacoins += Decimal(trade["bought"])
            money -= (Decimal(trade["bought"])
                      * Decimal(trade["matecoin_price"]))
        if trade["sold"] is not None:
            metacoins -= Decimal(trade["sold"])
            money += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
    result = {
        "earned_money": str(money),
        "matecoin_account": str(metacoins)
    }
    path = os.path.dirname(os.path.dirname(file_name))
    profit_file = os.path.join(path, "profit.json")
    with open(profit_file, "w") as file:
        json.dump(result, file, indent=2)
