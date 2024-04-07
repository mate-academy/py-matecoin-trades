import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as f:
        trades_data = json.load(f)

    total_profit = Decimal("0.0")
    current_matecoin_balance = Decimal("0.0")

    for trade in trades_data:

        if "bought" in trade and trade["bought"] is not None:
            bought_amount = Decimal(trade["bought"])
            current_matecoin_balance += bought_amount
            total_profit -= bought_amount * Decimal(trade["matecoin_price"])

        if "sold" in trade and trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            current_matecoin_balance -= sold_amount
            total_profit += sold_amount * Decimal(trade["matecoin_price"])

    profit_data = {
        "earned_money": str(total_profit.normalize()),
        "matecoin_account": str(current_matecoin_balance.normalize())
    }

    with open("profit.json", "w") as f:
        json.dump(profit_data, f, ensure_ascii=False, indent=2)
