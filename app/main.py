import json
from decimal import Decimal
from typing import Dict, List


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r", encoding="utf-8") as file:
        trades: List[Dict[str, str | None]] = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        bought = trade.get("bought")
        if bought is not None:
            bought_amount = Decimal(bought)
            matecoin_account += bought_amount
            earned_money -= bought_amount * price

        sold = trade.get("sold")
        if sold is not None:
            sold_amount = Decimal(sold)
            matecoin_account -= sold_amount
            earned_money += sold_amount * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file)
