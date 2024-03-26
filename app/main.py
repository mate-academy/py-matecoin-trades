import json
from decimal import Decimal


def calculate_profit(file_json: str) -> None:
    with open(file_json, "r") as f:
        transactions = json.load(f)

    profit = {"earned_money": 0, "matecoin_account": 0}

    for transact in transactions:
        if not transact["bought"] is None:
            profit["matecoin_account"] += Decimal(transact["bought"])
            profit["earned_money"] -= (Decimal(transact["bought"])
                                       * Decimal(transact["matecoin_price"]))

        if not transact["sold"] is None:
            profit["matecoin_account"] -= Decimal(transact["sold"])
            profit["earned_money"] += (Decimal(transact["sold"])
                                       * Decimal(transact["matecoin_price"]))

    profit = {k: str(v) for k, v in profit.items()}
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
