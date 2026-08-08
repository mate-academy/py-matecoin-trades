import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    with open(filename, "r") as file:
        open_file = json.load(file)

    print(open_file)

    for trade in open_file:
        if trade["bought"] is not None:
            earned_money = (Decimal(earned_money) - Decimal(trade["bought"])
                            * Decimal(trade["matecoin_price"]))
            matecoin_account = (Decimal(matecoin_account)
                                + Decimal(trade["bought"]))
        if trade["sold"] is not None:
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account -= Decimal(trade["sold"])

    profit_dictionary = {"earned_money": str(earned_money),
                         "matecoin_account": str(matecoin_account)}
    profit = json.dumps(profit_dictionary)
    print(profit)

    with open("profit.json", "w") as file:
        json.dump(profit_dictionary, file, indent=2)
