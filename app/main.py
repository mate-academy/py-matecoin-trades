import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    spended_money = 0
    recieved_money = 0
    coins = 0

    with open(file_name, "r") as trades_file:
        trades = json.load(trades_file)

    for trade in trades:
        if trade["bought"]:
            coins += Decimal(trade["bought"])
            spended_money += (Decimal(trade["bought"])
                              * Decimal(trade["matecoin_price"]))
        if trade["sold"]:
            coins -= Decimal(trade["sold"])
            recieved_money += (Decimal(trade["sold"])
                               * Decimal(trade["matecoin_price"]))

    with open("profit.json", "w") as profit:
        json.dump({
            "earned_money": str(recieved_money - spended_money),
            "matecoin_account": str(coins),
        }, profit, indent=2)
