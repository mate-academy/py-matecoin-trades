from decimal import Decimal
import json
import os


def calculate_profit(trades: str) -> None:
    total_earned = Decimal("0")
    total_spent = Decimal("0")
    matecoin_account = Decimal("0")
    with open(trades, "r") as f:
        trades_data = json.load(f)

    for data in trades_data:
        matecoin_price = Decimal(data['matecoin_price'])
        if data["bought"] is not None:
            bought_volume = Decimal(data["bought"])
            total_spent += bought_volume * matecoin_price
            matecoin_account += bought_volume
        if data["sold"] is not None:
            sold_volume = Decimal(data["sold"])
            total_earned += sold_volume * matecoin_price
            matecoin_account -= sold_volume

    earned_money = total_earned - total_spent
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
