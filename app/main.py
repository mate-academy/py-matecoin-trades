from decimal import Decimal
import json
import os


def calculate_profit(name: str) -> None:
    with open(os.path.name, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade["bought"] is None:
            trade["bought"] = "0"
        if trade["sold"] is None:
            trade["sold"] = "0"

        dec_bought = Decimal(trade["bought"])
        dec_price = Decimal(trade["matecoin_price"])
        dec_sold = Decimal(trade["sold"])

        costs = dec_bought * dec_price
        income = dec_sold * dec_price

        earned_money += income - costs
        matecoin_account += dec_bought - dec_sold

    profit_dict = {"earned_money": f"{earned_money}",
                   "matecoin_account": f"{matecoin_account}"}
    # print(os.getcwd())

    with open("profit.json", "w") as json_file:
        json.dump(profit_dict, json_file, indent=2)
