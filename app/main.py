from decimal import Decimal

import json


def calculate_profit(trades: str = "trades.json") -> None:
    with open(trades) as file_in:
        file_json = json.load(file_in)

    matecoins = 0
    money = 0

    for new_file in file_json:
        if new_file["bought"] is not None:
            matecoins += Decimal(new_file["bought"])
            money -= Decimal(new_file["bought"]) * Decimal(
                new_file["matecoin_price"])
        if new_file["sold"] is not None:
            matecoins -= Decimal(new_file["sold"])
            money += Decimal(new_file["sold"]) * Decimal(
                new_file["matecoin_price"])

    new_file_json = {
        "earned_money": str(money),
        "matecoin_account": str(matecoins)
    }
    with open("profit.json", "a") as file_out:
        json.dump(new_file_json, file_out, indent=2)
