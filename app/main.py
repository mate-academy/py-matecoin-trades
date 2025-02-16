import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        transactions = json.load(file)

    profit = 0
    mate_coins = 0
    for transaction in transactions:
        price = Decimal(transaction["matecoin_price"])
        bought = 0
        if transaction["bought"] is not None:
            bought = Decimal(transaction["bought"])
        sold = 0
        if transaction["sold"] is not None:
            sold = Decimal(transaction["sold"])

        profit -= bought * price
        profit += sold * price
        mate_coins += bought - sold

    profit = {
        "earned_money": str(profit),
        "matecoin_account": str(mate_coins)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file)
