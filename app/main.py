import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade.get("bought"):
            volume = Decimal(trade["bought"])
            matecoin_account += volume
            earned_money -= volume * price

        if trade.get("sold"):
            volume = Decimal(trade["sold"])
            matecoin_account -= volume
            earned_money += volume * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
