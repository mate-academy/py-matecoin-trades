import json

from decimal import Decimal


def calculate_profit(file_name):
    with open(file_name, "r") as f:
        trade_info = json.load(f)

    update_data = {
        "earned_money": Decimal("0.0"),
        "matecoin_account": Decimal("0.0")
    }

    for trade in trade_info:
        if trade["bought"]:
            update_data["earned_money"] -=\
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            update_data["matecoin_account"] += Decimal(trade["bought"])

        if trade["sold"]:
            update_data["earned_money"] +=\
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            update_data["matecoin_account"] -= Decimal(trade["sold"])

    with open(file_name, "a") as f:
        json.dump(update_data, f, indent=2)
