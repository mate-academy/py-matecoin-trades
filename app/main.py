import json
from decimal import Decimal
from typing import Any, Dict, List


def calculate_profit(trades: str) -> None:
    with open(trades, "r", encoding="utf-8") as f:
        trades: List[Dict[str, Any]] = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        bought_str = trade.get("bought")
        if bought_str is not None:
            bought = Decimal(bought_str)
            matecoin_account += bought
            earned_money -= bought * price

        sold_str = trade.get("sold")
        if sold_str is not None:
            sold = Decimal(sold_str)
            matecoin_account -= sold
            earned_money += sold * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
