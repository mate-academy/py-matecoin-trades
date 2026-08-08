import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    sold = 0
    bought = 0
    coins = 0

    with open(filename, "r") as f:
        date_coins = json.load(f)

    for transaction in date_coins:
        price = Decimal(transaction["matecoin_price"])

        if transaction["sold"]:
            sold += Decimal(transaction["sold"]) * price
            coins -= Decimal(transaction["sold"])
        if transaction["bought"]:
            bought += Decimal(transaction["bought"]) * price
            coins += Decimal(transaction["bought"])

    output = {
        "earned_money": str(sold - bought),
        "matecoin_account": str(coins)
    }

    with open("profit.json", "w") as output_file:
        json.dump(output, output_file, indent=2)
