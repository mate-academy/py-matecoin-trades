import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    profit = Decimal()
    qty = Decimal()

    with open(file=file_name, mode="r") as file:
        trades = json.load(file)

        for trade in trades:
            value = trade["bought"]
            bought_units = value if value is not None else Decimal(0)
            bought_units = Decimal(bought_units)

            value = trade["sold"]
            sold_units = value if value is not None else Decimal(0)
            sold_units = Decimal(sold_units)

            price = Decimal(trade["matecoin_price"])
            profit += (bought_units * price + sold_units * price)
            qty += (bought_units - sold_units)

    info = {
        "earned_money" : str(profit),
        "matecoin_account" : str(qty)
    }

    with open(file="profit.json", mode="w") as file:
        file.write(json.dumps(info))
