import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as f:
        file_trades = json.load(f)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in file_trades:
        if trade["bought"] is not None:
            earned_money += (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"] is not None:
            earned_money -= (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account -= Decimal(trade["sold"])

    result = {
        "earned_money": str(earned_money * (-1)),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
