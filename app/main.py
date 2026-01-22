import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        file_data = json.load(f)

    total_bought_amount = Decimal(0)
    total_sold_amount = Decimal(0)
    total_bought = Decimal(0)
    total_sold = Decimal(0)

    for data in file_data:
        bought_js = Decimal(data.get("bought") or 0)
        sold_js = Decimal(data.get("sold") or 0)
        price_js = Decimal(data["matecoin_price"])

        total_bought_amount += bought_js * price_js
        total_sold_amount += sold_js * price_js
        total_sold += sold_js
        total_bought += bought_js

    profit = str(total_sold_amount - total_bought_amount)
    account = str(total_bought - total_sold)

    with open("profit.json", "w") as out:
        json.dump(
            {
                "earned_money": profit,
                "matecoin_account": account
            }, out, indent=2
        )
