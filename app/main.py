import json
import decimal
import os


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r", encoding="utf-8") as file_2:
        file_1 = json.load(file_2)
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    for item in file_1:

        bought = decimal.Decimal(item["bought"]) \
            if item["bought"] \
            else decimal.Decimal("0")
        sold = decimal.Decimal(item["sold"]) \
            if item["sold"] \
            else decimal.Decimal("0")
        matecoin_price = decimal.Decimal(item["matecoin_price"])

        if bought is not None:
            earned_money -= bought * matecoin_price
            matecoin_account += bought
        if sold is not None:
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    base_dir = os.path.dirname(os.path.dirname(file_name))
    profit_path = os.path.join(base_dir, "profit.json")

    with open(profit_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
