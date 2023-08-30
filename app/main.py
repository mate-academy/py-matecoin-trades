import json
from decimal import Decimal


def calculate_profit(operations: json) -> None:
    with open(operations) as input_file:
        operations_per_day = json.load(input_file)

    money_balance = 0
    coin_account = 0

    for operation in operations_per_day:
        if operation["bought"] is not None:
            money_balance -= Decimal(operation["bought"]) * Decimal(
                operation["matecoin_price"]
            )
            coin_account += Decimal(operation["bought"])

        if operation["sold"] is not None:
            money_balance += Decimal(operation["sold"]) * Decimal(
                operation["matecoin_price"]
            )
            coin_account -= Decimal(operation["sold"])

    day_result = {
        "earned_money": str(money_balance),
        "matecoin_account": str(coin_account),
    }

    with open("profit.json", "w") as output_file:
        json.dump(day_result, output_file, indent=2)
