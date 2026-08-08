import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades_data = json.load(file)

    balance = 0
    for trade in trades_data:
        if trade["bought"]:
            balance -= (Decimal(trade["bought"])
                        * Decimal(trade["matecoin_price"]))
        if trade["sold"]:
            balance += (Decimal(trade["sold"])
                        * Decimal(trade["matecoin_price"]))

    bought = sum(Decimal(trade["bought"])
                 for trade in trades_data
                 if trade["bought"])

    sold = sum(Decimal(trade["sold"])
               for trade in trades_data
               if trade["sold"])

    profit = {"earned_money": str(balance),
              "matecoin_account": str(bought - sold)}

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
