import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    res = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    with open(file_name, "rb") as f:
        source = json.load(f)

    for trade in source:
        if trade["bought"] is not None:
            res["matecoin_account"] += Decimal(trade["bought"])
            res["earned_money"] -= (Decimal(trade["bought"])
                                    * Decimal(trade["matecoin_price"]))
        else:
            res["matecoin_account"] -= Decimal(trade["sold"])
            res["earned_money"] += (Decimal(trade["sold"])
                                    * Decimal(trade["matecoin_price"]))

    with open("profit.json", "w") as input_file:
        json.dump(
            {
                "earned_money": str(res["earned_money"]),
                "matecoin_account": str(res["matecoin_account"])
            },
            input_file,
            indent=2
        )
