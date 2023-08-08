import json
from decimal import Decimal


def calculate_profit(files_name: str) -> None:
    with open(files_name, "r") as file:
        trades = json.load(file)

    earned_money = 0
    matecoin_account = 0

    for trade in trades:
        if trade["bought"] is not None and trade["sold"] is None:
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account += (Decimal(trade["bought"]))
        elif trade["sold"] is not None and trade["bought"] is None:
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account -= (Decimal(trade["sold"]))
        else:
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"])) - \
                            (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))

            matecoin_account += (Decimal(trade["bought"])
                                 - Decimal(trade["sold"]))

    with open("profit.json", "w") as profit_file:
        json.dump({"earned_money": str(Decimal(earned_money)),
                   "matecoin_account": str(Decimal(matecoin_account))},
                  profit_file, indent=2)
