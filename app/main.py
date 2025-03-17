import json
from decimal import Decimal
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def calculate_profit(file_name: str = f"{BASE_DIR}/app/trades.json") -> None:
    with open(file_name) as f:
        trades_data = json.load(f)

    matecoin_account = Decimal("0.0")
    total_spent = Decimal("0.0")
    total_earned = Decimal("0.0")

    for daily_trade in trades_data:
        if daily_trade["sold"] is not None:
            sold = Decimal(daily_trade["sold"])
        else:
            sold = Decimal("0.0")

        if daily_trade["bought"] is not None:
            bought = Decimal(daily_trade["bought"])
        else:
            bought = Decimal("0.0")

        matecoin_account += bought - sold
        total_spent += bought * Decimal(daily_trade["matecoin_price"])
        total_earned += sold * Decimal(daily_trade["matecoin_price"])

    earned_money = total_earned - total_spent
    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
