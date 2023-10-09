import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    # Read the days data from the JSON file
    with open(filename, "r") as f:
        days = json.load(f)

    for day in days:
        bought = day.get("bought")
        sold = day.get("sold")
        matecoin_price = Decimal(day["matecoin_price"])

        if bought:
            bought = Decimal(bought)
            earned_money -= bought * matecoin_price
            matecoin_account += bought

        if sold:
            sold = Decimal(sold)
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
