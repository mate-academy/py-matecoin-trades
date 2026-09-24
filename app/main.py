import decimal
import json


def calculate_profit(file_name: str) -> None:
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    with open(file_name, "r") as file:
        data = json.load(file)

    for trade in data:
        price = decimal.Decimal(trade["matecoin_price"])

        if trade["bought"]:
            bought = decimal.Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * price

        if trade["sold"]:
            sold = decimal.Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * price

    wallet = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(wallet, file, indent=2)
