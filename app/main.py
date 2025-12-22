from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    matecoin_account = Decimal("0")
    profit = Decimal("0")

    for transaction in trades:
        if transaction["bought"] is not None:
            bought = Decimal(transaction["bought"])
            matecoin_price = Decimal(transaction["matecoin_price"])

            matecoin_account += bought
            profit -= bought * matecoin_price
        if transaction["sold"] is not None:
            sold = Decimal(transaction["sold"])
            matecoin_price = Decimal(transaction["matecoin_price"])

            matecoin_account -= sold
            profit += sold * matecoin_price

    result = {
        "earned_money": str(profit), "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as d:
        json.dump(result, d, indent=2)
