import json
from decimal import Decimal


def calculate_profit(json_file: str) -> None:
    with open(json_file) as json_trades_info:
        trades_info = json.load(json_trades_info)

    earned_money = 0
    matecoin_account = 0

    for trade in trades_info:
        one_trade_matecoin_amount = (Decimal(trade["bought"] or 0)
                                     - Decimal(trade["sold"] or 0))
        one_trade_profit = (-one_trade_matecoin_amount
                            * Decimal(trade["matecoin_price"]))

        earned_money += one_trade_profit
        matecoin_account += one_trade_matecoin_amount

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as json_profit:
        json.dump(profit, json_profit, indent=2)
