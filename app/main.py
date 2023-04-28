import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    spent_money = Decimal()
    earned_money = Decimal()
    coins = Decimal()
    with open(trades, "r") as data, open("profit.json", "w") as profit:
        for i in json.load(data):
            if i["bought"]:
                spent_money += \
                    Decimal(i["bought"]) * Decimal(i["matecoin_price"])
                coins += Decimal(i["bought"])
            if i["sold"]:
                earned_money += \
                    Decimal(i["sold"]) * Decimal(i["matecoin_price"])
                coins -= Decimal(i["sold"])
    json.dump({"earned_money": str(earned_money - spent_money),
               "matecoin_account": str(coins)}, profit, indent=2)
