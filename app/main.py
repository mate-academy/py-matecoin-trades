import os
import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(trades_file: str) -> None:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    profit_file = os.path.join(base_dir, "..", "profit.json")

    total_spent = Decimal("0")
    total_earned = Decimal("0")
    matecoin_account = Decimal("0")

    with open(trades_file, "r") as file:
        trades = json.load(file)

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = Decimal(trade.get("matecoin_price"))

        if bought is not None:
            bought_amount = Decimal(bought)
            matecoin_account += bought_amount
            total_spent += bought_amount * price

        if sold is not None:
            sold_amount = Decimal(sold)
            matecoin_account -= sold_amount
            total_earned += sold_amount * price

    earned_money = total_earned - total_spent

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(profit_file, "w") as outfile:
        json.dump(profit_data, outfile, indent=2)


BASE_DIR = Path(__file__).resolve().parent.parent
calculate_profit(f"{BASE_DIR}/app/trades.json")
