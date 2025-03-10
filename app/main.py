import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:

    with open(filename, "r") as f:
        trades_py = json.load(f)

    earned_money = 0
    matecoin_account = 0

    for trade in trades_py:
        if trade["bought"] is None:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
        elif trade["sold"] is None:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))

        else:
            matecoin_account += (Decimal(trade["bought"])
                                 - Decimal(trade["sold"]))
            earned_money += ((Decimal(trade["sold"])
                              - Decimal(trade["bought"]))
                             * Decimal(trade["matecoin_price"]))

    earned_money = str(earned_money)
    matecoin_account = str(matecoin_account)
    dict_json = dict(earned_money=earned_money,
                     matecoin_account=matecoin_account)

    with open("profit.json", "w") as file:
        json.dump(dict_json, file, indent=2)
