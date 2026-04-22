import json

from decimal import Decimal


def calculate_profit(trades_info: str) -> None:
    with open(trades_info, "r") as trade:
        trades = json.load(trade)

    balance = Decimal(0.0)
    spent = Decimal(0.0)
    earning = Decimal(0.0)

    for trade in trades:
        if not trade["bought"] is None:
            balance += Decimal(trade["bought"])
            spent += (Decimal(trade["bought"])
                      * Decimal(trade["matecoin_price"]))
        if not trade["sold"] is None:
            balance -= Decimal(trade["sold"])
            earning += (Decimal(trade["sold"])
                        * Decimal(trade["matecoin_price"]))

    earned = Decimal(earning) - Decimal(spent)
    profit = {
        "earned_money": str(earned),
        "matecoin_account": str(balance)
    }

    with open("profit.json", "a") as result_file:
        json.dump(profit, result_file, indent=2)
