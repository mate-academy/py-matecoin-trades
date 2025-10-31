import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        data = json.load(f)

    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    for item in data:
        if item["bought"] is not None and item["matecoin_price"] is not None:
            matecoin_account += Decimal(item["bought"])
            spent = Decimal(item["bought"]) * Decimal(item["matecoin_price"])
            earned_money -= spent

        if item["sold"] is not None and item["matecoin_price"] is not None:
            matecoin_account -= Decimal(item["sold"])
            spent = Decimal(item["sold"]) * Decimal(item["matecoin_price"])
            earned_money += spent

    data_of_coin = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as j_file:
        json.dump(data_of_coin, j_file, indent=2)
