import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades_data = json.load(file)

    prof = {
        "earned_money": "0",
        "matecoin_account": "0"
    }

    for des in trades_data:
        if des["bought"] is not None:
            cost_b = Decimal(des["bought"]) * Decimal(des["matecoin_price"])
            prof["earned_money"] = str(Decimal(prof["earned_money"]) - cost_b)
            prof["matecoin_account"] = str(Decimal(prof["matecoin_account"])
                                           + Decimal(des["bought"]))
        if des["sold"] is not None:
            cost_s = Decimal(des["sold"]) * Decimal(des["matecoin_price"])
            prof["earned_money"] = str(Decimal(prof["earned_money"]) + cost_s)
            prof["matecoin_account"] = str(Decimal(prof["matecoin_account"])
                                           - Decimal(des["sold"]))

    with open("profit.json", "w") as file:
        json.dump(prof, file, indent=2)
