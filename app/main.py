import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(filename, "r") as file:
        trades = json.load(file)

    for trade in trades:
        bought = trade["bought"]
        sold = trade["sold"]
        price = Decimal(trade["matecoin_price"])

        if bought is not None:
            coins = Decimal(bought)

            matecoin_account += coins
            earned_money -= coins * price

        if sold is not None:
            coins = Decimal(sold)

            matecoin_account -= coins
            earned_money += coins * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)


calculate_profit("app/trades.json")
