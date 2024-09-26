from decimal import Decimal
import json


def calculate_profit(file_name: str):
    with open(file_name) as f:
        trades = json.load(f)

    earned_money = Decimal()
    matecoin_account = Decimal()

    for trade in trades:
        if trade["bought"]:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= Decimal(trade["bought"]) * \
                Decimal(trade["matecoin_price"])

        if trade["sold"]:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += Decimal(trade["sold"]) * \
                Decimal(trade["matecoin_price"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
