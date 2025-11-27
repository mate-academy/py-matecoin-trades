import json
from decimal import Decimal


def calculate_profit(source_file: str) -> None:
    with open(source_file, "r") as json_file:
        data = json.load(json_file)

    total_money = Decimal("0.00")
    total_matecoin = Decimal("0.00")

    for deal in data:
        if deal["bought"]:
            total_matecoin += Decimal(deal["bought"])
            total_money -= Decimal(
                deal["matecoin_price"]) * Decimal(deal["bought"])
        if deal["sold"]:
            total_matecoin -= Decimal(deal["sold"])
            total_money += Decimal(
                deal["matecoin_price"]) * Decimal(deal["sold"])

    with open("profit.json", "w") as json_file:
        body = {
            "earned_money": str(total_money),
            "matecoin_account": str(total_matecoin)
        }
        json.dump(body, json_file)
