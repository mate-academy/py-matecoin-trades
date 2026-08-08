import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as trad:
        trades = json.load(trad)
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
        profit = {
            "earned_money": str(money),
            "matecoin_account": str(coins)
        }
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
