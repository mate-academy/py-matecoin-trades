import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for item in trades:
        bought_value = item.get("bought")
        bought = Decimal(bought_value) \
            if bought_value is not None else Decimal(0)

        sold_value = item.get("sold")
        sold = Decimal(sold_value) if sold_value is not None else Decimal(0)

        price = Decimal(item["matecoin_price"])

        earned_money += sold * price - bought * price
        matecoin_account += bought - sold

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file_with_profit:
        json.dump(profit, file_with_profit, indent=2)
