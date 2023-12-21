import json
from decimal import Decimal
from os import path


def calculate_profit(file_name: str) -> None:
    with open(path.join(path.dirname(path.abspath(__file__)),
                        file_name), "r") as f:
        trades = json.load(f)
        print(trades, type(trades))
        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for trade in trades:
            bought = trade["bought"]
            sold = trade["sold"]
            matecoin_price = trade["matecoin_price"]
            print(type(matecoin_price))
            if bought:
                earned_money -= (Decimal(bought)
                                 * Decimal(matecoin_price))
                matecoin_account += Decimal(bought)
            elif sold:
                earned_money += Decimal(sold) * Decimal(matecoin_price)
                matecoin_account -= Decimal(sold)
        print(earned_money)
        print(matecoin_account)


calculate_profit("trades.json")
