import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal(0)
    matecoins = Decimal(0)
    with open(filename, "r") as file:
        trades = json.load(file)
        for trade in trades:
            if trade["bought"] is None:
                bought = Decimal(0)
            else:
                bought = Decimal(trade["bought"])
            if trade["sold"] is None:
                sold = Decimal(0)
            else:
                sold = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])

            earned_money += (sold * price) - (bought * price)
            matecoins += bought - sold

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoins)
        }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
