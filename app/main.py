from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    profit = {
        "earned_money": 0,
        "matecoin_account": 0,
    }

    with open(file_name, "r") as file:
        trades_list = json.load(file)
        for trade in trades_list:
            matecoin_price = Decimal(trade["matecoin_price"])
            if trade["bought"] is not None:
                bought = Decimal(trade["bought"])
                profit["earned_money"] -= bought * matecoin_price
                profit["matecoin_account"] += bought
            if trade["sold"] is not None:
                sold = Decimal(trade["sold"])
                profit["earned_money"] += sold * matecoin_price
                profit["matecoin_account"] -= sold
    profit = {key: str(value) for key, value in profit.items()}

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
