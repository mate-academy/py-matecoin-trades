import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as json_file:
        data = json.load(json_file)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for item in data:
        price = Decimal(str(item["matecoin_price"]))
        if item["bought"] is not None:
            amount = Decimal(str(item["bought"]))
            earned_money -= price * amount
            matecoin_account += amount
        if item["sold"] is not None:
            amount = Decimal(str(item["sold"]))
            earned_money += price * amount
            matecoin_account -= amount

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
