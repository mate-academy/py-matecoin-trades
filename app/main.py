import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    matecoin_account = Decimal(0)
    earned_money = Decimal(0)

    with open(trades, "r") as file:
        trades_data = json.load(file)

        for trade in trades_data:
            bought = trade["bought"]
            sold = trade["sold"]
            matecoin_price = trade["matecoin_price"]

            if sold:
                earned_money += Decimal(sold) * Decimal(matecoin_price)
                matecoin_account += Decimal(sold)

            if bought:
                earned_money -= Decimal(bought) * Decimal(matecoin_price)
                matecoin_account -= Decimal(bought)

    final_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(-matecoin_account)
    }

    with open("profit.json", "w") as file1:
        json.dump(final_dict, file1, indent=2)
