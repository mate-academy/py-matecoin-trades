import json
from decimal import Decimal


def calculate_profit(file_name: str = "trades.json") -> None:
    result = {
        "earned_money": 0,
        "matecoin_account": 0,
    }
    with open(file_name) as operations:
        transactions = json.load(operations)
        for transaction in transactions:
            if transaction["bought"] is not None:
                result["matecoin_account"] += Decimal(transaction["bought"])
                result["earned_money"] -= (
                    Decimal(transaction["bought"])
                    * Decimal(transaction["matecoin_price"])
                )
            if transaction["sold"] is not None:
                result["matecoin_account"] -= Decimal(transaction["sold"])
                result["earned_money"] += (
                    Decimal(transaction["sold"])
                    * Decimal(transaction["matecoin_price"])
                )

    result = {
        "earned_money": str(result["earned_money"]),
        "matecoin_account": str(result["matecoin_account"]),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
