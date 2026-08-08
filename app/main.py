import json
from decimal import Decimal


def calculate_profit(js_file: str) -> None:
    with open(js_file, "r") as file:
        data = json.load(file)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for dicti in data:
        if dicti["bought"] is not None:
            earned_money -= (
                Decimal(dicti["bought"])
                * Decimal(dicti["matecoin_price"])
            )
            matecoin_account += Decimal(dicti["bought"])

        if dicti["sold"] is not None:
            earned_money += (
                Decimal(dicti["sold"])
                * Decimal(dicti["matecoin_price"])
            )
            matecoin_account -= Decimal(dicti["sold"])
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
