import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    profit = Decimal("0")
    matecoin_balanse = Decimal("0")

    for trade in trades:
        if trade["bought"]:
            bought_volume = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            profit -= bought_volume * matecoin_price
            matecoin_balanse += bought_volume
        if trade["sold"]:
            sold_volume = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            profit += sold_volume * matecoin_price
            matecoin_balanse -= sold_volume

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_balanse)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
