import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    data_account = {
        "earned_money": Decimal("0.00"),
        "matecoin_account": Decimal("0.00")
    }

    with open(file_name, "r") as file:
        transactions = json.load(file)

    for transaction in transactions:
        matecoin_price = Decimal(transaction["matecoin_price"])

        if transaction["bought"] is not None:
            bought = Decimal(transaction["bought"])
            data_account["matecoin_account"] += bought
            data_account["earned_money"] -= bought * matecoin_price
        if transaction["sold"] is not None:
            sold = Decimal(transaction["sold"])
            data_account["matecoin_account"] -= sold
            data_account["earned_money"] += sold * matecoin_price

    data_account["earned_money"] = str(data_account["earned_money"])
    data_account["matecoin_account"] = str(data_account["matecoin_account"])

    with open("profit.json", "w") as profit_file:
        json.dump(data_account, profit_file, indent=2)
