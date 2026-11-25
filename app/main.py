import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as json_file:
        data = json.load(json_file)
    total_profit = {"earned_money": Decimal("0"),
                    "matecoin_account": Decimal("0")}
    for operation in data:
        if operation["bought"] is not None:
            total_profit["earned_money"] -= \
                (Decimal(operation["bought"])
                 * Decimal(operation["matecoin_price"])
                 )
            total_profit["matecoin_account"] += Decimal(operation["bought"])
        if operation["sold"] is not None:
            total_profit["earned_money"] +=\
                (Decimal(operation["sold"])
                 * Decimal(operation["matecoin_price"])
                 )
            total_profit["matecoin_account"] -= Decimal(operation["sold"])
    total_profit["earned_money"] = str(total_profit["earned_money"])
    total_profit["matecoin_account"] = str(total_profit["matecoin_account"])
    with open("profit.json", "w") as json_file:
        json.dump(total_profit, json_file, indent=2)
