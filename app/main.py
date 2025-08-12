import json
import os
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as f:
        trades = json.load(f)

    coin_balance = Decimal("0")
    profit = Decimal("0")

    for trade in trades:
        price = Decimal(str(trade["matecoin_price"]))
        buy_size = Decimal(str(trade["bought"] or "0"))
        sell_size = Decimal(str(trade["sold"] or "0"))

        if buy_size > 0:
            coin_balance += buy_size
            profit -= buy_size * price

        if sell_size > 0:
            coin_balance -= sell_size
            profit += sell_size * price

    data_to_file = {
        "earned_money": str(profit),
        "matecoin_account": str(coin_balance)
    }
    profit_file_path = os.path.join(os.path.dirname(file_name), "profit.json")

    with open(profit_file_path, "w", encoding="utf-8") as file:
        json.dump(data_to_file, file, indent=2)
