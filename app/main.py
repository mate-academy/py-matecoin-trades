import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0"),
    }

    with open(file_name, "r") as file:
        data = json.load(file)

    for info in data:
        bought = info["bought"]
        sold = info["sold"]
        price = Decimal(info["matecoin_price"])

        if bought is not None:
            # Купівля
            profit["matecoin_account"] += Decimal(bought)
            profit["earned_money"] -= Decimal(bought) * price

        if sold is not None:
            # Продаж
            profit["matecoin_account"] -= Decimal(sold)
            profit["earned_money"] += Decimal(sold) * price

    # Перетворюємо у str для JSON
    profit = {k: str(v) for k, v in profit.items()}

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
