import json
from decimal import Decimal


def calculate_profit(json_file):

    with open(json_file) as file_in:
        trade_list = json.load(file_in)
        earned_money = 0
        matecoin_account = 0

        for trade in trade_list:
            coin_price = Decimal(trade["matecoin_price"])
            if trade["sold"]:
                earned_money += Decimal(trade["sold"]) * coin_price
                matecoin_account -= Decimal(trade["sold"])

            if trade["bought"]:
                earned_money -= Decimal(trade["bought"]) * coin_price
                matecoin_account += Decimal(trade["bought"])

        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open("profit.json", "w") as file_out:
            json.dump(profit, file_out, indent=2)
