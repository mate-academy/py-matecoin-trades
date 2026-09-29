import json
from decimal import Decimal


def calculate_profit(new_file: str) -> None:
    with open(new_file) as f:
        trades = json.load(f)
    money = Decimal(0)
    coin = Decimal(0)
    for item in trades:
        if item["bought"] is not None:
            coin += Decimal(item["bought"])
            money -= Decimal(item["matecoin_price"]) * Decimal(item["bought"])

        if item["sold"] is not None:
            coin -= Decimal(item["sold"])
            money += Decimal(item["sold"]) * Decimal(item["matecoin_price"])

    capital = {"earned_money": str(money), "matecoin_account": str(coin)}
    with open("profit.json", "w") as k:
        json.dump(capital, k, indent=2)
