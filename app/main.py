import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    result = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    with open(file_name, "r") as file:
        transactions = json.load(file)
        for transaction in transactions:
            if transaction["bought"]:
                result["matecoin_account"] += Decimal(transaction["bought"])
                result["earned_money"] = (
                    result["earned_money"]
                    - Decimal(transaction["bought"])
                    * Decimal(transaction["matecoin_price"])
                )
            if transaction["sold"]:
                result["matecoin_account"] -= Decimal(transaction["sold"])
                result["earned_money"] = (
                    result["earned_money"]
                    + Decimal(transaction["sold"])
                    * Decimal(transaction["matecoin_price"])
                )

    result["earned_money"] = str(result["earned_money"])
    result["matecoin_account"] = str(result["matecoin_account"])

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
