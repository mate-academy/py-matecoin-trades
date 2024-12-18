from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    profit = {
        "earned_money": "0",
        "matecoin_account": "0"
    }
    with open(file_name, "r") as source:
        data = json.load(source)
    for transaction in data:
        if not transaction["bought"] is None:
            profit["earned_money"] = str(
                Decimal(profit["earned_money"])
                - Decimal(transaction["bought"])
                * Decimal(transaction["matecoin_price"])
            )
            profit["matecoin_account"] = str(
                Decimal(profit["matecoin_account"])
                + Decimal(transaction["bought"])
            )
        if not transaction["sold"] is None:
            profit["earned_money"] = str(
                Decimal(profit["earned_money"])
                + Decimal(transaction["sold"])
                * Decimal(transaction["matecoin_price"])
            )
            profit["matecoin_account"] = str(
                Decimal(profit["matecoin_account"])
                - Decimal(transaction["sold"])
            )
    with open("profit.json", "w") as pofit_file:
        json.dump(profit, pofit_file, indent=2)
