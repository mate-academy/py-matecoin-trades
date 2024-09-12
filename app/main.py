from decimal import Decimal

import json


def calculate_profit(file_name):
    with open(file_name, "r") as trade_report:
        operations = json.load(trade_report)

    earned_money = 0
    matecoin_account = 0

    for operation in operations:
        matecoin_price = Decimal(operation["matecoin_price"])

        if operation["sold"]:
            earned_money += Decimal(operation["sold"] * matecoin_price)
            matecoin_account -= Decimal(operation["sold"])

        if operation["bought"]:
            earned_money -= Decimal(operation["sold"] * matecoin_price)
            matecoin_account += Decimal(operation["sold"])

    with open("profit.json" "w") as operations_report:
        json.dump({"earned_money": str(earned_money),
                  "matecoin_account": str(matecoin_account)},
                  operations_report, indent=2)
