import json
from decimal import Decimal


def calculate_profit(file_name: str) -> float:
    with open(file_name, "r", encoding="utf-8") as f:
        data = json.load(f)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for entry in data:

        bought = (
            Decimal(entry["bought"]) if entry["bought"] is not None
            else Decimal("0")
        )
        sold = (
            Decimal(entry["sold"]) if entry["sold"] is not None
            else Decimal("0")
        )
        price = Decimal(entry["matecoin_price"])

        matecoin_account += bought
        matecoin_account -= sold
        earned_money -= bought * price
        earned_money += sold * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
