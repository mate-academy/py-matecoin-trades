import json
from decimal import Decimal


def calculate_profit(trades_filename: json) -> None:
    with open(trades_filename, "r") as trades_file:
        trades_dict = json.load(trades_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_dict:
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            spent = bought * matecoin_price
            earned_money -= spent
            matecoin_account += bought
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit_data, profit_file, indent=2)
