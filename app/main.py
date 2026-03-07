import json
import sys
from decimal import Decimal


def calculate_profit(f_name: str) -> None:
    with open(f_name, "r") as file:
        data = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in data:
        price = Decimal(trade["matecoin_price"])
        bought = Decimal(trade["bought"]) if trade["bought"] is not None else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] is not None else Decimal("0")

        matecoin_account += bought - sold

        earned_money += sold * price - price * bought

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)

if __name__ == "__main__":
    calculate_profit(sys.argv[1])
