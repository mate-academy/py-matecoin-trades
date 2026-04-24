import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)

    matecoin_account = Decimal("0.0")
    earned_money = Decimal("0.0")

    for account in data:
        price = Decimal(account["matecoin_price"])

        if account["bought"] is not None:
            bought = Decimal(account["bought"])
            matecoin_account += bought
            earned_money -= (bought * price)
        if account["sold"] is not None:
            sold = Decimal(account["sold"])
            matecoin_account -= sold
            earned_money += (sold * price)

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as json_file:
        json.dump(result, json_file, indent=2)
