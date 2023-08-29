import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as d1:
        list_of_dict = json.load(d1)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in list_of_dict:
        bought, sold, matecoin_price = trade.values()
        if bought:
            earned_money -= Decimal(bought) * Decimal(matecoin_price)
            matecoin_account += Decimal(bought)
        if sold:
            earned_money += Decimal(sold) * Decimal(matecoin_price)
            matecoin_account -= Decimal(sold)
    profit = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
