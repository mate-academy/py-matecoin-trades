import decimal

import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as operation_file:
        operations = json.load(operation_file)
        earned_money = 0
        matecoin_account = 0
        for operations_checker in operations:
            if operations_checker["bought"] is not None:
                matecoin_account += decimal.Decimal(
                    operations_checker["bought"])
                earned_money -= decimal.Decimal(
                    operations_checker["matecoin_price"]) * decimal.Decimal(
                    operations_checker["bought"])
            if operations_checker["sold"] is not None:
                matecoin_account -= decimal.Decimal(operations_checker["sold"])
                earned_money += decimal.Decimal(
                    operations_checker["matecoin_price"]) * decimal.Decimal(
                    operations_checker["sold"]
                )
        profit = {"earned_money": str(earned_money),
                  "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
