from json import load, dump
from decimal import Decimal


def calculate_profit(file):
    with open(file, "r") as file:
        trades = load(file)

    earned_money = 0
    matecoin_account = 0

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            earned_money += Decimal(trade["bought"]) * price
            matecoin_account += Decimal(trade["bought"])

        if trade["sold"]:
            earned_money -= Decimal(trade["sold"]) * price
            matecoin_account -= Decimal(trade["sold"])

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as output_file:
        dump(result, output_file)
