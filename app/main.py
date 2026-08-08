import json
from decimal import Decimal


def calculate_profit(file_name):
    with open(file_name, "r") as file_read:
        trades_data = json.load(file_read)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trades_data:
        current_matecoin = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            earned_money -= Decimal(trade["bought"]) * current_matecoin
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"] is not None:
            earned_money += Decimal(trade["sold"]) * current_matecoin
            matecoin_account -= Decimal(trade["sold"])

    with open("profit.json", "w") as file_write:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account),
            },
            file_write,
            indent=2)
