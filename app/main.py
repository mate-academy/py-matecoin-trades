import json
from decimal import Decimal


def calculate_profit(path: str) -> None:
    with open(path, "r") as file:
        earned_money = 0
        matecoin_account = 0
        trades = json.load(file)
        for trade in trades:
            for action, cost in trade.items():
                if action == "bought" and cost is not None:
                    bought = Decimal(trade["bought"])
                    price = Decimal(trade["matecoin_price"])
                    matecoin_account += bought
                    earned_money -= bought * price
                elif action == "sold" and cost is not None:
                    sold = Decimal(trade["sold"])
                    price = Decimal(trade["matecoin_price"])
                    matecoin_account -= sold
                    earned_money += sold * price
    with open("profit.json", "w") as new_file:
        json.dump({"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)},
                  new_file,
                  indent=2)
