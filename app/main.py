from __future__ import annotations

import json
from decimal import Decimal, getcontext
from typing import Any


getcontext().prec = 28


def _to_decimal(value: str | int | float | None) -> Decimal:
    if value is None:
        return Decimal("0")
    return Decimal(str(value))


def _to_str_no_sci(dec: Decimal) -> str:
    text = format(dec.normalize(), "f")
    if "." in text:
        text = text.rstrip("0").rstrip(".")
    return text if text else "0"


def calculate_profit(trades_file: str, out_file: str = "profit.json") -> None:
    with open(trades_file, "r", encoding="utf-8") as file_obj:
        trades: list[dict[str, Any]] = json.load(file_obj)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = _to_decimal(trade.get("matecoin_price"))

        bought_value = trade.get("bought")
        if bought_value is not None:
            amount = _to_decimal(bought_value)
            matecoin_account += amount
            earned_money -= amount * price

        sold_value = trade.get("sold")
        if sold_value is not None:
            amount = _to_decimal(sold_value)
            matecoin_account -= amount
            earned_money += amount * price

    result = {
        "earned_money": _to_str_no_sci(earned_money),
        "matecoin_account": _to_str_no_sci(matecoin_account),
    }

    with open(out_file, "w", encoding="utf-8") as file_obj:
        json.dump(result, file_obj, ensure_ascii=False, indent=2)

    return None
