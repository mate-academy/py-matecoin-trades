import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as f:
        trades = json.load(f)

    current_coins = Decimal("0")
    profit = Decimal("0")

    for trade in trades:
        price = trade.get("matecoin_price")
        if price is not None:
            price = Decimal(price)
        else:
            continue

        if "bought" in trade and trade["bought"] is not None:
            bought_volume = Decimal(trade["bought"])
            current_coins += bought_volume
            profit -= bought_volume * price

        if "sold" in trade and trade["sold"] is not None:
            sold_volume = Decimal(trade["sold"])
            current_coins -= sold_volume
            profit += sold_volume * price

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(current_coins)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
