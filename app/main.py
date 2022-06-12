import json
from decimal import Decimal


def calculate_profit(file_name):
    with open(file_name) as file:
        trades = json.load(file)

    earned_money = 0
    matecoin_account = 0

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            earned_money -= Decimal(trade["bought"]) * matecoin_price
            matecoin_account += Decimal(trade["bought"])

        if trade["sold"]:
            earned_money += Decimal(trade["sold"]) * matecoin_price
            matecoin_account -= Decimal(trade["sold"])

    with open("profit.json", "w") as file:
        return json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            file,
            indent=2
        )
