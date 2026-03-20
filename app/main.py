import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(name_file, "r") as traders_file:
        traders = json.load(traders_file)

        for trade in traders:
            price = Decimal(trade["matecoin_price"])

            if trade["bought"] is not None:
                volume = Decimal(trade["bought"])
                earned_money -= volume * price
                matecoin_account += volume

            if trade["sold"] is not None:
                volume = Decimal(trade["sold"])
                earned_money += volume * price
                matecoin_account -= volume

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file, indent=2)
