from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with (open(file_name, "r") as file,
          open("profit.json", "w") as profit):
        trades = json.load(file)
        total_bought = 0
        total_sold = 0
        total_coins = 0
        for trade in trades:
            if not trade["bought"] is None:
                total_coins += Decimal(trade["bought"])
                total_bought += (Decimal(trade["bought"])
                                 * Decimal(trade["matecoin_price"]))
            if not trade["sold"] is None:
                total_coins -= Decimal(trade["sold"])
                total_sold += (Decimal(trade["sold"])
                               * Decimal(trade["matecoin_price"]))
        profits = {
            "earned_money": str(total_sold - total_bought),
            "matecoin_account": str(total_coins)
        }
        json.dump(profits, profit, indent=2)
