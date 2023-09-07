import json
from decimal import Decimal
from typing import Any


def calculate_profit(input_file: Any) -> None:
    with open(input_file, "r") as f:
        trades_data = json.load(f)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades_data:
        if trade["bought"] is not None:
            earned_money += (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account += Decimal(trade["bought"])

        if trade["sold"] is not None:
            earned_money -= (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account -= Decimal(trade["sold"])

    result = {
        "earned_money": str(earned_money * (-1)),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as output_file:
        json.dump(result, output_file, indent=2)
