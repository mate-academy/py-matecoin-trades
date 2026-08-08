import json
from decimal import Decimal, getcontext


def calculate_profit(filename: str) -> None:
    getcontext().prec = 28

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(filename, "r") as file:
        trades = json.load(file)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            volume = Decimal(trade["bought"])
            cost = volume * price
            earned_money -= cost
            matecoin_account += volume

        if trade["sold"]:
            volume = Decimal(trade["sold"])
            revenue = volume * price
            earned_money += revenue
            matecoin_account -= volume

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as outfile:
        json.dump(result, outfile, indent=2)
