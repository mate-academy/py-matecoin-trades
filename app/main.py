import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as trades_file:
        trades = json.load(trades_file)
        matecoin_account = 0
        earned_money = 0
        for trade in trades:
            if trade["bought"] is not None:
                matecoin_account += Decimal(trade["bought"])
                earned_money -= (
                    Decimal(trade["bought"])
                    * Decimal(trade["matecoin_price"])
                )
            if trade["sold"] is not None:
                matecoin_account -= Decimal(trade["sold"])
                earned_money += (
                    Decimal(trade["sold"])
                    * Decimal(trade["matecoin_price"])
                )

        new_trade_data = {
            "earned_money": f"{earned_money}",
            "matecoin_account": f"{matecoin_account}"
        }

        with open("profit.json", "w") as profit:
            json.dump(new_trade_data, profit, indent=2)
