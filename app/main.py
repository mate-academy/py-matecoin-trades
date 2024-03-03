import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    earned = 0
    account = 0

    for trade in trades:
        if trade["bought"]:
            bought_volume = Decimal(trade["bought"])
            account += bought_volume
            earned -= (bought_volume * Decimal(trade["matecoin_price"]))

        if trade["sold"]:
            sold_volume = Decimal(trade["sold"])
            account -= sold_volume
            earned += (sold_volume * Decimal(trade["matecoin_price"]))

    result = {
        "earned_money": str(earned),
        "matecoin_account": str(account)
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
