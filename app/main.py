import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r", encoding="utf-8") as file_input:
        data = json.load(file_input)

    earned = Decimal("0")
    coin_left = Decimal("0")

    for trade in data:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = Decimal(str(trade["matecoin_price"]))

        bought_d = Decimal(str(bought)) if bought is not None else Decimal("0")
        sold_d = Decimal(str(sold)) if sold is not None else Decimal("0")

        earned += (sold_d * price) - (bought_d * price)
        coin_left += bought_d - sold_d

    profit = {
        "earned_money": str(earned),
        "matecoin_account": str(coin_left),
    }

    with open("profit.json", "w") as file_output:
        json.dump(profit, file_output, indent=2)
