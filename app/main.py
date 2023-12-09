import json
from decimal import Decimal


def calculate_profit(path_to_file: str) -> None:
    with open(path_to_file, "r") as f:
        operations = json.load(f)
    profit = Decimal(0)
    coins = Decimal(0)
    for operation in operations:
        bought = Decimal(operation.get("bought")) \
            if operation.get("bought") else 0
        sold = Decimal(operation.get("sold")) if operation.get("sold") else 0
        price = Decimal(operation.get("matecoin_price"))
        profit += (sold - bought) * price
        coins += bought - sold
    result = {"earned_money": str(profit), "matecoin_account": str(coins)}
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
