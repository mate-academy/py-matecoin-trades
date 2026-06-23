import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file) as input_file:
        trades = json.load(input_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            bought = Decimal(trade["bought"])
            earned_money -= price * bought
            matecoin_account += bought

        if trade["sold"]:
            sold = Decimal(trade["sold"])
            earned_money += sold * price
            matecoin_account -= sold

    with open("profit.json", "w") as output_file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account),
            },
            output_file,
            indent=2,
        )
