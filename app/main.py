import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(file_name, "r") as r_file:
        for element in json.load(r_file):
            if element["bought"] is not None:
                matecoin_account += Decimal(element["bought"])
                earned_money -= (Decimal(element["bought"])
                                 * Decimal(element["matecoin_price"]))
            if element["sold"] is not None:
                matecoin_account -= Decimal(element["sold"])
                earned_money += (Decimal(element["sold"])
                                 * Decimal(element["matecoin_price"]))

    with open("profit.json", "w") as w_file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            w_file,
            indent=2
        )
