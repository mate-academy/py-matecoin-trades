import json
from decimal import Decimal


def convert_profit_date_for_json(info: dict) -> dict:
    return {
        "earned_money": str(info["earned_money"]),
        "matecoin_account": str(info["matecoin_account"]),
    }


def calculate_profit(file_name: str) -> None:
    dict_operation = {}
    with open(file_name) as f:
        dict_operation = json.load(f)

    dict_profit = {"earned_money" : Decimal("0.0"),
                   "matecoin_account": Decimal("0.0")}

    for operation in dict_operation:
        if operation["bought"] is not None:
            dict_profit["earned_money"] -= (
                Decimal(str(operation["bought"]))
                * Decimal(str(operation["matecoin_price"]))
            )
            dict_profit["matecoin_account"] += Decimal(
                str(operation["bought"])
            )
        if operation["sold"] is not None:
            dict_profit["earned_money"] += (
                Decimal(str(operation["sold"]))
                * Decimal(str(operation["matecoin_price"]))
            )
            dict_profit["matecoin_account"] -= Decimal(str(operation["sold"]))

    with open("profit.json", "w") as f:
        json.dump(convert_profit_date_for_json(dict_profit), f, indent=2)
