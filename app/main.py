from decimal import Decimal
import json


def calculate_profit(file_name):
    with open(file_name, "r") as trades:

        profit = 0
        matecoin_account = 0
        trades_list = json.load(trades)
        for trade in trades_list:
            matecoin_price = Decimal(trade["matecoin_price"])
            if trade["bought"] is not None:
                profit += Decimal(trade["bought"]) * matecoin_price
                matecoin_account += Decimal(trade["bought"])

            if trade["sold"] is not None:
                profit -= Decimal(trade["sold"]) * matecoin_price
                matecoin_account -= Decimal(trade["sold"])

        profit_list = {
            "earned_money": str(profit),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as profit:
            json.dump(profit_list, profit, indent=2)

