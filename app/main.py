import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as f:
        trades = json.load(f)

    coin_balance = Decimal("0")
    avg_buy_price = Decimal("0")
    profit = Decimal("0")

    for trade in trades:
        price = Decimal(str(trade["matecoin_price"]))

        if trade["bought"] > 0:
            buy_size = Decimal(str(trade["bought"]))
            avg_buy_price = (
                (avg_buy_price * coin_balance) + (price * buy_size)
            ) / (coin_balance + buy_size)
            coin_balance += buy_size

        if trade["sold"] > 0:
            sell_size = Decimal(str(trade["sold"]))
            profit += sell_size * (price - avg_buy_price)
            coin_balance -= sell_size

    with open("profit.json", "w") as f:
        json.dump({
            "earned_money": str(profit),
            "matecoin_account": str(coin_balance)
        }, f, indent=2)
