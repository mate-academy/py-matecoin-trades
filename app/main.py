from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as read_file:
        trades = json.load(read_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= Decimal(trade["bought"]) * price
        if trade["sold"] is not None:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += Decimal(trade["sold"]) * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as write_file:
        json.dump(result, write_file, indent=2)
