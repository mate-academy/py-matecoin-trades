import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    dolar_profit = 0
    matecoin_balance = 0

    with open(file_name, "r") as file:
        transactions_data = json.load(file)
    for transaction in transactions_data:
        if transaction["bought"]:
            matecoin_balance += Decimal(transaction["bought"])
            dolar_profit -= (Decimal(transaction["bought"])
                             * Decimal(transaction["matecoin_price"]))
        if transaction["sold"]:
            matecoin_balance -= Decimal(transaction["sold"])
            dolar_profit += (Decimal(transaction["sold"])
                             * Decimal(transaction["matecoin_price"]))

    result = {
        "earned_money": str(dolar_profit),
        "matecoin_account": str(matecoin_balance)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
