import json

from decimal import Decimal


def calculate_profit(file_name):
    with open(file_name, "r") as f:
        trade_info = json.load(f)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trade_info:
        if trade["bought"]:
            earned_money -= \
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            matecoin_account += Decimal(trade["bought"])

        if trade["sold"]:
            earned_money += \
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            matecoin_account -= Decimal(trade["sold"])

    update_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(file_name, "a") as f:
        json.dump(update_data, f, indent=2)
