import json
from decimal import Decimal
from typing import Any


def calculate_profit(in_file: Any) -> None:
    with open(in_file, "r") as file:
        operations = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for operation in operations:
        bought = Decimal(operation["bought"]) \
            if operation["bought"] else Decimal("0")
        sold = Decimal(operation["sold"]) \
            if operation["sold"] else Decimal("0")
        matecoin_price = Decimal(operation["matecoin_price"])

        matecoin_account += bought - sold

        earned_money += sold * matecoin_price - bought * matecoin_price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as out_file:
        json.dump(result, out_file, indent=2)
