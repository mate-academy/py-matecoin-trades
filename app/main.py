import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    balance = {
        "earned_money": Decimal(0),
        "matecoin_account": Decimal(0)
    }

    with open(file_name) as f:
        trades = json.load(f)

    for trade in trades:
        if trade["bought"]:
            bought = Decimal(str(trade["bought"]))
            matecoin_price = Decimal(str(trade["matecoin_price"]))
            profit = bought * matecoin_price
            balance["earned_money"] -= profit
            balance["matecoin_account"] += bought

        if trade["sold"]:
            sold = Decimal(str(trade["sold"]))
            matecoin_price = Decimal(str(trade["matecoin_price"]))
            profit = sold * matecoin_price
            balance["earned_money"] += profit
            balance["matecoin_account"] -= sold

    balance["earned_money"] = str(balance["earned_money"])
    balance["matecoin_account"] = str(balance["matecoin_account"])

    with open("profit.json", "w") as f:
        json.dump(balance, f, indent=2)
