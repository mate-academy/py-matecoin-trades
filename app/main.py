from __future__ import annotations

import json
from decimal import Decimal
from typing import Any, Dict, Optional


def _to_decimal(value: Optional[str]) -> Decimal:
    """Convert JSON string or None to Decimal (None -> Decimal('0'))."""
    return Decimal(value) if value is not None else Decimal("0")


def _decimal_to_str(value: Decimal) -> str:
    """Return a non-exponential string for Decimal suitable for JSON."""
    return format(value, "f")


def calculate_profit(filename: str) -> None:
    """
    Read trades from `filename`, compute earned money and current coin
    balance using Decimal, and dump results to profit.json as strings.
    """
    with open(filename, "r", encoding="utf-8") as f:
        trades: list[Dict[str, Any]] = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = _to_decimal(trade.get("matecoin_price"))
        bought = trade.get("bought")
        sold = trade.get("sold")

        if bought is not None:
            bought_amount = _to_decimal(bought)
            matecoin_account += bought_amount
            earned_money -= bought_amount * price

        if sold is not None:
            sold_amount = _to_decimal(sold)
            matecoin_account -= sold_amount
            earned_money += sold_amount * price

    result = {
        "earned_money": _decimal_to_str(earned_money),
        "matecoin_account": _decimal_to_str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
