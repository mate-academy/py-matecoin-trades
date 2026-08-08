import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)
    earned = Decimal(0)
    matecoin_account = Decimal(0)
    for trade in trades:
        if trade["bought"] is not None:
            earned -= (Decimal(trade["bought"])
                       * Decimal(trade["matecoin_price"]))
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"] is not None:
            earned += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            matecoin_account -= Decimal(trade["sold"])
    profit_dict = {
        "earned_money": str(earned),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2)
