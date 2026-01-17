import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    result = {
        "earned_money" : Decimal(0),
        "matecoin_account" : Decimal(0)
    }

    with open(file=file_name, mode="r") as file:
        trades = json.load(file)

        for trade in trades:
            price = Decimal(trade["matecoin_price"])

            if trade.get("bought"):
                bought_qty = Decimal(trade["bought"])
                result["earned_money"] -= Decimal(bought_qty * price)
                result["matecoin_account"] += Decimal(bought_qty)

            if trade.get("sold"):
                sold_qty = Decimal(trade["sold"])
                result["earned_money"] += Decimal(sold_qty * price)
                result["matecoin_account"] -= Decimal(sold_qty)

    file_content = {
        "earned_money" : str(result["earned_money"]),
        "matecoin_account" : str(result["matecoin_account"])
    }

    with open(file="profit.json", mode="w") as file:
        json.dump(file_content, file, indent=4)
