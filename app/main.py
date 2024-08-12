import os
import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    # Використання абсолютного шляху
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    total_spent = Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            bought_amount = Decimal(trade["bought"])
            matecoin_account += bought_amount
            total_spent += bought_amount * Decimal(trade["matecoin_price"])
        if trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            earned_money += sold_amount * Decimal(trade["matecoin_price"])
            matecoin_account -= sold_amount

    # Вираховуємо чистий прибуток
    net_profit = earned_money - total_spent

    profit_data = {
        "earned_money": str(net_profit),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
