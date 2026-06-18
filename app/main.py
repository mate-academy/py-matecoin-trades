import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r", encoding="utf-8") as file:
        datas = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for data in datas:
        bought = data["bought"]
        sold = data["sold"]
        matecoin_price = data["matecoin_price"]

        if bought is None:
            bought = "0"
        if sold is None:
            sold = "0"

        earned_money += \
            ((Decimal(sold) - Decimal(bought)) * Decimal(matecoin_price))
        matecoin_account += Decimal(bought) - Decimal(sold)

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2, separators=(",", ": "))
