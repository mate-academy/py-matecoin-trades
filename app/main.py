from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    profit = {
        "earned_money": "0",
        "matecoin_account": "0"
    }
    with open(file_name, "r") as source:
        json_file = json.load(source)
    for trans in json_file:
        if not trans["bought"] is None:
            profit["earned_money"] = str(
                Decimal(profit["earned_money"])
                - Decimal(trans["bought"])
                * Decimal(trans["matecoin_price"])
            )
            profit["matecoin_account"] = str(
                Decimal(profit["matecoin_account"])
                + Decimal(trans["bought"])
            )
        if not trans["sold"] is None:
            profit["earned_money"] = str(
                Decimal(profit["earned_money"])
                + Decimal(trans["sold"])
                * Decimal(trans["matecoin_price"])
            )
            profit["matecoin_account"] = str(
                Decimal(profit["matecoin_account"])
                - Decimal(trans["sold"])
            )
    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
