import json
from decimal import Decimal


def calculate_profit(file_name):
    with open(file_name) as json_file:
        trades = json.load(json_file)

        earned_money = 0
        matecoin_account = 0

        for trade in trades:
            price = Decimal(trade["matecoin_price"])
            if trade["bought"]:
                earned_money -= Decimal(trade["bought"]) * price
                matecoin_account += Decimal(trade["bought"])
            if trade["sold"]:
                earned_money += Decimal(trade["sold"]) * price
                matecoin_account -= Decimal(trade["sold"])

        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as profit_file:
            json.dump(profit, profit_file, indent=2)


calculate_profit("trades.json")
