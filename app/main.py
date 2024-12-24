
import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    with open(trades_file, "r") as file:
        trades = json.load(file)

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * matecoin_price
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * matecoin_price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as output_file:
        json.dump(result, output_file)
#


calculate_profit("trades.json")
