import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    result = {"earned_money": 0, "matecoin_account": 0}
    with open(filename, "r") as file:
        trades = json.load(file)
    for deals in trades:
        if deals["sold"] is not None:
            result["earned_money"] += (Decimal(deals["sold"])
                                       * Decimal(deals["matecoin_price"]))
            result["matecoin_account"] -= Decimal(deals["sold"])
        if deals["bought"] is not None:
            result["earned_money"] -= (Decimal(deals["bought"])
                                       * Decimal(deals["matecoin_price"]))
            result["matecoin_account"] += Decimal(deals["bought"])
    str_res = {key: str(value) for key, value in result.items()}
    with open("profit.json", "w") as file:
        json.dump(str_res, file, indent=2)
