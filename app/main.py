import json
from decimal import Decimal


def calculate_profit(file_name: None) -> None:
    with open(file_name, "r") as file:
        operations = json.load(file)
    matecoins = Decimal("0")
    profit = Decimal("0")
    for operation in operations:
        price = Decimal(operation["matecoin_price"])
        if operation["bought"]:
            matecoins += Decimal(operation["bought"])
            profit -= Decimal(operation["bought"]) * price
        if operation["sold"]:
            matecoins -= Decimal(operation["sold"])
            profit += Decimal(operation["sold"]) * price
    with open("profit.json", "w") as json_file:
        json.dump({"earned_money": str(profit),
                  "matecoin_account": str(matecoins)},
                  json_file,
                  indent=2)
