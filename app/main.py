import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    with open(name) as data:
        trade_data = json.load(data)

    matecoin_account = 0
    earned_money = 0
    for day in trade_data:

        if day["bought"]:
            bought = Decimal(day["bought"])
            price = Decimal(day["matecoin_price"])
            matecoin_account += bought
            earned_money -= price * bought

        if day["sold"]:
            sold = Decimal(day["sold"])
            price = Decimal(day["matecoin_price"])
            matecoin_account -= sold
            earned_money += price * sold

    with (open("profit.json", "w") as profit):
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            profit,
            indent=2
        )
