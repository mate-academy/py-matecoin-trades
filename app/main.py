import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")

        earned_money += (sold * price) - (bought * price)
        matecoin_account += bought - sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
