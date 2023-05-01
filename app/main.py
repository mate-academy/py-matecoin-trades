import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    matecoin = 0
    profit = 0
    for transaction in trades:
        price = Decimal(transaction["matecoin_price"])
        if transaction.get("sold") is None:
            profit -= price * Decimal(transaction["bought"])
            matecoin += Decimal(transaction["bought"])
        elif transaction.get("bought") is None:
            profit += price * Decimal(transaction["sold"])
            matecoin -= Decimal(transaction["sold"])
        else:
            profit -= price * Decimal(transaction["bought"])
            matecoin += Decimal(transaction["bought"])
            profit += price * Decimal(transaction["sold"])
            matecoin -= Decimal(transaction["sold"])

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin)
    }

    with open("profit.json", "w") as file_write:
        json.dump(result, file_write, indent=2)
