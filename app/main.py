import json
from decimal import Decimal


def calculate_profit(filename: json) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(filename, "r") as file:
        trades = json.load(file)

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought:
            bought = Decimal(bought)
            earned_money -= bought * matecoin_price
            matecoin_account += bought

        if sold:
            sold = Decimal(sold)
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    res = {"earned_money": earned_money,
           "matecoin_account": matecoin_account}
    with open("profit.json", "w") as file:
        json.dump(res, file, indent=2)
