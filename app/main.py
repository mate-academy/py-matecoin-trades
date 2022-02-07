from decimal import Decimal
import json


def calculate_profit(file_name):
    earned_money = 0
    matecoin_account = 0

    with open(file_name) as source:
        trades_information = json.load(source)

    for trade in trades_information:
        if not trade["sold"]:
            trade["sold"] = 0
        elif not trade["bought"]:
            trade["bought"] = 0
        trade_profit = Decimal(trade["sold"]) - Decimal(trade["bought"])
        earned_money += Decimal(trade["matecoin_price"]) * trade_profit
        matecoin_account += -1 * trade_profit

    with open("profit.json", "a") as destination:
        json.dump({"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)},
                  destination, indent=2)
