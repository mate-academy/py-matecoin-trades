import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(filename, "r", encoding="utf-8") as f:
        trades = json.load(f)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            volume = Decimal(trade["bought"])
            earned_money -= volume * price
            matecoin_account += volume
        if trade["sold"]:
            volume = Decimal(trade["sold"])
            earned_money += volume * price
            matecoin_account -= volume

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
