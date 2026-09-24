import json
from decimal import Decimal


def calculate_profit(file_name: str) -> any:
    with open(file_name) as file:
        user_date = json.load(file)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in user_date:
        price = Decimal(trade["matecoin_price"])
        if trade.get("bought"):
            brought = Decimal(trade["bought"])
            matecoin_account += brought
            earned_money -= brought * price
        if trade.get("sold"):
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * price
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }
    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
