import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:

        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_amount = Decimal(trade["bought"])
            earned_money -= bought_amount * matecoin_price
            matecoin_account += bought_amount

        if trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            earned_money += sold_amount * matecoin_price
            matecoin_account -= sold_amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    output_path = "C:\\Users\\user\\projects\\py-matecoin-trades/profit.json"

    with open(output_path, "w") as file:
        json.dump(result, file, indent=2)
