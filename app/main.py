import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)

    bought = Decimal("0")
    money = Decimal("0")

    for item in data:
        if item["bought"] is not None:
            bought += Decimal(item["bought"])
            money -= Decimal(item["matecoin_price"]) * Decimal(item["bought"])
        if item["sold"] is not None:
            bought -= Decimal(item["sold"])
            money += Decimal(item["matecoin_price"]) * Decimal(item["sold"])

    with open("profit.json", "w") as json_file:
        json.dump(
            {
                "earned_money": str(money),
                "matecoin_account": str(bought),
            },
            json_file,
            indent=2
        )
