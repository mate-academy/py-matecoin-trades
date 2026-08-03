import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:

    with open(trades) as trades_file:
        trades_operations = json.load(trades_file)

    operations_dict = {}
    earned_money = 0
    matecoin_balance = 0

    for operation in trades_operations:
        if operation["sold"] is None:
            op_balance = Decimal(operation["bought"])
            earned_money -= (
                Decimal(op_balance) * Decimal(operation["matecoin_price"])
            )
            matecoin_balance += op_balance

        elif operation["bought"] is None:
            op_balance = Decimal(operation["sold"])
            earned_money += (
                Decimal(op_balance) * Decimal(operation["matecoin_price"])
            )
            matecoin_balance -= op_balance

        else:
            earned_money -= (
                Decimal(operation["bought"])
                * Decimal(operation["matecoin_price"])
            )
            earned_money += (
                Decimal(operation["sold"])
                * Decimal(operation["matecoin_price"])
            )
            matecoin_balance += (
                Decimal(operation["bought"]) - Decimal(operation["sold"])
            )

    operations_dict["earned_money"] = str(earned_money)
    operations_dict["matecoin_account"] = str(matecoin_balance)

    with open("profit.json", "w") as file:
        json.dump(operations_dict, file, indent=2)
