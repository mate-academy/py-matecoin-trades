import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data = json.load(file)

    sold = 0
    bought = 0
    coins = 0

    for el in data:
        price = Decimal(el["matecoin_price"])
        if el["sold"]:
            sold += Decimal(el["sold"]) * price
            coins -= Decimal(el["sold"])
        if el["bought"]:
            bought += Decimal(el["bought"]) * price
            coins += Decimal(el["bought"])

    total_profit = {
        "earned_money": str(sold - bought),
        "matecoin_account": str(coins)
    }

    with open("profit.json", "w") as file:
        json.dump(total_profit, file, indent=2)
