import json
from decimal import Decimal
from os import path


def calculate_profit(file_name: str) -> None:
    current_directory = path.dirname(path.abspath(__file__))
    with open(path.join(current_directory, file_name), "r") as f:
        trades = json.load(f)
        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for trade in trades:
            bought = trade["bought"]
            sold = trade["sold"]
            matecoin_price = trade["matecoin_price"]
            if bought:
                earned_money -= (Decimal(bought)
                                 * Decimal(matecoin_price))
                matecoin_account += Decimal(bought)
            if sold:
                earned_money += Decimal(sold) * Decimal(matecoin_price)
                matecoin_account -= Decimal(sold)

        result = {"earned_money": str(earned_money),
                  "matecoin_account": str(matecoin_account)}

        with open("profit.json", "w") as f_profit:
            json.dump(result, f_profit, indent=2)


calculate_profit("trades.json")
