from decimal import Decimal

import json


def calculate_profit(file_name):
    with open(file_name) as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
                if trade["sold"]:
            earned_money += Decimal(trade["sold"]) * \
                            Decimal(trade["matecoin_price"])
            matecoin_account -= Decimal(trade["sold"])
        else:
            earned_money -= Decimal(trade["sold"]) * \
                            Decimal(trade["matecoin_price"])
            matecoin_account += Decimal(trade["sold"])

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
