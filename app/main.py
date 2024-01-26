import json
from decimal import Decimal


def calculate_profit(f_name: str) -> None:
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    with open(f_name, "r") as file:
        data = json.load(file)

        for trans in data:
            sold = trans["sold"]
            coin_price = trans["matecoin_price"]
            bought = trans["bought"]

            if trans["sold"] is not None:
                earned_money += Decimal(sold) * Decimal(coin_price)
                matecoin_account -= Decimal(sold)
            if trans["bought"] is not None:
                earned_money -= Decimal(bought) * Decimal(coin_price)
                matecoin_account += Decimal(bought)

    profit = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
