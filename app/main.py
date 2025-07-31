import json
from decimal import Decimal
from typing import Dict, List, Optional


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades: List[Dict[str, Optional[str]]] = json.load(f)

    earned_money: Decimal = Decimal("0")
    matecoin_account: Decimal = Decimal("0")

    for trade in trades:
        price: Decimal = Decimal(trade["matecoin_price"])

        bought_str: Optional[str] = trade.get("bought")
        sold_str: Optional[str] = trade.get("sold")

        if bought_str is not None:
            bought: Decimal = Decimal(bought_str)
            earned_money -= bought * price
            matecoin_account += bought

        if sold_str is not None:
            sold: Decimal = Decimal(sold_str)
            earned_money += sold * price
            matecoin_account -= sold

    result: Dict[str, str] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
