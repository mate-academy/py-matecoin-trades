import json
from decimal import Decimal


def calculate_profit(name_of_file: str) -> None:

    with open(name_of_file, "r") as json_file:
        trades = json.load(json_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (
                Decimal(trade["bought"])
                * Decimal(trade["matecoin_price"])
            )

        if trade["sold"] is not None:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (
                Decimal(trade["sold"])
                * Decimal(trade["matecoin_price"])
            )

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as json_file:
        json.dump(result, json_file, indent=2)
