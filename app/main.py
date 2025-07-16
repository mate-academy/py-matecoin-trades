import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    trades_info = []
    profit = {
        "earned_money": 0,
        "matecoin_account": 0
    }
    with open(file_name, "r") as file:
        trades_info = json.load(file)

    for operation in trades_info:
        for key, value in operation.items():
            if key == "bought" and value:
                profit["matecoin_account"] += Decimal(value)
                profit["earned_money"] -= (
                    Decimal(value)
                    * Decimal(operation["matecoin_price"])
                )
            elif key == "sold" and value:
                profit["matecoin_account"] -= Decimal(value)
                profit["earned_money"] += (
                    Decimal(value)
                    * Decimal(operation["matecoin_price"])
                )
    profit = {key: str(value) for key, value in profit.items()}
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
