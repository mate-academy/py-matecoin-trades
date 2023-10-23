import decimal
import json


def calculate_profit(name: str) -> None:
    profit = {
        "bought": decimal.Decimal("0"),
        "sold": decimal.Decimal("0"),
        "matecoin_account": decimal.Decimal("0")
    }
    with open(name, "r") as file:
        content_of_file = json.load(file)

    for element in content_of_file:
        current_price = decimal.Decimal(element.get("matecoin_price"))

        if element.get("bought"):
            bought_price = decimal.Decimal(element.get("bought"))
            profit["matecoin_account"] += bought_price
            profit["bought"] += current_price * bought_price

        if element.get("sold"):
            sold_price = decimal.Decimal(element.get("sold"))
            profit["matecoin_account"] -= sold_price
            profit["sold"] += current_price * sold_price

        total_profit = profit.get("sold") - profit.get("bought")
        result = {
            "earned_money": str(total_profit),
            "matecoin_account": str(profit.get("matecoin_account"))
        }

        with open("profit.json", "w") as new_file:
            json.dump(result, new_file, indent=2)
