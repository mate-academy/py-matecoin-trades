import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    profit, account = Decimal(), Decimal()
    with open(filename, "r") as file_in, open("profit.json", "w") as file_out:
        data = json.load(file_in)
        for row in data:
            price = Decimal(row["matecoin_price"])
            if row["bought"]:
                bought = Decimal(row["bought"])
                profit -= bought * price
                account += bought
            if row["sold"]:
                sold = Decimal(row["sold"])
                profit += sold * price
                account -= sold
        result = {"earned_money": str(profit),
                  "matecoin_account": str(account)}
        json.dump(result, file_out, indent=2)
