import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        list_of_data = json.load(file)

    amount_of_coins = Decimal(0)
    balance = Decimal(0)

    for data in list_of_data:
        if data["bought"] is not None:
            amount_of_coins += Decimal(data["bought"])
            balance -= (
                Decimal(data["bought"]) * Decimal(data["matecoin_price"])
            )

        if data["sold"] is not None:
            amount_of_coins -= Decimal(data["sold"])
            balance += (
                Decimal(data["sold"]) * Decimal(data["matecoin_price"])
            )

    result = {
        "earned_money": str(balance),
        "matecoin_account": str(amount_of_coins),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
