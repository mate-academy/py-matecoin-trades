import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = trade.get("bought")
        sold = trade.get("sold")

        if bought is not None:
            bought_amount = Decimal(bought)
            earned_money -= bought_amount * price
            matecoin_account += bought_amount

        if sold is not None:
            sold_amount = Decimal(sold)
            earned_money += sold_amount * price
            matecoin_account -= sold_amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
