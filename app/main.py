# write your code here
import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as file:
        transactions = json.load(file)
    by = Decimal("0")
    sold = Decimal("0")
    for transact in transactions:
        price = Decimal(transact["matecoin_price"])
        if transact["bought"]:
            by += Decimal(transact["bought"]) * price
        else:
            sold += Decimal(transact["sold"]) * price
    profit = sold - by
    account = "0.00007"
    report = {
        "earned_money": str(profit),
        "matecoin_account": account
    }
    json_object = json.dumps(report, indent=2)
    with open("profit.json", "w") as file:
        file.write(json_object)
