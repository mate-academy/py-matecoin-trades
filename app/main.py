import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        currency_data = json.load(f)
    trades = {
        "earned_money": Decimal(),
        "matecoin_account": Decimal()
    }
    for operation in currency_data:
        if operation["bought"] is not None:
            trades["earned_money"] -= (
                Decimal(operation["bought"])
                * Decimal(operation["matecoin_price"])
            )
            trades["matecoin_account"] += Decimal(operation["bought"])
        if operation["sold"] is not None:
            trades["earned_money"] += (
                Decimal(operation["sold"])
                * Decimal(operation["matecoin_price"])
            )
            trades["matecoin_account"] -= Decimal(operation["sold"])
    trades["earned_money"] = str(trades["earned_money"])
    trades["matecoin_account"] = str(trades["matecoin_account"])
    with open("profit.json", "w") as f:
        json.dump(trades, f, indent=2)
