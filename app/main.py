from decimal import Decimal
import json


def calculate_profit(file_name):
    earned_money = 0
    matecoin_account = 0

    with open(file_name) as source:
        trades_information = json.load(source)

    for trade in trades_information:
        for value in ("sold", "bought"):
            if not trade[value]:
                trade[value] = 0
        trade_profit = Decimal(trade["sold"]) - Decimal(trade["bought"])
        earned_money += Decimal(trade["matecoin_price"]) * trade_profit
        matecoin_account -= trade_profit

    with open("profit.json", "a") as destination:
        json.dump({"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)},
                  destination, indent=2)
