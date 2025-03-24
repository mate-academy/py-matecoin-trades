import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as f:
        data = json.load(f)
    profit = {"earned_money": Decimal("0"), "matecoin_account": Decimal("0")}

    for transaction in data:
        bought = Decimal(transaction["bought"]) if (
            transaction.get("bought")) else Decimal("0")
        sold = Decimal(transaction["sold"]) if (
            transaction.get("sold")) else Decimal("0")
        price = Decimal(transaction["matecoin_price"])

        profit["earned_money"] += sold * price - bought * price
        profit["matecoin_account"] += bought - sold

    profit_str = {k: str(v) for k, v in profit.items()}

    with open("D:\\Mate\\py-matecoin-trades\\profit.json", "w") as f:
        json.dump(profit_str, f, indent=2)
