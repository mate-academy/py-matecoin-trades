import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        data = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for item in data:
        if item.get("bought"):
            matecoin_account += Decimal(item["bought"])
            earned_money -= (
                Decimal(item["bought"])
                * Decimal(item["matecoin_price"])
            )

        if item.get("sold") is not None:
            matecoin_account -= Decimal(item["sold"])
            earned_money += (
                Decimal(item["sold"])
                * Decimal(item["matecoin_price"])
            )

    with open("profit.json", "w") as file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account),
            },
            file,
            indent=2,
        )
