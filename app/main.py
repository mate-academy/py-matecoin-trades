from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    total_earned = 0
    total_balance = 0
    with open(filename, "r") as trades_file:
        trades = json.load(trades_file)
        for trade in trades:
            bought = Decimal(trade.get("bought") or "0")
            sold = Decimal(trade.get("sold") or "0")
            price = Decimal(trade.get("matecoin_price") or "0")

            total_earned += (sold - bought) * price
            total_balance += bought - sold

    with open("profit.json", "w") as profit_file:
        profit_data = {
            "earned_money": str(total_earned),
            "matecoin_account": str(total_balance),
        }
        json.dump(profit_data, profit_file, indent=2)
