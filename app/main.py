import json
from decimal import Decimal
from typing import Any


def calculate_profit(trades_file: Any) -> None:
    try:
        with open(trades_file, "r") as file:
            trades_dictionary = json.load(file)

        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for trade in trades_dictionary:
            bought = Decimal(trade.get("bought") or " 0")
            sold = Decimal(trade.get("sold") or "0")
            price = Decimal(trade.get("matecoin_price") or "0")

            if bought:
                matecoin_account += bought
                earned_money -= bought * price

            if sold:
                matecoin_account -= sold
                earned_money += sold * price

        profit_data = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as profit_file:
            json.dump(profit_data, profit_file, indent=2)
    except Exception as e:
        print(f"Error: {e}")
