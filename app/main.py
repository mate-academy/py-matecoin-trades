import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        info = json.load(file)

    current_balance = Decimal(0)
    total_bought = Decimal(0)
    total_sold = Decimal(0)

    for trade in info:
        bought_amount = trade.get("bought") or 0
        sold_amount = trade.get("sold") or 0
        matecoin_price = trade.get("matecoin_price") or 0

        if bought_amount:
            current_balance += Decimal(bought_amount)
            total_bought += Decimal(bought_amount) * Decimal(matecoin_price)
        if sold_amount:
            current_balance -= Decimal(sold_amount)
            total_sold += Decimal(sold_amount) * Decimal(matecoin_price)

    earned_money = Decimal(total_sold) - Decimal(total_bought)
    result = {
        "earned_money": f"{Decimal(earned_money)}",
        "matecoin_account": f"{Decimal(current_balance)}"
    }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
