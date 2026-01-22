import json
from decimal import Decimal, InvalidOperation
from typing import Optional


def calculate_profit(file_name: str) -> Optional[None]:
    try:
        with open(file_name, "r") as f:
            trades = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

    total_earned = Decimal("0")
    matecoin_balance = Decimal("0")

    for trade in trades:
        try:
            bought = Decimal(trade.get("bought") or "0")
            sold = Decimal(trade.get("sold") or "0")
            price = Decimal(trade["matecoin_price"]) \
                if (trade.get("matecoin_price")
                    is not None) else Decimal("0")

            if bought > 0:
                total_earned -= bought * price
                matecoin_balance += bought
            if sold > 0:
                total_earned += sold * price
                matecoin_balance -= sold
        except (InvalidOperation, KeyError):
            return None

    result = {
        "earned_money": str(total_earned),
        "matecoin_account": str(matecoin_balance)
    }

    try:
        with open("profit.json", "w") as f:
            json.dump(result, f, indent=2)
    except IOError:
        return None

    return None
