import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    with open(name) as file_in:
        traders = json.load(file_in)
    matecoin_account = Decimal("0.0")
    earned_money = Decimal("0.0")
    for dct in traders:
        if dct["bought"] is not None:
            bought_amount = Decimal(dct["bought"])
            matecoin_account += bought_amount
            earned_money -= (bought_amount
                             * Decimal(dct["matecoin_price"]))
    for dct in traders:
        if dct["sold"] is not None:
            sold_amount = Decimal(dct["sold"])
            matecoin_account -= sold_amount
            earned_money += (sold_amount
                             * Decimal(dct["matecoin_price"]))

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file_out:
        json.dump(profit, file_out, indent=2)
