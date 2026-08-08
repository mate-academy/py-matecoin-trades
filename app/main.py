import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    balance = 0
    matecoin_account = 0

    for trade in trades:
        if trade["bought"]:
            amount_to_buy = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            balance -= amount_to_buy * price
            matecoin_account += amount_to_buy

        if trade["sold"]:
            amount_to_sell = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            balance += amount_to_sell * price
            matecoin_account -= amount_to_sell

    profit_dict = {
        "earned_money": str(balance),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2)
