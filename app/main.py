import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit = 0
    account = 0
    with open(file_name, "r") as file:
        trades = json.load(file)

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            profit -= bought * matecoin_price
            account += bought
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            profit += sold * matecoin_price
            account -= sold
    profit_dict = {
        "earned_money": str(profit),
        "matecoin_account": str(account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2)
