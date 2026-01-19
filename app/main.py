import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        coins = json.load(file)

    profit = Decimal("0")
    matecoin_account = Decimal("0")

    for coin in coins:
        operation = Decimal("0")
        if coin["bought"]:
            operation += Decimal(coin["bought"])
        if coin["sold"]:
            operation -= Decimal(coin["sold"])

        profit -= operation * Decimal(coin["matecoin_price"])
        matecoin_account += operation

    with open("profit.json", "w") as file:
        json.dump(
            {
                "earned_money": f"{profit}",
                "matecoin_account": f"{matecoin_account}"
            },
            file,
            indent=2
        )
