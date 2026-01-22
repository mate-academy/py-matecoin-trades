# write your code here
import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as file:
        transactions = json.load(file)
    matecoin_account = Decimal("0")
    by = Decimal("0")
    sold = Decimal("0")
    for transact in transactions:
        price = Decimal(transact["matecoin_price"])
        if transact["bought"]:
            by += Decimal(transact["bought"]) * price
            matecoin_account += Decimal(transact["bought"])
        if transact["sold"]:
            sold += Decimal(transact["sold"]) * price
            matecoin_account -= Decimal(transact["sold"])
    profit = sold - by
    report = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_account.copy_abs())
    }
    with open("profit.json", "w") as file:
        json.dump(report, file, indent=2)
