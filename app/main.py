import json
from decimal import Decimal


def calculate_profit(file_json: str) -> None:
    with open(file_json, "r") as trade_data:
        operations = json.load(trade_data)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for operation in operations:
        if operation["bought"] is not None and operation["sold"] is not None:
            earned_money += (
                (Decimal(operation["sold"]) - Decimal(operation["bought"]))
                * Decimal(operation["matecoin_price"])
            )
            matecoin_account += (Decimal(operation["bought"])
                                 - Decimal(operation["sold"]))
        if operation["bought"] is not None and operation["sold"] is None:
            earned_money -= (Decimal(operation["bought"])
                             * Decimal(operation["matecoin_price"]))
            matecoin_account += Decimal(operation["bought"])
        if operation["sold"] is not None and operation["bought"] is None:
            earned_money += (Decimal(operation["sold"])
                             * Decimal(operation["matecoin_price"]))
            matecoin_account -= Decimal(operation["sold"])
    profit_info = {
        "earned_money": f"{earned_money}",
        "matecoin_account": f"{matecoin_account}"
    }
    with open("profit.json", "w") as profit_file:
        json.dump(profit_info, profit_file, indent=2)
