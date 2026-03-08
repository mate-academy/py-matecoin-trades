import json
from decimal import Decimal
from typing import Any, Dict, List


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r", encoding="utf-8") as input_file:
        trades: List[Dict[str, Any]] = json.load(input_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = trade["bought"]
        sold = trade["sold"]
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought is not None:
            bought_amount = Decimal(bought)
            matecoin_account += bought_amount
            earned_money -= bought_amount * matecoin_price

        if sold is not None:
            sold_amount = Decimal(sold)
            matecoin_account -= sold_amount
            earned_money += sold_amount * matecoin_price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as output_file:
        json.dump(result, output_file, indent=2)
