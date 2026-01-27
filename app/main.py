import json
from decimal import Decimal
from typing import Any, Dict, List, Optional


def _to_decimal(value: Optional[str]) -> Decimal:
    if value is None:
        return Decimal("0")
    return Decimal(value)


def calculate_profit(trades_filename: str) -> None:
    with open(trades_filename, "r", encoding="utf-8") as file_reader:
        trades: List[Dict[str, Any]] = json.load(file_reader)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought_amount = _to_decimal(trade.get("bought"))
        sold_amount = _to_decimal(trade.get("sold"))
        matecoin_price = _to_decimal(trade.get("matecoin_price"))

        if bought_amount != Decimal("0"):
            matecoin_account += bought_amount
            earned_money -= bought_amount * matecoin_price

        if sold_amount != Decimal("0"):
            matecoin_account -= sold_amount
            earned_money += sold_amount * matecoin_price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as file_writer:
        json.dump(result, file_writer, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
