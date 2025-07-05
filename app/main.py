import json
from decimal import Decimal


def calculate_profit(filename: str = "trades.json") -> None:
    with open(filename, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought_str = trade.get("bought")
        sold_str = trade.get("sold")
        price = Decimal(trade["matecoin_price"])

        if bought_str is not None:
            bought = Decimal(bought_str)
            matecoin_account += bought
            earned_money -= price * bought

        if sold_str is not None:
            sold = Decimal(sold_str)
            matecoin_account -= sold
            earned_money += price * sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
