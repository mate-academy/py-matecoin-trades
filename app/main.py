from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        transactions = json.load(file)
        print(transactions)

        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for transaction in transactions:
            price = Decimal(transaction["matecoin_price"])
            if transaction["bought"] is not None:
                bought = Decimal(transaction["bought"])
                matecoin_account += bought
                earned_money -= bought * price

            if transaction["sold"] is not None:
                sold = Decimal(transaction["sold"])
                matecoin_account -= sold
                earned_money += price * sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
