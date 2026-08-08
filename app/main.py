import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades_data = json.load(f)
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)
    for transaction in trades_data:
        bought = (transaction.get("bought") or 0)
        sold = (transaction.get("sold") or 0)
        matecoin_price = transaction.get("matecoin_price")
        matecoin_account += Decimal(bought) - Decimal(sold)
        earned_money += (
            (Decimal(sold) * Decimal(matecoin_price))
            - (Decimal(bought) * Decimal(matecoin_price))
        )

    trades_result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(trades_result, f, indent=2)
