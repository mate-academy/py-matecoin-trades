import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trading_data = json.load(file)

    earned_money = 0
    mc_account = 0

    for trade in trading_data:
        mc_price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            bought = Decimal(trade["bought"])
            earned_money -= mc_price * bought
            mc_account += bought

        if trade["sold"]:
            sold = Decimal(trade["sold"])
            earned_money += mc_price * sold
            mc_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(mc_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
