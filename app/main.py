import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as trades_json:
        trades_history = json.load(trades_json)

    earned_money = 0
    matecoin_account = 0
    for trade in trades_history:
        if trade["bought"] is not None:
            earned_money -= Decimal(trade["bought"]) * Decimal(
                trade["matecoin_price"])
            matecoin_account += Decimal(trade["bought"])
            if trade["sold"] is not None:
                earned_money += Decimal(trade["sold"]) * Decimal(
                    trade["matecoin_price"])
                matecoin_account -= Decimal(trade["sold"])
        else:
            earned_money += Decimal(trade["sold"]) * Decimal(
                trade["matecoin_price"])
            matecoin_account -= Decimal(trade["sold"])

    profit_dict = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}

    json.dump(profit_dict, open("profit.json", "w"))
