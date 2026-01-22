import json
from decimal import Decimal


def calculate_profit(name_of_file: str) -> None:
    result = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    with open(name_of_file, "r") as json_file:
        list_of_transactions = json.load(json_file)
        for transaction in list_of_transactions:
            if transaction["bought"]:
                result["earned_money"] -= (
                    Decimal(transaction["bought"])
                    * Decimal(transaction["matecoin_price"])
                )
                result["matecoin_account"] += Decimal(transaction["bought"])
            if transaction["sold"]:
                result["earned_money"] += (
                    Decimal(transaction["sold"])
                    * Decimal(transaction["matecoin_price"])
                )
                result["matecoin_account"] -= Decimal(transaction["sold"])
        result["earned_money"] = str(result["earned_money"])
        result["matecoin_account"] = str(result["matecoin_account"])

    with open("profit.json", "w") as profit_report:
        json.dump(result, profit_report, indent=2, sort_keys=True)
