import json
from decimal import Decimal


def calculate_profit(trades) -> None:
    with open(trades, "r") as file:
        transaction_history = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for transaction in transaction_history:
        coin_price = Decimal(transaction["matecoin_price"])

        if transaction["bought"]:
            bought = Decimal(transaction["bought"])

            earned_money -= bought * coin_price
            matecoin_account += bought

        if transaction["sold"]:
            sold = Decimal(transaction["sold"])

            earned_money += sold * coin_price
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
