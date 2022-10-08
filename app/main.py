import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as file_input:
        data_py = json.load(file_input)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in data_py:
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal(0)
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal(0)
        price = Decimal(trade["matecoin_price"]) \
            if trade["matecoin_price"] else Decimal(0)
        earned_money += (sold - bought) * price
        matecoin_account += bought - sold

    profit = {
        "earned_money": f"{earned_money}",
        "matecoin_account": f"{matecoin_account}"
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
