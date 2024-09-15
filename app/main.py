import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    result = {"earned_money": Decimal("0"),
              "matecoin_account": Decimal("0")}

    with open(file_name, "r") as f:
        data = json.load(f)

    for day in data:
        bought, sold, matecoin_price = day.values()
        if bought:
            result["earned_money"] -= Decimal(bought) * Decimal(matecoin_price)
            result["matecoin_account"] += Decimal(bought)
        if sold:
            result["earned_money"] += Decimal(sold) * Decimal(matecoin_price)
            result["matecoin_account"] -= Decimal(sold)

    with open("profit.json", "w") as f:
        json.dump({key: str(val) for key, val in result.items()}, f, indent=2)
