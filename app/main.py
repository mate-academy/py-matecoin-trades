from __future__ import annotations

import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = trade["bought"]
        sold = trade["sold"]
        price = trade["matecoin_price"]

        if bought is not None:
            earned_money -= Decimal(bought) * Decimal(price)
            matecoin_account += Decimal(bought)

        if sold is not None:
            earned_money += Decimal(sold) * Decimal(price)
            matecoin_account -= Decimal(sold)

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
