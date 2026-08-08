import json
from decimal import Decimal
from typing import Any, Dict, List


def calculate_profit(trades_filename: str) -> None:
    with open(trades_filename, "r", encoding="utf-8") as file:
        trades: List[Dict[str, Any]] = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought_value = trade.get("bought")
        sold_value = trade.get("sold")
        price_value = trade.get("matecoin_price")

        price = Decimal(str(price_value))

        if bought_value is not None:
            bought = Decimal(str(bought_value))
            matecoin_account += bought
            earned_money -= bought * price

        if sold_value is not None:
            sold = Decimal(str(sold_value))
            matecoin_account -= sold
            earned_money += sold * price

    result: Dict[str, str] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)
