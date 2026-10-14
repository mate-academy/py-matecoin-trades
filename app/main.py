from decimal import Decimal
import json


def calculate_profit(file_name: str = "trades.json") -> None:
    with open(file_name, "r", encoding="utf-8") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade.get("bought") is not None:
            bought_amount = Decimal(trade["bought"])
            matecoin_account += bought_amount
            earned_money -= bought_amount * price

        if trade.get("sold") is not None:
            sold_amount = Decimal(trade["sold"])
            matecoin_account -= sold_amount
            earned_money += sold_amount * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    calculate_profit()
