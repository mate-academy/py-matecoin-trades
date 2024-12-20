import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        transactions = json.load(file)

    money = Decimal("0")
    matecoins = Decimal("0")

    for transaction in transactions:
        bought = Decimal(transaction["bought"] or "0")
        sold = Decimal(transaction["sold"] or "0")
        price = Decimal(transaction["matecoin_price"])

        money += sold * price
        money -= bought * price
        matecoins += bought
        matecoins -= sold

    with open("profit.json", "w") as file:
        json.dump({
            "earned_money": str(money),
            "matecoin_account": str(matecoins),
        }, file, indent=2)
