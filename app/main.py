from decimal import Decimal
import json


def calculate_profit(name: str) -> None:
    with open(name, "r") as file:
        trades = json.load(file)
    bought = sum(Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
                 for trade in trades if trade["bought"])
    sold = sum(Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
               for trade in trades if trade["sold"])
    earned_money = (sold - bought)
    account = (sum(Decimal(trade["bought"])
               for trade in trades if trade["bought"])
               - sum(Decimal(trade["sold"])
               for trade in trades if trade["sold"]))
    profit_string = {"earned_money": str(earned_money),
                     "matecoin_account": str(account)}
    with open("profit.json", "w") as profit:
        json.dump(profit_string, profit, indent=2)
