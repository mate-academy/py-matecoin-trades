import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(file_name, "r") as file:
        saved_json = json.load(file)

    for json_dict in saved_json:
        price = Decimal(json_dict["matecoin_price"])
        if json_dict["bought"] is not None:
            volume = Decimal(json_dict["bought"])
            matecoin_account += volume
            earned_money -= volume * price

        if json_dict["sold"] is not None:
            volume = Decimal(json_dict["sold"])
            matecoin_account -= volume
            earned_money += volume * price

    with open("profit.json", "w") as file:
        json.dump({
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }, file, indent=2)
