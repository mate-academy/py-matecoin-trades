import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit = {
        "earned_money": Decimal(0),
        "matecoin_account": Decimal(0)
    }

    with open(file_name) as f:
        operations = json.load(f)

    for operation in operations:
        if operation["bought"]:
            buy = Decimal(str(operation["bought"]))
            balance = Decimal(str(operation["matecoin_price"]))
            profit["earned_money"] -= buy * balance
            profit["matecoin_account"] += buy

        if operation["sold"]:
            sell = Decimal(str(operation["sold"]))
            balance = Decimal(str(operation["matecoin_price"]))
            profit["earned_money"] += sell * balance
            profit["matecoin_account"] -= sell
    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
