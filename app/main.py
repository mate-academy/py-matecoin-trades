import json

from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)
        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for trade in trades:
            matecoin_price = Decimal(trade["matecoin_price"])
            if trade["bought"]:
                bought_volume_of_coints = Decimal(trade["bought"])
                purchase_cost = bought_volume_of_coints * matecoin_price
                earned_money -= purchase_cost
                matecoin_account += bought_volume_of_coints
            if trade["sold"]:
                sold_volume_of_coints = Decimal(trade["sold"])
                income = sold_volume_of_coints * matecoin_price
                earned_money += income
                matecoin_account -= sold_volume_of_coints

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as output_file:
        json.dump(profit_data, output_file, indent=2)
