import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        data = []

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for transaction in data:
        price = Decimal(transaction["matecoin_price"])

        if transaction.get("bought") is not None:
            bought_amount = Decimal(transaction["bought"])
            earned_money -= bought_amount * price
            matecoin_account += bought_amount

        if transaction.get("sold") is not None:
            sold_amount = Decimal(transaction["sold"])
            earned_money += sold_amount * price
            matecoin_account -= sold_amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as out_file:
        json.dump(result, out_file, indent=2)
