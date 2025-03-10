import json
import os
from decimal import Decimal, getcontext
from typing import Any, Dict

getcontext().prec = 28


def calculate_profit(trades_file: str) -> None:
    matecoin_account: Decimal = Decimal("0")
    earned_money: Decimal = Decimal("0")
    with open(trades_file, "r", encoding="utf-8") as file:
        trades_data = json.load(file)
    for trade in trades_data:
        bought_str = trade.get("bought")
        sold_str = trade.get("sold")
        price_str = trade.get("matecoin_price")
        if price_str is None:
            continue
        price: Decimal = Decimal(price_str)
        if bought_str is not None:
            bought_amount: Decimal = Decimal(bought_str)
            matecoin_account += bought_amount
            earned_money -= bought_amount * price
        if sold_str is not None:
            sold_amount: Decimal = Decimal(sold_str)
            matecoin_account -= sold_amount
            earned_money += sold_amount * price
    profit_data: Dict[str, Any] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }
    base_dir: str = os.path.dirname(os.path.dirname(os.path.abspath(trades_file)))
    profit_file: str = os.path.join(base_dir, "profit.json")
    with open(profit_file, "w", encoding="utf-8") as output_file:
        json.dump(profit_data, output_file, ensure_ascii=False, indent=2)


def main() -> None:
    calculate_profit("trades.json")
