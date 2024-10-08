import json
from decimal import Decimal


def calculate_profit(file_name: str) -> Decimal:
    with open(file_name, "r") as trades_file:
        trades = json.load(trades_file)
    spended_money = 0
    recieved_money = 0
    coins = 0
    for trade in trades:
        if trade["bought"]:
            spended_money += (Decimal(trade["bought"])
                              * Decimal(trade["matecoin_price"]))
            coins += Decimal(trade["bought"])
        if trade["sold"]:
            recieved_money += (Decimal(trade["sold"])
                               * Decimal(trade["matecoin_price"]))
            coins -= Decimal(trade["sold"])
    with open("profit.json", "w") as profit:
        json.dump({
            "earned_money": str(recieved_money - spended_money),
            "matecoin_account": str(coins),
        }, profit, indent=2)
