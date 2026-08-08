import decimal
import json
import os


def calculate_profit(trades: json) -> None:
    profit_file_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "../profit.json")
    with (open(trades, "r") as f):
        trades_list = json.load(f)
        earned_money = 0
        matecoin_account = 0
        profit = {}

        for day_operations in trades_list:
            bought = decimal.Decimal(
                day_operations["bought"]
            ) if day_operations["bought"] else 0
            sold = decimal.Decimal(
                day_operations["sold"]
            ) if day_operations["sold"] else 0

            price = decimal.Decimal(day_operations["matecoin_price"])
            earned_money += (sold * price) - (bought * price)
            matecoin_account += sold - bought
            profit["earned_money"] = str(earned_money)
            profit["matecoin_account"] = str(abs(matecoin_account))

    with open(profit_file_path, "w") as file:
        json.dump(profit, file, indent=2)
