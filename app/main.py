import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    with open(name, "r") as file:
        read = json.load(file)
    earned_money = 0
    matecoin_account = 0
    for dct in read:
        if dct["bought"] is not None:
            earned_money -= \
                Decimal(dct["bought"]) * Decimal(dct["matecoin_price"])
            matecoin_account += Decimal(dct["bought"])
        if dct["sold"] is not None:
            earned_money += \
                Decimal(dct["sold"]) * Decimal(dct["matecoin_price"])
            matecoin_account -= Decimal(dct["sold"])
    result = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as file_2:
        json.dump(result, file_2, indent=2)
