from decimal import Decimal
import json


def calculate_profit(trades) -> None:
    with open(trades, "r") as file_in:
        trades_data = json.load(file_in)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        coin_price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            earned_money -= bought * coin_price
            matecoin_account += bought
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            earned_money += sold * coin_price
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file_out:
        json.dump(result, file_out, indent=2)
