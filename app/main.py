from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        info = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for element in info:
        price = Decimal(element["matecoin_price"])

        bought = element["bought"]
        sold = element["sold"]

        if bought is not None:
            volume = Decimal(bought)
            earned_money -= volume * price
            matecoin_account += volume

        if sold is not None:
            volume = Decimal(sold)
            earned_money += volume * price
            matecoin_account -= volume

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as output:
        json.dump(result, output, indent=2)
