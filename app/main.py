import json
import os
from decimal import Decimal
from typing import Any


def calculate_profit(trades: Any) -> None:
    with open(trades, "r") as f:
        trades_list = json.load(f)
    matecoin_account = Decimal(0)
    earned_money = Decimal(0)
    for element in trades_list:
        if element["bought"] is not None and element["bought"] != "null":
            earned_money = (earned_money
                            - (Decimal(element["bought"])
                               * Decimal(element["matecoin_price"])))
            matecoin_account = matecoin_account + Decimal(element["bought"])
        if element["sold"] is not None and element["sold"] != "null":
            earned_money = (earned_money
                            + (Decimal(element["sold"])
                               * Decimal(element["matecoin_price"])))
            matecoin_account = matecoin_account - Decimal(element["sold"])
    profit_directory = os.path.dirname(trades)
    profit_path = os.path.join(profit_directory, "profit.json")
    profit_file = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open(profit_path, "w") as p:
        json.dump(profit_file, p, indent=2)
    return None
