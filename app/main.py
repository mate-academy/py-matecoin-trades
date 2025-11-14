import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        operations = json.load(file)

    income = Decimal("0")
    account = Decimal("0")

    for operation in operations:
        price = Decimal(operation["matecoin_price"])
        if operation["bought"] is not None:
            bought = Decimal(operation["bought"])
            account += bought
            income -= bought * price
        if operation["sold"] is not None:
            sold = Decimal(operation["sold"])
            account -= sold
            income += sold * price

    with open("profit.json", "w") as file:
        json.dump(
            {
                "earned_money": str(income),
                "matecoin_account": str(account)
            },
            file,
            indent=2,
        )
