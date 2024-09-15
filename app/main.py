import json
from decimal import Decimal


def calculate_profit(name_file):
    with open(name_file) as f:
        trades = json.load(f)
        cash = 0
        coin = 0
        for day in trades:
            if day["bought"] is not None:
                coin += Decimal(day["bought"])
                cash -= Decimal(day["matecoin_price"]) * Decimal(day["bought"])
            if day["sold"] is not None:
                coin -= Decimal(day["sold"])
                cash += Decimal(day["matecoin_price"]) * Decimal(day["sold"])
    result = {
        "earned_money": str(cash),
        "matecoin_account": str(coin)
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
