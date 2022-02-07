import json
from decimal import Decimal


def calculate_profit(file_name):
    with open(file_name) as f:
        trades = json.load(f)

    earned_money = 0
    matecoin_account = 0

    for entry in trades:
        matecoin_price = Decimal(entry["matecoin_price"])

        if entry["bought"]:
            earned_money -= Decimal(entry["bought"]) * matecoin_price
            matecoin_account += Decimal(entry["bought"])

        elif entry["sold"]:
            earned_money += Decimal(entry["sold"]) * matecoin_price
            matecoin_account -= Decimal(entry["sold"])

    with open("profit.json", "w") as f:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            f,
            indent=2
        )
