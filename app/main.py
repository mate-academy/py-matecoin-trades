import json
from decimal import Decimal


def calculate_profit(trades_information: str) -> None:
    with open(trades_information, "r") as file:
        trades = json.load(file)
    bought = sum(Decimal(trade["bought"])
                 for trade in trades if trade["bought"] is not None)
    sold = sum(Decimal(trade["sold"])
               for trade in trades if trade["sold"] is not None)
    earned_mon = sum(Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
                     for trade in trades if trade["sold"] is not None)
    spent_mon = sum(Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
                    for trade in trades if trade["bought"] is not None)
    earned_mon -= spent_mon
    matecoin_account = bought - sold
    profit_json = {
        "earned_money": str(earned_mon),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(profit_json, file, indent=2)
