import json

from decimal import Decimal


def calculate_profit(trade_statistics: str) -> None:
    with open(trade_statistics, "r", encoding="utf-8") as file:
        data = json.load(file)

    profit = 0
    matecoin_count = 0

    for trade in data:

        if trade["sold"] is not None:
            matecoin_count -= Decimal(trade["sold"])
            profit += (Decimal(trade["sold"])
                       * Decimal(trade["matecoin_price"]))

        if trade["bought"] is not None:
            matecoin_count += Decimal(trade["bought"])
            profit -= (Decimal(trade["bought"])
                       * Decimal(trade["matecoin_price"]))

    with open("profit.json", "w") as file:
        nafarmil = {
            "earned_money": str(profit),
            "matecoin_account": str(matecoin_count)
        }

        json.dump(nafarmil, file, indent=2)
