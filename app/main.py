from decimal import Decimal
import json


def calculate_profit(file_name: json):
    with open(file_name, "r") as f:
        trades_data = json.load(f)
    money = Decimal("0")
    amount_crypto = Decimal("0")
    for day in trades_data:
        if day["bought"] is not None:
            spend = Decimal(day["bought"]) * Decimal(day["matecoin_price"])
            money -= spend
            amount_crypto += Decimal(day["bought"])
        if day["sold"] is not None:
            earn_money = Decimal(day["sold"]) * Decimal(day["matecoin_price"])
            money += earn_money
            amount_crypto -= Decimal(day["sold"])
    res = {
        "earned_money": str(money),
        "matecoin_account": str(amount_crypto)
    }
    with open("profit.json", "w") as k:
        json.dump(res, k, indent=2)
