import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        data = json.load(f)
    coin_balance = Decimal("0")
    fiat_balance = Decimal("0")
    for item in data:
        price = Decimal(item["matecoin_price"])
        if item["bought"] is not None:
            volume = Decimal(item["bought"])
            coin_balance += volume
            fiat_balance -= volume * price
        if item["sold"] is not None:
            volume = Decimal(item["sold"])
            coin_balance -= volume
            fiat_balance += volume * price
    result = {
        "earned_money": str(fiat_balance),
        "matecoin_account": str(coin_balance)
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
