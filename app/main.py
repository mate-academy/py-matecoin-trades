import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        currency_data = json.load(f)
    accumulation = {
        "earned_money": Decimal(),
        "matecoin_account": Decimal()
    }
    for operation in currency_data:
        if operation["bought"] is not None:
            accumulation["earned_money"] -= (
                Decimal(operation["bought"])
                * Decimal(operation["matecoin_price"])
            )
            accumulation["matecoin_account"] += Decimal(operation["bought"])
        if operation["sold"] is not None:
            accumulation["earned_money"] += (
                Decimal(operation["sold"])
                * Decimal(operation["matecoin_price"])
            )
            accumulation["matecoin_account"] -= Decimal(operation["sold"])
    accumulation["earned_money"] = str(accumulation["earned_money"])
    accumulation["matecoin_account"] = str(accumulation["matecoin_account"])
    with open("PROFIT.json", "w") as f:
        json.dump(accumulation, f, indent=2)
