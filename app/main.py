import json
import os
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    if os.path.exists(file_name):
        with open(file_name) as f:
            data_operations = json.load(f)

    earned_money = 0
    matecoin_account = 0

    for operation in data_operations:
        bought = Decimal(operation["bought"] or Decimal("0"))
        sold = Decimal(operation["sold"] or Decimal("0"))
        price = Decimal(operation["matecoin_price"])
        earned_money += (sold - bought) * price
        matecoin_account += bought - sold

    profit_dict = {}
    profit_dict["earned_money"] = str(earned_money)
    profit_dict["matecoin_account"] = str(matecoin_account)

    with open("profit.json", "w") as f:
        json.dump(profit_dict, f, indent=2)
