import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        matecoin_bought = Decimal("0")
        matecoin_sold = Decimal("0")
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            matecoin_bought = Decimal(trade["bought"])
        if trade["sold"]:
            matecoin_sold = Decimal(trade["sold"])

        earned_money += (matecoin_sold - matecoin_bought) * matecoin_price
        matecoin_account += matecoin_bought - matecoin_sold

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as outfile:
        json.dump(profit_data, outfile, indent=2)
