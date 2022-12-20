import decimal
import json


def calculate_profit(name: str) -> None:
    opened_file = open(name, "r")
    with opened_file as file:
        parsed_data = json.load(file)

    profit = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    for operation in parsed_data:
        if operation["bought"] is not None:
            profit["earned_money"] -= \
                decimal.Decimal(operation["bought"]) * \
                decimal.Decimal(operation["matecoin_price"])
            profit["matecoin_account"] += decimal.Decimal(operation["bought"])

        if operation["sold"] is not None:
            profit["earned_money"] += \
                decimal.Decimal(operation["sold"]) * \
                decimal.Decimal(operation["matecoin_price"])
            profit["matecoin_account"] -= decimal.Decimal(operation["sold"])

    for kpi, value in profit.items():
        profit[kpi] = str(value)

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)