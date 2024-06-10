import json
from decimal import Decimal


def calculate_profit(path: str, profit_filename: str) -> None:
    with open(path, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"]) if (trade["bought"]
                                              is not None) else Decimal("0")
        sold = Decimal(trade["sold"]) if (trade["sold"]
                                          is not None) else Decimal("0")
        price = Decimal(trade["matecoin_price"])

        matecoin_account += bought
        matecoin_account -= sold
        earned_money -= bought * price
        earned_money += sold * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(profit_filename, "w") as file:
        json.dump(result, file, indent=4)


calculate_profit("trades.json", "profit.json")
