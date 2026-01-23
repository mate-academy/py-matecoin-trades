import json
from decimal import Decimal


def calculate_profit(name_of_file: str) -> None:
    with open(name_of_file, "r") as f:
        trading_data = json.load(f)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trading_data:
        if trade["bought"] is not None:
            rate = Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            matecoin_account += Decimal(trade["bought"])
            earned_money -= rate

        if trade["sold"] is not None:
            rate = Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            matecoin_account -= Decimal(trade["sold"])
            earned_money += rate

    profit_data = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as f:
        json.dump(profit_data, f, indent=2)
