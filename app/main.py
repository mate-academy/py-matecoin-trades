import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        operation_info = json.load(f)
    profit = [Decimal(0), Decimal(0)]
    for operation in operation_info:
        if operation["bought"] is not None:
            profit[0] += Decimal(operation["bought"])
            profit[1] -= (
                Decimal(operation["bought"])
                * Decimal(operation["matecoin_price"])
            )
        if operation["sold"] is not None:
            profit[0] -= Decimal(operation["sold"])
            profit[1] += (
                Decimal(operation["sold"])
                * Decimal(operation["matecoin_price"])
            )
    profit_result = {
        "earned_money": str(Decimal(profit[1])),
        "matecoin_account": str(Decimal(profit[0]))
    }
    with open("profit.json", "w") as f:
        json.dump(profit_result, f, indent=2)
