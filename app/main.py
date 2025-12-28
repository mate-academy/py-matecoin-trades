import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)

    matecoin_count = Decimal("0")
    earned_count = Decimal("0")

    for trade in trades:
        bought = trade["bought"]
        sold = trade["sold"]
        price = Decimal(trade["matecoin_price"])

        if bought is not None:
            bought_amount = Decimal(bought)
            matecoin_count += bought_amount
            earned_count -= bought_amount * price

        if sold is not None:
            sold_amount = Decimal(sold)
            matecoin_count -= sold_amount
            earned_count += sold_amount * price

    result = {
        "earned_money": str(earned_count),
        "matecoin_account": str(matecoin_count),
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
