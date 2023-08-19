import json
from decimal import Decimal


def calculate_transaction(transaction: dict, result: dict) -> None:
    matecoin_price = Decimal(transaction.get("matecoin_price"))

    if transaction.get("bought"):
        bought_amount = Decimal(transaction.get("bought"))
        result["matecoin_account"] += bought_amount
        result["earned_money"] -= bought_amount * matecoin_price

    if transaction.get("sold"):
        sold_amount = Decimal(transaction.get("sold"))
        result["matecoin_account"] -= sold_amount
        result["earned_money"] += sold_amount * matecoin_price


def calculate_profit(input_file: str) -> None:
    result = {
        "earned_money": Decimal("0.0"),
        "matecoin_account": Decimal("0.0"),
    }

    with open(input_file, "r") as file:
        transactions = json.load(file)
        for transaction in transactions:
            calculate_transaction(transaction, result)

    result = {k: str(v) for k, v in result.items()}

    with open("profit.json", "w") as new_file:
        json.dump(result, new_file, indent=2)
