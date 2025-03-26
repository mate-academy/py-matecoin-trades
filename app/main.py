# write your code here
import json

from decimal import Decimal


def calculate_profit(filename: json) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade["bought"]:
            bought = Decimal(trade["bought"])
        else:
            bought = Decimal("0")
        if trade["sold"]:
            sold = Decimal(trade["sold"])
        else:
            sold = Decimal("0")

        price = Decimal(trade["matecoin_price"])

        matecoin_account += bought - sold
        earned_money += sold * price - bought * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as output_file:
        json.dump(result, output_file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
