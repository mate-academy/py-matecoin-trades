from typing import Any
import json
from decimal import Decimal


def calculate_profit(json_file_name: Any) -> None:
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    with open(json_file_name, "r") as json_file:
        incoming_data = json.load(json_file)

    for trade in incoming_data:
        price = Decimal(trade["matecoin_price"])

        if trade.get("bought") is not None:
            bought = Decimal(trade.get("bought"))
            matecoin_account += bought
            earned_money -= bought * price

        if trade.get("sold") is not None:
            bought = Decimal(trade.get("sold"))
            matecoin_account -= bought
            earned_money += bought * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as json_file:
        json.dump(result, json_file, indent=2)
