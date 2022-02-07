from decimal import Decimal
import json


def calculate_profit(file_name):
    profit = dict()
    earned_money = 0
    matecoin_account = 0

    with open(file_name) as source:
        trades_information = json.load(source)

    for trade_information in trades_information:
        if not trade_information["sold"]:
            trade_information["sold"] = 0
        elif not trade_information["bought"]:
            trade_information["bought"] = 0
        trade_profit = \
            Decimal(trade_information
                    ["sold"]) - Decimal(trade_information["bought"])
        earned_money += \
            Decimal(trade_information["matecoin_price"]) * trade_profit
        matecoin_account += -1 * trade_profit

    profit["earned_money"] = str(earned_money)
    profit["matecoin_account"] = str(matecoin_account)
    with open("profit.json", "a") as destination:
        json.dump(profit, destination)
