import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    transactions = None
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(trades) as reader:
        transactions = json.load(reader)

    for transaction in transactions:
        price = Decimal(transaction["matecoin_price"])
        if transaction["bought"] is not None:
            amount = Decimal(transaction["bought"])
            matecoin_account += amount
            earned_money -= amount * price
        if transaction["sold"] is not None:
            amount = Decimal(transaction["sold"])
            matecoin_account -= amount
            earned_money += amount * price

    with open("profit.json", "w") as writer:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            }, writer, indent=2)
