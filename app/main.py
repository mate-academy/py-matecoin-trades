import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        profits = json.load(file)

    earned_money = 0
    matecoin_account = 0
    for profit in profits:
        if profit["bought"]:
            bought = Decimal(profit["bought"])
            matecoin_account += bought
            total_bought = bought * Decimal(profit["matecoin_price"])
            earned_money -= total_bought

        if profit["sold"]:
            sold = Decimal(profit["sold"])
            matecoin_account -= sold
            total_sold = sold * Decimal(profit["matecoin_price"])
            earned_money += total_sold

    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2)
