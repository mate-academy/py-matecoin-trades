import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    money = Decimal("0")
    coins = Decimal("0")

    for trade in trades:
        if trade["bought"]:
            coins += Decimal(trade["bought"])
            money -= (Decimal(trade["bought"])
                      * Decimal(trade["matecoin_price"]))

        if trade["sold"]:
            coins -= Decimal(trade["sold"])
            money += (Decimal(trade["sold"])
                      * Decimal(trade["matecoin_price"]))

    result = {
        "earned_money": str(money),
        "matecoin_account": str(coins)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
