import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    total_profit = Decimal("0.00")
    current_balance = Decimal("0.00")
    for trade in trades:
        if "bought" in trade and trade["bought"]:
            total_profit -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
        if "sold" in trade and trade["sold"]:
            total_profit += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            current_balance -= Decimal(trade["sold"])

    result = {
        "earned_money": str(total_profit),
        "current_balance": str(current_balance)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file)
