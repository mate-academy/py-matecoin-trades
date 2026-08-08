from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        data = json.load(f)
    money = Decimal("0")
    mate_coins = Decimal("0")
    for item in data:
        matecoin_price = Decimal(item["matecoin_price"])
        if item.get("bought") and item["bought"] != "null":
            amount = Decimal(item["bought"])
            mate_coins += amount
            money -= amount * matecoin_price
        if item.get("sold") and item["sold"]:
            amount = Decimal(item["sold"])
            mate_coins -= amount
            money += amount * matecoin_price
    with open("profit.json", "w") as f:
        result = {
            "earned_money": str(money),
            "matecoin_account": str(mate_coins)
        }
        json.dump(result, f, indent=2)
