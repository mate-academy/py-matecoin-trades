import json
from decimal import Decimal


def calculate_profit(trade: str) -> None:
    profit = {}
    earned_money = "0.0"
    matecoin_account = "0.0"
    with open(trade, "r") as file:
        trades = json.load(file)
    for trade in trades:
        if trade["bought"]:
            plus_coin = str(Decimal(matecoin_account)
                            + Decimal(trade["bought"]))
            minus_money = str(Decimal(earned_money)
                              - Decimal(trade["matecoin_price"])
                              * Decimal(trade["bought"]))
            matecoin_account = plus_coin
            earned_money = minus_money
        if trade["sold"]:
            plus_money = str(Decimal(earned_money)
                             + Decimal(trade["matecoin_price"])
                             * Decimal(trade["sold"]))
            minus_coin = str(Decimal(matecoin_account)
                             - Decimal(trade["sold"]))
            matecoin_account = minus_coin
            earned_money = plus_money
    profit["earned_money"] = earned_money
    profit["matecoin_account"] = matecoin_account
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
