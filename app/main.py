import json
from decimal import Decimal


def calculate_profit(trades_information: str) -> None:
    with open(trades_information, "r") as file:
        trades = json.load(file)
    earned = sum(Decimal(trade["sold"])
                 * Decimal(trade["matecoin_price"])
                 for trade in trades
                 if trade["sold"] is not None
                 ) - sum(Decimal(trade["bought"])
                         * Decimal(trade["matecoin_price"])
                         for trade in trades
                         if trade["bought"] is not None)
    matecoin = sum(Decimal(trade["bought"])
                   for trade in trades
                   if trade["bought"] is not None
                   ) - sum(Decimal(trade["sold"])
                           for trade in trades
                           if trade["sold"] is not None)
    profit = {"earned_money": str(earned),
              "matecoin_account": str(matecoin)}
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
