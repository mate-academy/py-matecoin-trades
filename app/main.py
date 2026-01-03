from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        trades = json.load(file)

    buy_amount = Decimal(0)
    sell_amount = Decimal(0)
    matecoin_amount = Decimal(0)

    for trade in trades:
        if trade.get("bought"):
            bought = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            buy_amount += bought * price
            matecoin_amount += Decimal(trade["bought"])
        if trade.get("sold"):
            sold = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            sell_amount += sold * price
            matecoin_amount -= Decimal(trade["sold"])

    result = {
        "earned_money": str(sell_amount - buy_amount),
        "matecoin_account": str(matecoin_amount)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
