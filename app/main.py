import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        transaction_list = json.load(file)

    bought = sum(
        Decimal(transaction["bought"]) * Decimal(transaction["matecoin_price"])
        for transaction in transaction_list
        if transaction.get("bought")
    )

    sold = sum(
        Decimal(transaction["sold"]) * Decimal(transaction["matecoin_price"])
        for transaction in transaction_list
        if transaction.get("sold")
    )

    earned_money = sold - bought
    matecoin_account = sum(
        Decimal(transaction["bought"] or 0) - Decimal(transaction["sold"] or 0)
        for transaction in transaction_list
    )

    with open("profit.json", "w") as file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            file,
            indent=2
        )
