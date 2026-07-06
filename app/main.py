import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    total_money = Decimal()
    coin_account = Decimal()
    with open(file_name, "r") as file:
        matecoin_trades = json.load(file)
    for trade in matecoin_trades:
        if trade["bought"]:
            coin_account += Decimal(trade["bought"])
            total_money -= (Decimal(trade["matecoin_price"])
                            * Decimal(trade["bought"]))
        if trade["sold"]:
            total_money += (Decimal(trade["matecoin_price"])
                            * Decimal(trade["sold"]))
            coin_account -= Decimal(trade["sold"])
    with open("profit.json", "w") as file:
        json.dump({"earned_money": str(total_money),
                   "matecoin_account": str(coin_account)}, file, indent=2)
