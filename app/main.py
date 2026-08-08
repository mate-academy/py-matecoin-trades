import json

from decimal import Decimal


def calculate_profit(json_file):

    earned_money = 0
    matecoin_account = 0

    with open(json_file) as file_in:
        trades_list = json.load(file_in)

    for trade in trades_list:
        coin_price = Decimal(trade["matecoin_price"])
        if trade["sold"] is not None:
            earned_money += Decimal(trade["sold"]) * coin_price
            matecoin_account -= Decimal(trade["sold"])
        if trade["bought"] is not None:
            earned_money -= Decimal(trade["bought"]) * coin_price
            matecoin_account += Decimal(trade["bought"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file_out:
        json.dump(profit, file_out, indent=2)
