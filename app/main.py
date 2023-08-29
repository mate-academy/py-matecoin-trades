import json

from decimal import Decimal


def calculate_profit(trades_info: json) -> None:
    with open(trades_info) as f:
        trades_data = json.load(f)

        earned_money = 0
        matecoin_account = 0
        for trade in trades_data:
            if trade["bought"]:
                earned_money -= (Decimal(trade["bought"])
                                 * Decimal(trade["matecoin_price"]))
                matecoin_account += Decimal(trade["bought"])
            if trade["sold"]:
                earned_money += (Decimal(trade["sold"])
                                 * Decimal(trade["matecoin_price"]))
                matecoin_account -= Decimal(trade["sold"])

        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as profit_file:
            json.dump(profit, profit_file, indent=2)
