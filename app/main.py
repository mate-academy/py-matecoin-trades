from decimal import Decimal
import json


def calculate_profit(name: str) -> None:

    profit = {
        "bought": Decimal("0"),
        "sold": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    with open(name, "r") as f:
        trades_data = json.load(f)

    for part in trades_data:

        current_price = Decimal(part.get("matecoin_price"))

        if part.get("bought"):
            current_bought = Decimal(part.get("bought"))
            profit["matecoin_account"] += current_bought
            profit["bought"] += current_price * current_bought

        if part.get("sold"):
            current_sold = Decimal(part.get("sold"))
            profit["matecoin_account"] -= current_sold
            profit["sold"] += current_price * current_sold

    total_earn = profit.get("sold") - profit.get("bought")
    result = {
        "earned_money": str(total_earn),
        "matecoin_account": str(profit.get("matecoin_account"))
    }

    with open("profit.json", "w") as new_file:
        json.dump(result, new_file, indent=2)
