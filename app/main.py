import json
from decimal import Decimal, ROUND_DOWN
from typing import Any


def calculate_profit(trades_file: Any) -> None:
    with open(trades_file, "r") as f:
        trades_data = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        matecoin_price = Decimal(trade["matecoin_price"])
        bought = Decimal(trade.get("bought", "0") or "0")
        sold = Decimal(trade.get("sold", "0") or "0")
        earned_money += sold * matecoin_price
        matecoin_account += bought - sold
    earned_money = earned_money.quantize(Decimal("1E-8"), rounding=ROUND_DOWN)
    matecoin_account = matecoin_account.quantize(Decimal("1E-8"), rounding=ROUND_DOWN)

    earned_money = earned_money.normalize()
    matecoin_account = matecoin_account.normalize()

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2, sort_keys=True)
